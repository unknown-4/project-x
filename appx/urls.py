from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login_user", views.login_user, name="login"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("loginfailed",views.loginfailed, name="loginfailed"),
    path('verify/<str:email>', views.verify),
]
