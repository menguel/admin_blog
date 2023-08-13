from django.urls import path
from authentication.views import home, register, logIn, logOut

urlpatterns = [
    path('', home, name="home"),
    path('register', register, name='register' ),
    path('login', logIn, name='login'),
    path('logout', logOut, name='logout'),
]