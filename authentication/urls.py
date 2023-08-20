from django.urls import path
from authentication.views import home, register, logIn, logOut, activate

urlpatterns = [
    path('', home, name="home"),
    path('register', register, name='register' ),
    path('login', logIn, name='login'),
    path('logout', logOut, name='logout'),
    path('activate/<uidb64>/<token>', activate, name="activate" )
]