
from django.contrib import admin
from django.urls import path,include
from users.views import UserRegistrationView,LoginView

urlpatterns = [
   path('api-auth/', include('rest_framework.urls')),
    path('api/users/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/users/login/', LoginView.as_view(), name='api-login'),
    


]
