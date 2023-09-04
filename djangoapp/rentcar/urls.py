from django.urls import path
from rentcar import views

app_name = 'rentcar'

urlpatterns = [
    path('', views.index, name='index'),

]
