from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('create-account/', 
    CreateAccountView.as_view(), 
    name='createAccount')
    ,
    path('<int:pk>/',
    MyAccountView.as_view(),
    name='myAccount'
    )
]
