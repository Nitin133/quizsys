from django.conf.urls import url
from . import views

urlpatterns=[
    url('quizpage',views.quizpage,name="quizpage"),
    url('result',views.result,name="result"),
    url("start",views.start,name="start"),
    url('home',views.home,name="home"),
    url('nextques',views.nextques,name="nextques"),
    url('backques',views.backques,name="backques"),
    url('regs',views.regs,name="regs"),
    
  
    url('login',views.login,name="login"),

]