from django.shortcuts import render
from django.http import HttpResponse

class Language():
  def __init__(self, name, use, description):
    self.name = name
    self.use = use
    self.description = description

languages = [
  Language('HTML', 'frontend', 'used for structure- think of the skeleton'),
  Language('CSS', 'frontend', 'used for styling and design'),
  Language('Javascript', 'frontend', 'used for making interactive pages'),
]

# Create your views here.

def home(request):
  return HttpResponse('<h1> Welcome</h1>')

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'languages/index.html', { 'languages': languages })