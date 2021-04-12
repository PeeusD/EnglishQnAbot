
from time import sleep
import Pos.Adjective, Pos.Adverb, Pos.Articles, Pos.Conditional, Pos.verb, Pos.Noun, Pos.Preposition, Pos.Pronoun, Pos.Sub_Agrmt, Pos.Tense
import Fillers.Fill_pt1, Fillers.Fill_pt2, Fillers.Fill_pt3, Fillers.Fill_pt4, Fillers.Fill_pt5, Fillers.Fill_pt6
import datetime, random
from telegram import ChatAction, Bot, ParseMode
from os import getenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv('TOKEN')
chat_id = getenv('CHAT_ID')
bot = Bot(token=TOKEN)

x = datetime.datetime.now()  #capturing day from 0--6
x = int(x.strftime("%w"))

y = datetime.datetime.now()  #capturing (H) time in 24 frmt
y = int(y.strftime("%H"))

def schedulling_query():   #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
 
    print('...RUNNING YOUR DEV-MODE APP...FoR Err DETECTION')
    print(f"ON Todays Day--> {x} And Current time:--> {y}")
    for i in range(52):       #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
           
            
            
            if (x == 0) & (y == 3) :      # here x is days and y is 24 hr frmt timing...
              ques = Pos.Adjective.questions[i][0]
              ans = Pos.Adjective.sol[i] 
            
            elif  (x == 1) & (y == 3 ) :
              ques = Pos.Adverb.questions[i][0]
              ans = Pos.Adverb.sol[i]
            elif  (x == 2) & (y == 3 ) :
              ques = Pos.Articles.questions[i][0]
              ans = Pos.Articles.sol[i]
            elif  (x == 3) & (y == 3 ) :
              ques = Pos.Conditional.questions[i][0]
              ans = Pos.Conditional.sol[i]
            elif  (x == 4) & (y == 3) :
              ques = Pos.verb.questions[i][0]
              ans = Pos.verb.sol[i]
            elif  (x == 5) & (y == 3) :
              ques = Pos.Noun.questions[i][0]
              ans = Pos.Noun.sol[i]
            elif  (x == 6) & (y == 3) :
              ques = Pos.Preposition.questions[i][0]
              ans = Pos.Preposition.sol[i]
            elif (x == 1) & (y == 16) :
              ques = Pos.Pronoun.questions[i][0]
              ans = Pos.Pronoun.sol[i]
            
            elif  (x == 2) & (y == 16) :
              ques = Pos.Sub_Agrmt.questions[i][0]
              ans = Pos.Sub_Agrmt.sol[i]
            elif  (x == 3) & (y == 16) :
              ques = Pos.Tense.questions[i][0]
              ans = Pos.Tense.sol[i]

            else :
              print("holiday: Above days/time doesnt matched!")
              break
            
              
            # decorating bot replying to users...
            bot.send_chat_action(chat_id = chat_id, action = ChatAction.TYPING)
            sleep(4)

            
            options = ['A', 'B', 'C', 'D', 'E']
            #shuffling the options 
            idx = range(len(options))
            i1, i2 = random.sample(idx, 2)
            options[i1], options[i2] = options[i2], options[i1]

            
            #sending question in poll formt to the supergroup
            bot.send_poll(chat_id = chat_id, question = ques, options = options)
            
            #adding html formatting..
            op_tg ='<b>'
            cls_tg ='</b>'
            
            ans = op_tg + ans + cls_tg
            sleep(25)  #delay timing 25 sec between ques and ans

            #for sending messages as ans to the supergroup
            bot.send_message(chat_id = chat_id, text = ans, parse_mode = ParseMode.HTML)   



def schedulling_query2():
   #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
    print('...RUNNING YOUR DEV-MODE APP...FoR Fillers')
    print(f"ON Todays Day--> {x} And Current time:--> {y}")
    for i in range(31):       #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
           
            
            
            if (x == 0) & (y == 6) :      # here x is days and y is 24 hr frmt timing...
              ques =  Fillers.Fill_pt1.questions[i][0]
              ans = Fillers.Fill_pt1.sol[i] 
            
            elif  (x == 1) & (y == 6 ) :
              ques = Fillers.Fill_pt3.questions[i][0]
              ans = Fillers.Fill_pt2.sol[i]
            elif  (x == 2) & (y == 6) :
              ques = Fillers.Fill_pt3.questions[i][0]
              ans = Fillers.Fill_pt3.sol[i]
            elif  (x == 3) & (y == 6 ) :
              ques = Fillers.Fill_pt4.questions[i][0]
              ans = Fillers.Fill_pt4.sol[i]
            elif  (x == 4) & (y == 6) :
              ques = Fillers.Fill_pt5.questions[i][0]
              ans = Fillers.Fill_pt5.sol[i]
            elif  (x == 5) & (y == 6) :
              ques = Fillers.Fill_pt6.questions[i][0]
              ans = Fillers.Fill_pt6.sol[i]
           
          

            else :
              print("holiday: Above days/time doesnt matched!")
              break
            
              
            # decorating bot replying to users...
            bot.send_chat_action(chat_id = chat_id, action = ChatAction.TYPING)
            sleep(4)

            
            # options = ['A', 'B', 'C', 'D', 'E']
            # #shuffling the options 
            # idx = range(len(options))
            # i1, i2 = random.sample(idx, 2)
            # options[i1], options[i2] = options[i2], options[i1]
            
            ques = '<b>' + ques + '</b>'
            
            #sending question in poll formt to the supergroup
            # bot.send_poll(chat_id = chat_id, question = ques, options = options)
            bot.send_message(chat_id = chat_id, text = ques, parse_mode = ParseMode.HTML)   

            #adding html formatting..
           
            
            ans = '<i>' + ans + '</i>'
            sleep(25)  #delay timing 25 sec between ques and ans

            #for sending messages as ans to the supergroup
            bot.send_message(chat_id = chat_id, text = ans, parse_mode = ParseMode.HTML)   



  

