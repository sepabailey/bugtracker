from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from bugticket.forms import LoginForm, SignupForm
from bugticket.models import CustomUser, Ticket
from django.contrib.auth.decorators import login_required
from bugticket.forms import TicketForm


@login_required
def index(request):
    user_data = CustomUser.objects.all()
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'index.html', {
        'user_data': user_data, 'form': form
    })


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def adduser(request):
    html = "signup.html"
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
            )
        new_user.save()
        login(request, new_user)
        return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, html, {'form': form})


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})
