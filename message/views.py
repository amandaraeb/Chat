from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from message.forms import ComposeForm
from message.models import Message


def received(request):
    ''' Function that returns all messages that the requesting user has
    received. Used in ajax function in template for displaying all received
    messages. '''

    messages = Message.objects.filter(recipient=request.user)
    return JsonResponse({'messages': list(messages.values())})

def compose(request):
    ''' View function that handles the form for composing a message. '''

    if request.method == 'POST':
        form = ComposeForm(request.POST)
        if form.is_valid():
            current_user = request.user
            recipient_username = request.POST.get('recipient')
            recipient = get_object_or_404(User, username=recipient_username)

            # Create Message object from form fields
            message = Message(recipient=recipient,
                              sender=current_user,
                              message=request.POST.get('message')).save()

    else:
        form = ComposeForm()

    return render(request, 'message/compose.html', {'form': form})
