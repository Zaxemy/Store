from django.urls import path
from users import views
from users.views import login, registration


app_name = 'users'

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration')    
]