from django.urls import path
from .views import index_view, profile

urlpatterns = [
    path('', index_view, name="Home"),
    path('profile/', profile, name='User profile'),
]