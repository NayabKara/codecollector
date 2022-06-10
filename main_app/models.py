from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

NAMES = (
  ('E', 'Express '),
  ('D', 'Django'),
  ('R', 'React'),
  ('A', 'Angular'),
)

class Example(models.Model):
  explanation = models.CharField(max_length=500)

  def __str__(self):
    return self.explanation
  
  def get_absoloute_url(self):
    return reverse('examples_detail', kwargs={'pk': self.id})

# Create your models here.
class Language(models.Model):
  name = models.CharField(max_length=100)
  use = models.CharField(max_length=500)
  description = models.CharField(max_length=1000)
  examples = models.ManyToManyField(Example)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'language_id': self.id})

class Framework(models.Model):
  description = models.CharField(max_length=500)
  name = models.CharField(
    max_length=1,
    choices = NAMES,
    default= NAMES[0][0]
    )
  language = models.ForeignKey(Language, on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.get_name_display()} on {self.description}" 
