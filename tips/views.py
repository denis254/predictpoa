from django.shortcuts import render, redirect
from . models import FreeTipsGame, vipTipsGame, punterTipsGame, Comment
from django.utils import timezone
from . forms import RegistrationForm, CommentForm
from django.contrib import messages

#Today's Free tips method
def home(request):

    model = FreeTipsGame

    template_name = 'home.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(ticket__published=True)

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/home.html', args)

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

def comment(request):

    model =  Comment

    template_name = 'comment.html'

    comments = Comment.objects.filter(published=True)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            form.instance.user = request.user

            comment = form.save()

            comment.save()

            return redirect('/home')

    else:
        form = CommentForm()


    return render(request, 'free/comment.html', {'comments':comments,
        'form':form,})
