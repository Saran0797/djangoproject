"""
URL configuration for djangoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from Users.views import profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", include("Users.urls")),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="Login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="Logout"),
    path("profile/", profile, name="profile"),
    path("password_reset/", auth.views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="password_reset"),
    path("password_reset/done/",
         auth.views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",
         auth.views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name="password_reset_confirmation"),
    path("password_reset_complete/",
         auth.views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),
    path("", include("blog.urls"))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
