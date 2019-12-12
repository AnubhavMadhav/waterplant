from django.urls import path, include
from .views import ListCustomersView
urlpatterns = [  
    path('customers/',ListCustomersView.as_view(), name="customers-all")
    #path('',views.index,name='index'),
    #path('about',views.about,name='about'),
    #path('detail',views.about,name='detail'),
    #path('search',views.search,name="search")
]