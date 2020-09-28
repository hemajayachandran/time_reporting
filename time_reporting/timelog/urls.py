from django.urls import path
from . import views

app_name = "timelog"
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),

]
