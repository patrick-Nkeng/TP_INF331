from django.urls import path
from .views import home
from .views import user_profil
from .views import notification
from .views import formulaire
from .views import chatbot
from .views import home_tech
from .views import ChatbotAPIView
from .views import makerequest
from .views import redirect_view, makerequest

from . import views




urlpatterns = [
    path('', home, name='home'),
    path('chat/', ChatbotAPIView.as_view(), name='chatbot_api'),
    # Or if you prefer a more RESTful approach
    path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('user_profil/', user_profil,  name= 'user_profil'),
    path('notification/', notification, name= 'notification'),
    path('formulaire/', formulaire, name= 'formulaire'),
    path('chatbot/', chatbot, name= 'chatbot'),
    path('home_tech/', home_tech, name= 'home_tech'),
    path('staff/',views.staff,  name='users-staff'),
    path('redirect/', redirect_view, name='redirect'),
    path('makerequest/', makerequest, name='makerequest'),

    
]