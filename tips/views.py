from django.shortcuts import render, redirect
from . models import FreeTipsGame, vipTipsGame, punterTipsGame
from django.utils import timezone
from . forms import RegistrationForm
from django.contrib import messages

#Today's Free tips method
def home(request):
    return redirect("https://palsbetc.herokuapp.com/")

#Free tips results method
def results(request):

    model = FreeTipsGame

    template_name = 'free/results.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(ticket__published=True)

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/results.html', args)

def payment(request):
    return render(request, 'free/payment.html')

def pricing(request):
    return render(request, 'free/pricing.html')

def viptips(request):
    return render(request, 'free/viptips.html')

def signup(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.save()

            messages.success(request, 'Registration successful.You can now log in with your username and password')

            return redirect('/accounts/login')

    else:
        form = RegistrationForm()


    return render(request, 'free/signup.html', {'form':form})

def viptipsgames(request):

    model = vipTipsGame

    template_name = 'viptipsgames.html'

    args = {}

    home_page_teams = vipTipsGame.objects.filter(ticket__published=True)

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/viptipsgames.html', args)

def punterpick(request):

    model = punterTipsGame

    template_name = 'punterpick.html'

    args = {}

    home_page_teams = punterTipsGame.objects.filter(ticket__published=True)

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/punterpick.html', args)

def twitter(request):
    return redirect("https://twitter.com/predictpoa/")

def facebook(request):
    return redirect("https://web.facebook.com/Predictpoacom-261755261206726/?modal=admin_todo_tour/")
