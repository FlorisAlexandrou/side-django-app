from django.urls import path
from mat_app import views

urlpatterns = [
    path('', views.ClientList.as_view()),
    path('<int:pk>/', views.ClientDetail.as_view()),
]
