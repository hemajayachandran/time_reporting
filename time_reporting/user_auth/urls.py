from django.urls import path
from .views import home, login, signup, logout
from django.conf.urls.static import static
from time_reporting import settings

urlpatterns = [
    path('login/', login, name="loginto"),
    path('signup/', signup, name="signup"),
    path('home/', home, name="home"),
    path('logout/', logout, name="logout"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
