from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.template import loader
from . import forms, models

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def add_event(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        form.save()
        return render(request, 'event/done.html')
    else:
        form = forms.EventForm()
    return render(request, 'event/add_event.html', {'form': form})


def ticket_sale(request):
    if request.method == 'POST':
        form = forms.TicketForm(request.POST)

        if form.is_valid():

            event_title = form.cleaned_data.get('event')
            attendee_name = form.cleaned_data.get('name')
            attendee_email = form.cleaned_data.get('email')
            
            event = models.Event.objects.get(title = event_title)
            models.TicketSale.objects.create(event = event,  name = attendee_name, email = attendee_email)
            send_mail("Your Invitation", f"Hey there! you have been invited to {event.title}", "reyhanehneysidelphi@gmail.com", [attendee_email])

            return render(request, 'event/done.html')
    else:
        form = forms.TicketForm()
    return render(request, 'event/ticket_sale.html', {'form': form})


def manage_attendees(request, event_id):

    event = models.Event.objects.get(id = event_id)

    if request.method == 'POST':
        form = forms.ManageAttendeesForm(request.POST)

        
        manage = form.save(commit=False)
        manage.event = event
        manage.save()

        
        attendees = models.TicketSale.objects.all()

        for attendee in attendees :
            send_mail(f'Invitation For {event.title}', manage.message , 'reyhanehneysidelphi@gmail.com', [attendee.email])
            
        return render(request,'event/done.html')
        
    else:
        form = forms.ManageAttendeesForm()
    return render(request, 'event/manage_attendees.html', {'form':form, 'event':event})


def managers_planner(request, event_id):

    event = models.Event.objects.get(id = event_id)

    if request.method == 'POST':
        form = forms.ManagersPlannerForm(request.POST)

        planner = form.save(commit=False)
        planner.event = event
        planner.save()

        send_mail("Your Event's To Do List", planner.to_do_list, 'reyhanehneysidelphi@gmail.com', [event.organizer_email])
        
        return render(request, 'event/done.html')
    
    else:
        form = forms.ManagersPlannerForm()
    return render(request, 'event/managers_planner.html', {'form':form, 'event':event})