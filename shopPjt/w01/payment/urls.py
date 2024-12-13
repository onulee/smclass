from django.urls import path,include
from . import views

app_name= 'payment'
urlpatterns = [
    path('kakaopay/', views.kakaopay, name="kakaopay"),
    path('prepare_payment/', views.prepare_payment, name="prepare_payment"),
    path('paySuccess/', views.paySuccess, name='paySuccess'),
    path('payFail/', views.payFail, name="payFail"), 
    path('payCancel/', views.payCancel, name="payCancel"), 
    
]

