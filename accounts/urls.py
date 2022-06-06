from django.urls import path, include
from .views import LoginDetailView,RegistrationView,logout_user
urlpatterns = [
    path('login/', LoginDetailView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
]


