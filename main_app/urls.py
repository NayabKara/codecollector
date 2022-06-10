from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('languages/', views.index, name='index'),
  path('languages/create/', views.LanguageCreate.as_view(), name='languages_create'),
  path('languages/<int:pk>/update/', views.LanguageUpdate.as_view(), name='languages_update'),
  path('languages/<int:pk>/delete/', views.LanguageDelete.as_view(), name='languages_delete'),
  #'languages/:id'
  path('languages/<int:language_id>', views.languages_details, name="detail"),
  path('languages/<int:language_id>/add_frameworks', views.add_frameworks, name='add_frameworks'),

  #examples urls
  path('languages/<int:language_id>/assoc_example/<int:example_id>/', views.assoc_example, name='assoc_example'),
  # unassociate a example  and language
  path('languages/<int:language_id>/unassoc_example/<int:example_id>/', views.unassoc_example, name='unassoc_example'),
  path('examples/', views.ExampleList.as_view(), name='examples_index'),
  path('examples/<int:pk>/', views.ExampleDetail.as_view(), name='examples_detail'),
  #examples urls for CRUD
  path('examples/create/', views.ExampleCreate.as_view(), name='examples_create'),
  path('examples/<int:pk>/update/', views.ExampleUpdate.as_view(), name='examples_update'),
  path('examples/<int:pk>/delete/', views.ExampleDelete.as_view(), name='examples_delete'),
  #auth
  path('accounts/signup/', views.signup, name='signup')
] 