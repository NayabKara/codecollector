from django.forms import ModelForm
from .models import Frameworks

class FrameworksForm(ModelForm):
  class Meta:
    model = Frameworks
    fields= ['description', 'name']