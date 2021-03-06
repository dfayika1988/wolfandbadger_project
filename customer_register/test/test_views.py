from django.template.defaultfilters import title
from django.test import TestCase, Client
from django.urls import reverse
from wolfandbanger_project.customer_register import customer_list, customer_insert, customer_update, customer_delete
import json

class TestViews(TestCase):

    def setUP(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['demilsonfayika'])
        self.project1 = Project.objects.create(
            name='DemilsonFayika',
            area='London"
        )

    def test_customer_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_register/customer_list.html')

    def test_customer_detail_get(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_register/customer_list.html')

    def test_customer_detail_Post_add_new(self):
        Category.objects.create(
            customer=self.customer1,
             fullname = 'Demilson Fayika'

        )

        response = self.client.post(self.detail_url, {
               'fullname' : 'Demilson Fayika',
               'previous_address' : '19 pelham London SW7 2NQ',
               'telephone_number' : 02086817300,
                'area' = 'London'

        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.customer1.Customer.first().name, 'Demilson Fayika')

    def test_project_detail_Post_no_data(self):
        response = self.client.post(self.detail_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project1.expenses.count(), 0)

    def test_customer_detail_DELETE_delete(self):
        category1 = Category.create(
            customer=self.customer1,
            name='Demilson'

        )
        Customer.objects.create(
            customer=self.customer1,
           'previous_address' : '19 pelham London SW7 2NQ',
           'telephone_number' : 02086817300
            category=category1

        )
        response = self.customer.delete(self.detail_url, json.dumps({
            'id': 1
        }))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.customer.Customr1.count(), 0)

    def test_customer_detail_DELETE_no_id(self):
        category1 = Category.create(
            customer=self.customer1,
            'fullname : 'Demilson Fayika'

        )
        Customer.objects.create(
            customer=self.customer1,
            title='Demilson Fayika',
             previous_address = '19 pelham London SW7 2NQ',
             telephone_number = 02086817300,
             position = 'London'

        )
        response = self.client.delete(self.detail_url, json.dumps)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(self.customer1.Customer.count(), 0)


    def test_customer_create_POST(self):
        url =reverse('add')
        response =self.client.post(url,{
             'fullname': 'Demilson Fayika',
              'area' = 'London'

        })

