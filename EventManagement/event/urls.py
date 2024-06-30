from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('add_event/', views.add_event, name='add-event'),
    path('ticket_sale/', views.ticket_sale, name='ticket-sale'),
    path('manage_attendees/<int:event_id>/', views.manage_attendees, name='manage-attendees'),
    path('managers_planner/<int:event_id>/', views.managers_planner, name='managers-planner')
]