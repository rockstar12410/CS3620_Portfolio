from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name="Home"),
    path('hobbies/', views.Hobbies, name="Hobbies"),
    path('hobbies/<int:id>', views.hobDetail, name="HobDetail"),
    path('portfolio/', views.Portfolio, name="Portfolio"),
    path('portfolio/<int:id>', views.PortDetail, name="PortDetail"),
    path('contact/', views.Contact, name="Contact")
]