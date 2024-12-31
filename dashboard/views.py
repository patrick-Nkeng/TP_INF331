from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
import os
import google.generativeai as genai
import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ChatRequestSerializer
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated  


class ChatbotAPIView(APIView):
    parser_classes = [JSONParser]  # Explicitly define JSON parser
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configure Gemini API
        genai.configure(api_key="AIzaSyDwJPtIOn-DNEX5RR29jh0wjdzp3L5grr0")
        
        # Initialize model and chat
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        
        # Load PDF content
        self.pdf_content = self._load_pdf

    def _load_pdf(self):
        pdf_path = '/home/fkdi/Downloads/repare_front/dokumen.pub_the-complete-a-guide-to-pc-repair.pdf'
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                return ' '.join([page.extract_text() for page in pdf_reader.pages]).lower().strip()
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return ""

    def post(self, request):
        serializer = ChatRequestSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_input = serializer.validated_data['message']

        try:
            # Initial context for maintenance assistance
            initial_prompt = """vous êtes un chatbot d'assistance amical de la société Techmain. 
            Votre objectif principal est de recommander une solution au problème de maintenance matérielle 
            ou logicielle de l'ordinateur des utilisateurs"""

            # Check if input is related to maintenance
            
            response = self.model.generate_content(f"{initial_prompt}Based on the maintenance guide, the following information is relevant: {self.pdf_content}. User query: {user_input}"f"Based on the maintenance guide, the following information is relevant: {self.pdf_content}. User query: {user_input}")
            bot_response = response.text
            
            return Response({
                'message': bot_response
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        # Add a GET method to handle OPTIONS and provide information
        return Response({
            'message': 'Chatbot API. Use POST to send messages.',
            'allowed_methods': ['POST', 'OPTIONS']
        }, status=status.HTTP_200_OK)

    def options(self, request):
        # Explicitly handle OPTIONS method
        response = Response()
        response['Allow'] = 'POST, OPTIONS'
        response['Content-Type'] = 'application/json'
        return response

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request,'dashboard/index.html') 

@login_required(login_url='user-login')
def staff(request):
       return render(request,'dashboard/staff.html') 

@login_required(login_url='user-login')
def product(request):
       return render(request,'dashboard/product.html') 


@login_required(login_url='user-login')
def order(request):
       return render(request,'dashboard/order.html') 

def chatbot(request):
    return render(request, 'dashboard/chatbot.html')

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users only

    def get(self, request):
        # Récupérer les notifications pour l'utilisateur connecté
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class NotificationUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            # Vérifie que la notification appartient à l'utilisateur connecté
            notification = Notification.objects.get(pk=pk, user=request.user)
        except Notification.DoesNotExist:
            return Response({'error': 'Notification not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

        notification.is_read = True
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
"""
def register(request):
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valide():
                  user = form.save()
                  login(request, user)
                  return redirect('home')
            else:
                  form = UserCreationForm()
            return render(request, 'users/register.html',{'form':form})

def user_login(request):
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user= authenticate (request, username = username, password=password)
            if user is not None:
                  login(request, user)
                  return redirect('home')
      return render(request, 'users/login.html')

def user_logout(request):
      logout(request)
      return redirect('home')

def user_home(request):
    return render(request, 'users/home.html')
      

"""