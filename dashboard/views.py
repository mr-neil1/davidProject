# dashboard/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    """Affiche la page principale"""
    return render(request, 'dashboard/index.html')

def fetch_flask_data(request):
    """API interne qui appelle Flask et renvoie le JSON au Front-end"""
    FLASK_URL = "http://127.0.0.1:5001/raw-data"
    
    try:
        response = requests.get(FLASK_URL, timeout=1)
        data = response.json()
    except Exception:
        data = {"error": "Service Flask hors ligne", "value": "N/A"}
        
    return JsonResponse(data)