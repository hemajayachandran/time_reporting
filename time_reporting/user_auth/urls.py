from django.urls import path
from .views import HomeView, LoginPageView, signup

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('login/', LoginPageView.as_view(), name="loginto"),
    path('signup/', signup, name="signup"),
]
