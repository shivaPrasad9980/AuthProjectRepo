from django.urls import path 
from . import views 

urlpatterns = [
    path('home/',views.home_view),
    path('python/',views.python_view),
    path('java/',views.java_view),
    path('aptitude/',views.aptitude_view),
    path('signup/',views.signup_view),
]
