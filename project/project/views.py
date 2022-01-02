from django.http import HttpResponse, QueryDict
import threading
from datetime import datetime
import schedule

class HourCounter:
    def __init__(self):
        self.initial_date = datetime.now().strftime('%x')
        self.initial_time = f"{datetime.now().strftime('%I')}:{datetime.now().strftime('%M')} {datetime.now().strftime('%p')}"
        print(self.initial_time)
        self.hour_count = 0

    def incrementCount(self):
        self.hour_count = self.hour_count + 1

hour_counter = HourCounter()


schedule.every(1).hours.do(hour_counter.incrementCount)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def about(request):
    return HttpResponse(f"""
        path: {request.path}\n\n
        query: { QueryDict( request.META['QUERY_STRING'] ).dict() }
    """)

def home(request):
    return HttpResponse("Home page")

def getHourCount(request):
    return HttpResponse(f"initial_time: {hour_counter.initial_time}; initial_date: {hour_counter.initial_date}; hour_count : {hour_counter.hour_count}")


set_interval(schedule.run_pending, 10)

"""
/home/Websitedev7849/virtualdjango/project
/home/Websitedev7849/virtualdjango/project/project
mysite-virtualenv
"""