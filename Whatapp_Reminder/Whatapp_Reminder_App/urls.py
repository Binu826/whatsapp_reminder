from django.urls import path
from Whatapp_Reminder_App import views
urlpatterns = [
    path('', views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('send_welcome_email',views.send_welcome_email,name='send_welcome_email'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('main',views.mainpage,name='main'),
    path('contacts',views.contacts,name='contacts'),
    path('profile/<int:id>',views.profile,name='profile'),
   
]