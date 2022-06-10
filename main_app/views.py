from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
from .models import Language, Example
from .forms import FrameworksForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# class Language():
#   def __init__(self, name, use, description):
#     self.name = name
#     self.use = use
#     self.description = description

# languages = [
#   Language('HTML', 'frontend', 'used for structure- think of the skeleton'),
#   Language('CSS', 'frontend', 'used for styling and design'),
#   Language('Javascript', 'frontend', 'used for making interactive pages'),
# ]
#commented out because of db connection error instead of deleting

# Create your views here.


class LanguageCreate(CreateView, LoginRequiredMixin): 
  model = Language
  field= '__all__'
  success_url = '/languages/'

  def form_valid(self, form): 
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
class LanguageUpdate(UpdateView, LoginRequiredMixin):
  model = Language
  fields = ['use', 'description']

@login_required
class LanguageDelete(DeleteView, LoginRequiredMixin):
  model = Language
  success_url = '/languages/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def index(request):
  languages = Language.objects.all(user=request.user)
  return render(request, 'languages/index.html', { 'languages': languages })

def languages_details(request, language_id):
  language = Language.objects.get(id=language_id)

  examples_language_doesnt_have = Example.objects.exclude(id__in= language.examples.all().values_list('id'))
  frameworks_form = FrameworksForm()
  return render(request, 'languages/detail.hitml', {'language' : language, 'frameworks_form': frameworks_form, 'examples': examples_language_doesnt_have})

@login_required
def add_frameworks(request, language_id):
  form = FrameworksForm(request.POST)
  if form.is_valid():
    new_frameworks = form.save(commit=False)
    new_frameworks.language_id = language_id
    new_frameworks.save()
  return redirect('detail', language_id=language_id)


class ExampleList(ListView, LoginRequiredMixin):
  model = Example


class ExampleDetail(DetailView, LoginRequiredMixin):
  model = Example


class ExampleCreate(CreateView, LoginRequiredMixin):
  model = Example
  fields = '__all__'


class ExampleUpdate(UpdateView, LoginRequiredMixin):
  model = Example
  fields = ['explanation']


class ExampleDelete(DeleteView, LoginRequiredMixin):
  model = Example
  success_url = '/examples/'

def assoc_example(request, language_id, example_id):
  Language.objects.get(id=language_id).examples.add(example_id)
  return redirect('detail', language_id=language_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
  #user submits the signup form
  #create new user
    form = UserCreationForm(request.POST)
    if form.is_valid():
      #  add the user to the database
      user = form.save()
      # log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)