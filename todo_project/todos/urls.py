from django.urls import path
from .  import views
# Create your views here.
urlpatterns  = [
     path('',views.ListTodo.as_view()),
     path('<int:pk>/', views.DetailTodo.as_view()),
]