from django.urls import path,include
from . import views

urlpatterns = [

 

    path('',views.customer_form, name='customer_insert' ), # get and post req. for insert operation
    path('<int:id>/', views.customer_form, name='customer_update'),
    path('delete/<int:id>/',views.customer_delete,name='customer_delete'),
    path('list/',views.customer_list, name='customer_list') # get req. to retrieve and display all records
]