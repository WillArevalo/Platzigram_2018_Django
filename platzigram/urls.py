#from django.contrib import admin
from django.urls import path


#views
#from platzigram.views import hello_world,hi,say_hi
#or
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
	#main
    path('hello-world/',local_views.hello_world),
    path('hi/', local_views.hi),
    path('say_hi/<str:name>/<int:age>/',local_views.say_hi),

    #posts
    path('posts/', posts_views.list_posts),
]
