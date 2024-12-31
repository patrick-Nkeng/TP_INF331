from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
# Create your views here.

def register(request):
     if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
     else:
         form = CreateUserForm()
     context = {
          'form':form
     }
     return render(request,'user/register.html',context) 


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

def profile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)

def redirect_view(request):
    # This view redirects to the 'makerequest' page
    return redirect('makerequest')

def makerequest(request):
       return render(request,'user/makerequest.html') 

"""
from django.shortcuts import render
import os
import google.generativeai as genai
import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ChatRequestSerializer

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
        pdf_path = '/home/fkdi/Downloads/projetGENIE/repare_front/dokumen.pub_the-complete-a-guide-to-pc-repair.pdf'
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
         #   initial_prompt = vous êtes un chatbot d'assistance amical de la société Techmain. 
          #  Votre objectif principal est de recommander une solution au problème de maintenance matérielle 
           # ou logicielle de l'ordinateur des utilisateurs

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

# In your urls.py, ensure proper routing
# urlpatterns = [
#     path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),
# ]

def home(request):
    return render(request, 'home.html')

def user_profil(request):
    return render( request, 'user_profil.html')

def notification(request):
    return render(request, 'notification.html')

def formulaire(request) :
    return render(request, 'formulaire.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def home_tech(request):
    return render(request, 'home_tech.html')

def staff(request):
       return render(request,'staff.html') 

"""