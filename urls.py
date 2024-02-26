from django.urls import path 
from .views import main,contact_view
from .views import main
urlpatterns = [
    path('',main, name="main" ),
    path('contact/',contact_view,name='contact')

]

