from django.urls import path, include
from .views import *


urlpatterns=[
    path('', home_page, name='home'), 
    path('about', about_page, name='about'),
    path('portfolio', portfolio_page, name='portfolio'),
    #path('blog', blog_page, name='blog'),
    path('contact', contact_page, name='contact'),
    # path('services', service_page, name='services'),
    # path('read_more', read_more, name='readmore')
]