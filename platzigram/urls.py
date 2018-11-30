#from django.contrib import admin
from django.urls import path


#views
#from platzigram import views
#or
from platzigram.views import hello_world,hi,say_hi

urlpatterns = [
    path('hello-world/',hello_world),
    path('hi/', hi),
    path('say_hi/<str:name>/<int:age>/',say_hi),
]
