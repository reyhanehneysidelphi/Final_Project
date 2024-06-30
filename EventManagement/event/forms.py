from django import forms
from . import models

class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title', 'description', 'location', 'date', 'organizer_email']

class TicketForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=models.Event.objects.all())
    class Meta:
        model = models.TicketSale
        fields = ['name','email','event']

class ManageAttendeesForm(forms.ModelForm):
    class Meta:
        model = models.ManageAttendees
        fields = ['message']


class ManagersPlannerForm(forms.ModelForm):
    class Meta:
        model = models.ManagersPlanner
        fields = ['to_do_list']