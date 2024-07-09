from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('booking', views.booking, name='booking'),
    path('menu', views.menu, name='menu'),
    path('service', views.service, name='service'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('base', views.base, name='base'),
    path('booking', views.booking, name='booking'),
    path('team', views.team, name='team'),
    path('Pages', views.Pages, name='Pages'),
]