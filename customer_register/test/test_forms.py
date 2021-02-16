from django.test import SimpleTestCase
from customer_register.forms import CustomerForm


class TestForms(simpleTestCase):

    def test_customer_form_valid_data(self):
        from = CustomerForm(data={
               'fullname' : 'Demilson Fayika',       
               'previous_address' : '19 pelham London SW7 2NQ',
               'telephone_number' : 02086817300,
               'area' = 'London'


        })

        self.assertTrue(form.is_valid())


        def test_cusotmer_no_data(self):
            form = CustomerForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors), 3)
