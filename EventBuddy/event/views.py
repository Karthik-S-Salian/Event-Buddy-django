from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm, CommentForm
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
    comments = event.comments.filter()[:20]
    events = Event.objects.filter(publish=True)[:3]

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.event = event
            new_comment.created_by = request.user
            new_comment.event = event
             # Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()

    return render(request, 'event/detail.html', {
        'event': event,
        "related_events":events,
        "tags":event.tags.all(),
        'comments': comments,
        'comment_form': comment_form
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