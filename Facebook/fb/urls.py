
from django.urls import path

from fb import views



urlpatterns = [
    path('',views.Sample,name='index'),
    path('index/',views.login_request,name='index')
]