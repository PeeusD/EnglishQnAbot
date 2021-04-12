
from telegram.ext import Updater
import schedule
from ques_sets import schedulling_query, schedulling_query2
import time



schedule.every().day.at("03:35").do(schedulling_query)    ##### SET 03:35  <--------------  CHANGE HERE FOR DEBUGGING  ------>
schedule.every().day.at("06:35").do(schedulling_query2 )    ##### SET 06:35  <--------------  CHANGE HERE FOR DEBUGGING  ------>

while True:
  
    # Checks whether a scheduled task... 
    #... is pending to run or not
    schedule.run_pending()
    time.sleep(1)            


updater = Updater(TOKEN)  
updater.start_polling()
updater.idle()
