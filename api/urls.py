from django.urls import path
from api import views 
urlpatterns = [  
    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),           
               
    #path('customers/',ListCustomersView.as_view(), name="customers-all"),
    #path('auth/login/', LoginView.as_view(), name="auth-login"),
    #path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
    #path('',views.index,name='index'),
    #path('about',views.about,name='about'),
    #path('detail',views.about,name='detail'),
    #path('search',views.search,name="search")
]