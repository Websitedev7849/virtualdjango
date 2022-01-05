from django.http import HttpResponse, QueryDict
from product.Product import Product


def about(request):
    return HttpResponse(f"""
        path: {request.path}\n\n
        query: { QueryDict( request.META['QUERY_STRING'] ).dict() }
    """)

def home(request):
    return HttpResponse("Home page")

def getPrice(request):
    url = request.GET["url"]
    product = Product(url)
    return HttpResponse( product.toString() )


"""
/home/Websitedev7849/virtualdjango/project
/home/Websitedev7849/virtualdjango/project/project
mysite-virtualenv
"""