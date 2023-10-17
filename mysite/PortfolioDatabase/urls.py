from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.Home, name="Home"),
    path('hobbies/', views.Hobbies, name="Hobbies"),
    path('hobbies/<int:id>', views.hobDetail, name="HobDetail"),
    path('portfolio/', views.Portfolio, name="Portfolio"),
    path('portfolio/<int:id>', views.PortDetail, name="PortDetail"),
    path('contact/', views.Contact, name="Contact"),
    path('contact/addcontact', views.Create_contact, name="create_contact"),
    path('portfolio/create_port', views.Create_port, name="create_port"),
    path('portfolio/update/<int:id>', views.Update_port, name="update_port"),
    path('portfolio/delete/<int:id>', views.Delete_port, name="delete_port")
]