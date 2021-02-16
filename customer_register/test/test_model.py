from django.test import TestCase 
from customer_register.models import fullname,  previous_address, telephone_number, position


def setUp(self):
    seft.Customer1 = Customer.objects.create(
        'fullname' : 'Demilson Fayika',
         'previous_address' : '19 pelham London SW7 2NQ',
          'telephone_number' : 02086817300,
          'area' = 'London'
    )


def test_customer_is_assinged_on_creation(self):
    self.assertEquals(self.customer1.slug, 'Customer-1')
