from django.urls import path
from . import views
from .views import ChatbotAPIView
from .views import chatbot, NotificationListView, NotificationUpdateView

urlpatterns =[
  
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff,  name='dashboard-staff'),
    path('product/',views.product,  name='dashboard-product'),
    path('order/',views.order,  name='dashboard-order'),
    path('chat/', ChatbotAPIView.as_view(), name='dashboard-chatbot'),
    # Or if you prefer a more RESTful approach
    path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('chatbot/', chatbot, name= 'dashboard-chatbot'),
     path('notifications/', NotificationListView.as_view(), name='notifications'),  # Liste des notifications
    path('notifications/mark-as-read/<str:pk>/', NotificationUpdateView.as_view(), name='mark-as-read'),  # Marquer une notification comme lue
]