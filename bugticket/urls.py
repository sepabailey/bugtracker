from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginview, name='login_url'),
    path('logout/', views.logoutview, name='logout_url'),
    path('signup/', views.adduser, name='signup'),
    path('ticket_detail/<int:id>', views.ticket_detail, name='ticket_detail'),
    path('ticketform/<int:user_id>', views.create_ticket, name='new_ticket_form'),
    path('in_progress/edit/<int:ticket_id>',
         views.inprogress_ticket, name='in_progress'),
    path('complete/edit/<int:ticket_id>',
         views.complete_ticket, name='complete_progress'),
    path('invalid/edit/<int:ticket_id>',
         views.invalid_ticket, name='invalid_progress'),
    path('edit_ticket/edit/<int:ticket_id>', views.edit_ticket, name='edit'),
    path('user_detail/<int:user_id>',
         views.user_detail, name='user_detail'),
]
