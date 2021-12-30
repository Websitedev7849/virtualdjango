from django.http import HttpResponse, QueryDict
import threading

class HourCounter:
    def __init__(self):
        self.hour_count = 0

    def incrementCount(self):
        self.hour_count = self.hour_count + 1

hour_counter = HourCounter()

# function to call HourCounter.incrementCount at ever 1 hour interval interval
def increaseHours():
    global hour_counter
    hour_counter.incrementCount()
    threading.Timer(60 * 60, increaseHours).start()
  

increaseHours()

def about(request):
    return HttpResponse(f"""
        path: {request.path}\n\n
        query: { QueryDict( request.META['QUERY_STRING'] ).dict() }
    """)

def home(request):
    return HttpResponse("Home page")

def getHourCount(request):
    return HttpResponse(f"hour_count : {hour_counter.hour_count}")

