from django.urls import path
from . import views  

urlpatterns = [
   
    path('alerts/', views.alerts_view, name='alerts'),
    path('map/', views.map_view, name='map'),
    path('profile/', views.profile_view, name='profile'),
]