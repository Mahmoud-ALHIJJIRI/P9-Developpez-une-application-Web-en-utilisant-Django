from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
]
