from django.urls import path
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('login_user/', login_view, name="Login"),
    path('register/', register_view, name="Register"),
    path('logout_user/', logout_view, name="Logout"),
]
