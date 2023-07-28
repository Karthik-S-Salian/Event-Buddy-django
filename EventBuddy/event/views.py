from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm
from .models import Event

def events(request):
    query = request.GET.get('query', '')
    # category_id = request.GET.get('category', 0)

    events = Event.objects.filter(publish=True)

    # if query:
    #     items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'event/events.html', {
        'events': events,
        'query': query,
    })


@login_required
def detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    events = Event.objects.filter(publish=True)[:3]
    print(events)
    return render(request, 'event/detail.html', {
        'event': event,
        "related_events":events,
        "tags":event.tags.all()
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('event:detail', pk=item.id)
    else:
        form = EventForm()

    return render(request, 'event/form.html', {
        'form': form,
        'title': 'New Event',
    })

@login_required
def edit(request, pk):
    event = get_object_or_404(Event, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()

            return redirect('event:detail', pk=event.id)
    else:
        form = EventForm(instance=event)

    return render(request, 'event/form.html', {
        'form': form,
        'title': 'Edit event',
    })

@login_required
def delete(request, pk):
    event = get_object_or_404(Event, pk=pk, created_by=request.user)
    event.delete()

    return redirect('/')