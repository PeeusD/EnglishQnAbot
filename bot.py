
from time import sleep
import Pos.Adjective, Pos.Adverb, Pos.Articles, Pos.Conditional, Pos.verb, Pos.Noun, Pos.Preposition, Pos.Pronoun, Pos.Sub_Agrmt, Pos.Tense, Pos.Narration
import Fillers.Fill_pt1, Fillers.Fill_pt2, Fillers.Fill_pt3, Fillers.Fill_pt4, Fillers.Fill_pt5, Fillers.Fill_pt6
import datetime, random, logging, asyncio
from telegram import Bot
from telegram.constants import ChatAction, ParseMode
from telegram.ext import Application, CommandHandler
from os import getenv
from functools import wraps
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = getenv('TOKEN')
chat_id = getenv('CHAT_ID')
bot = Bot(token=TOKEN)
USER1 = int(getenv('USER1'))
# USER2 = int(getenv('USER2'))


LIST_OF_ADMINS = [USER1]

async def restricted(func):
    @wraps(func)
    async def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id in LIST_OF_ADMINS:
            await bot.send_message(chat_id=user_id, text="Status: RUNNING...")
            return
        return func(update, context)
    return wrapped

class GrammarScheduler:
  def __init__(self, partsOfSpeech) -> None:
      self.pos = partsOfSpeech
      self.loop = asyncio.get_event_loop()

  def ques_polling(self):
        return self.loop.run_until_complete(self._ques_polling())

  async def _ques_polling(self):
    for i in range(len(self.pos.questions)):
      await bot.send_chat_action(chat_id=chat_id, action = ChatAction.TYPING)

      await asyncio.sleep(4)
      options = ['A', 'B', 'C', 'D', 'E']
      #shuffling the options 
      idx = range(len(options))
      i1, i2 = random.sample(idx, 2)
      options[i1], options[i2] = options[i2], options[i1]
      #sending question in poll formt to the supergroup
      message = await bot.send_poll(chat_id=chat_id, question=self.pos.questions[i], options=options)
      
      # for i in range(1,10):
      #   await bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text=str(i))

      #adding html formatting..
      op_tg ='<b>'
      cls_tg ='</b>'
      formated_ans = op_tg + self.pos.sol[i] + cls_tg

      await asyncio.sleep(10)  #delay timing 25 sec between ques and ans
      #for sending ans msg to the supergroup
      await bot.send_message(chat_id=chat_id, text=formated_ans, parse_mode=ParseMode.HTML)  


adj_obj = GrammarScheduler(Pos.Adjective)
adv_obj = GrammarScheduler(Pos.Adverb)
article_obj = GrammarScheduler(Pos.Articles)
cond_obj = GrammarScheduler(Pos.Conditional)
noun_obj = GrammarScheduler(Pos.Noun)
prep_obj = GrammarScheduler(Pos.Preposition)
pro_obj = GrammarScheduler(Pos.Pronoun)
subAgmt_obj = GrammarScheduler(Pos.Sub_Agrmt)
tense_obj = GrammarScheduler(Pos.Tense)
verb_obj = GrammarScheduler(Pos.verb)
narr_obj = GrammarScheduler(Pos.Narration)

adj_obj.ques_polling() # for debug

@restricted
def start_scheduller(update, context):
    admn_chat_id = update.message.chat_id
    days = (0, 1, 2, 3, 4, 5, 6)
    minutes = 5
    context.bot.send_message(chat_id=admn_chat_id, text='Scheduler Started!')
    context.job_queue.run_daily(adv_obj.ques_polling(), time=datetime.time(hour=10, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(article_obj.ques_polling(), time=datetime.time(hour=11, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(cond_obj.ques_polling(), time=datetime.time(hour=12, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(noun_obj.ques_polling(), time=datetime.time(hour=13, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(prep_obj.ques_polling(), time=datetime.time(hour=14, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(pro_obj.ques_polling(), time=datetime.time(hour=15, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(subAgmt_obj.ques_polling(), time=datetime.time(hour=16, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(tense_obj.ques_polling(), time=datetime.time(hour=17, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(verb_obj.ques_polling(), time=datetime.time(hour=18, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(adj_obj.ques_polling(), time=datetime.time(hour=19, minute=minutes), days=days, context=admn_chat_id)
    context.job_queue.run_daily(narr_obj.ques_polling(), time=datetime.time(hour=20, minute=minutes), days=days, context=admn_chat_id)
    
    # This is for different time scheduler(every 10 sec or every 1 hr)
    # context.job_queue.run_repeating(callback_auto_message, 10, context=chat_id, name=str(chat_id))
    # context.job_queue.run_once(callback_auto_message, 3600, context=chat_id)

@restricted
def stop_scheduller(update, context):
    admn_chat_id = update.message.chat_id
    job = context.job_queue.get_jobs_by_name(str(admn_chat_id))
    job[0].schedule_removal()
    context.bot.send_message(chat_id=admn_chat_id, text='Stopped Scheduler!')



def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("auto_start", start_scheduller))
    application.add_handler(CommandHandler("stop", stop_scheduller))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()





















  

