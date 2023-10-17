from django.urls import path
from .views import Login,Registration,Logout,MovieList,DetailView,Booking,Ticket


urlpatterns = [
    path ('', Login, name = 'login'),
    path ('register/', Registration, name= 'Register'),
    path ('logout/', Logout, name='logout'),
    path ('list/', MovieList, name = 'list'),
    path ('detail_view/<int:id>', DetailView, name = 'detail'),
    path ('booking/', Booking, name = 'booking'),
    path ('ticket/<str:user>', Ticket, name= 'ticket'),

]