from django.shortcuts import render, redirect
from event.models import Event

from .forms import SignupForm
from django.db.models.query_utils import Q
 

def index(request):
    events=[]
    if(request.user.id):
        events = Event.objects.filter(Q(publish=True)|Q(created_by=request.user))
    return render(request, 'core/index.html', {"events":events})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })