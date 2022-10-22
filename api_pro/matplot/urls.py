from django.urls import path
from .views import Matplot,Matplot1,Matplot2
urlpatterns = [
    path('api/',Matplot,name = 'Matplot'),
    path('api1/',Matplot1, name='matplot'),
    path('api2/',Matplot2, name='matplot'),
]