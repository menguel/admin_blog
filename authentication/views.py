from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect # Pour rediriger vers des pages 
from django.contrib.auth.models import User # Classe des utilisateurs
from django.contrib import messages # Pour les messages 
from django.contrib.auth import authenticate, login, logout # Pour les authentifications 
from siteblog import settings # Imprter les paramètres de Django
from django.core.mail import send_mail, EmailMessage # Envoie de message 

from .token import generatorToken
# Create your views here.


def home(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=username):
            messages.error(request, 'Ce nom a été déjà pris')
            return redirect('register')
        
        if User.objects.filter(email=email):
            messages.error(request, 'Cette email a déjà un compte')

            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, 'Le nom doit etre alpha numérique')

            return redirect('register')
        
        if password != password1:
            messages.error(request, 'Les deux mots de passe ne coincident pas')
            return redirect('register')

        mon_user = User.objects.create_user(username, email, password)
        mon_user.first_name = firstname
        mon_user.last_name = lastname
        mon_user.is_active = False
        mon_user.save()
        messages.success(request, 'Votre compte a été créé avec succes')

        # envoie d'email de bienvenue

        subject = "Bienvenu sur le blog de Joseph"
        message = "Bienvenue" + mon_user.first_name + ' ' + mon_user.last_name + "\nNous sommes heureux de vous compter parmi nous \n\n\n Merci \n\n M35"
        from_email = settings.EMAIL_HOST_USER
        to_list = [mon_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        # Email de confirmation

        current_site = get_current_site(request)
        email_subject = "Confirmation de l'adresse email sur le blog de Joe"
        messageConfirm = render_to_string("emailconfirm.html", {
            'name' : mon_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(mon_user.pk)), 
            'token' : generatorToken.make_token(mon_user)
        })

        email = EmailMessage(
            email_subject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [mon_user.email]
        )

        email.fail_silently = False

        email.send()
        return redirect('/login')
        
    return render(request, 'authentication/register.html')

def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'authentication/index.html', {'firstname' : firstname})
        elif my_user.is_active == False:
            messages.error(request, "Vous n'avez pas confirmé votre adresse email !!!")
        else :
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')
    return render(request, 'authentication/login.html')



def logOut(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Votre compte a bien été activé félicitation connectez vous maintenant")
        return redirect('login')
    
    else:
        messages.error(request, "L'activation de votre a échoué !!!")
        return redirect('home')

