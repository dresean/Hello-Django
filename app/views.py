from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("""
  You are at the index page!
  """)
  
def notes_detail(request, notes_id):
  return HttpResponse("""
  You are at the Notes Page
  """)

def 
# Create your views here.
