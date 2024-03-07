from django.urls import path
from accounts.views import RegisterView,LoginView
from home.views import BlogView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('home/',BlogView.as_view()),
]
