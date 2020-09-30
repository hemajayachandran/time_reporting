from django.urls import path
from . import views
from django.conf.urls.static import static
from time_reporting import settings

urlpatterns = [
    path('login/', views.login, name="loginto"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
