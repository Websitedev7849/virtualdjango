from django.http import HttpResponse, QueryDict
from product.Product import Product
import json


def about(request):
    return HttpResponse(f"""
        path: {request.path}\n\n
        query: { QueryDict( request.META['QUERY_STRING'] ).dict() }
    """)

def home(request):
    return HttpResponse("Home page")

def getPrice(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # product = Product(body['url'])
    return HttpResponse( body )


"""
/home/Websitedev7849/virtualdjango/project
/home/Websitedev7849/virtualdjango/project/project
mysite-virtualenv
"""