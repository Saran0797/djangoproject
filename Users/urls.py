from django.urls import path
from Users.views import register


urlpatterns = [
    path('', register, name="register")
]