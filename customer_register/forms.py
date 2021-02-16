from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class  Meta:
        model = Customer
        fields = ('fullname','previous_address','telephone_number','area')
        labels = {
            'fullname':'Full Name'
        
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm,self).__init__(*args, **kwargs)
        self.fields['area'].empty_label = "Select"
     
        
