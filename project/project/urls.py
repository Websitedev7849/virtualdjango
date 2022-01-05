from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
     path(f'', views.home), # home page
    path(r"about", views.about), # about page
    path(r"getprice", views.getPrice) # get the count of hours server is runing
]
