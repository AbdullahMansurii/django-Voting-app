from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Poll, Choice


def index(request):
    """
    Main page view that displays polls.
    Shows active polls by default, with toggle to show past polls.
    """
    # Get filter parameter from request (default to 'active')
    filter_type = request.GET.get('filter', 'active')
    
    # Get all polls
    all_polls = Poll.objects.all().order_by('-created_at')
    
    # Filter polls based on selection
    if filter_type == 'active':
        # Show only active polls that haven't ended
        polls = [poll for poll in all_polls if poll.is_currently_active()]
    else:
        # Show past polls (inactive or ended)
        polls = [poll for poll in all_polls if not poll.is_currently_active()]
    
    # Get the first active poll for featured display (if any)
    featured_poll = polls[0] if polls and filter_type == 'active' else None
    
    context = {
        'polls': polls,
        'featured_poll': featured_poll,
        'filter_type': filter_type,
    }
    return render(request, 'polls/index.html', context)


def vote(request, poll_id):
    """
    Handles voting on a poll.
    Accepts POST request with selected choice IDs.
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    
    # Check if poll is still active
    if not poll.is_currently_active():
        return redirect('polls:index')
    
    # Handle POST request (when user submits vote)
    if request.method == 'POST':
        # Get selected choice IDs from form
        choice_ids = request.POST.getlist('choice')
        
        if choice_ids:
            # Increment vote count for each selected choice
            for choice_id in choice_ids:
                try:
                    choice = poll.choice_set.get(pk=choice_id)
                    choice.votes += 1
                    choice.save()
                except Choice.DoesNotExist:
                    pass
        
        # Redirect to results page after voting
        return redirect('polls:results', poll_id=poll.id)
    
    # Handle GET request (show voting form)
    return render(request, 'polls/vote.html', {'poll': poll})


def results(request, poll_id):
    """
    Displays the results of a poll with vote counts and percentages.
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {
        'poll': poll,
        'choices': poll.choice_set.all().order_by('-votes'),
    }
    return render(request, 'polls/results.html', context)
