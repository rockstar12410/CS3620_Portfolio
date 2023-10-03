from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name="Home"),
    path('hobbies/', views.Hobbies, name="Hobbies"),
    path('portfolio/', views.Portfolio, name="Portfolio"),
    path('contact/', views.Contact, name="Contact")
]