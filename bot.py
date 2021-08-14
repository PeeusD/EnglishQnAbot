from ques_sets import schedulling_query, schedulling_query2
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, render_template



sched = BackgroundScheduler()

# Schedules job_function to be run on every day at 3:35 am

sched.add_job(schedulling_query, 'cron', hour='03', minute='35')   # SET utc 03:35  <--------------  CHANGE HERE FOR DEBUGGING  ------>
sched.add_job(schedulling_query2, 'cron', hour='06', minute='35')   # SET utc 06:35  <--------------  CHANGE HERE FOR DEBUGGING  ------>
sched.start()


app = Flask(__name__)
@app.route("/")
def index():
    return render_template ("index.html")
    

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)