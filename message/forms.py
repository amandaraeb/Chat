from django import forms

class ComposeForm(forms.Form):
    ''' Django form for composing messages. '''

    recipient = forms.CharField(label='recipient', max_length=30)
    message = forms.CharField(label='message', max_length=100)
