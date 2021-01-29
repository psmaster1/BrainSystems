from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import api
from . import views


app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrierung/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('impressum/', views.impressum, name='impressum'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('backend/home/', views.backend, name='backend'),
    path('backend/meine-daten/', views.userdata, name='userdata'),
    path('backend/chatbot/', views.chatbot, name='chatbot'),
    path('api/chatbot/', csrf_exempt(api.chatbot), name='api_chatbot'),
]

