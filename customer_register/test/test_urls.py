from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer_register.urls import customer_list, customer_insert, customer_update, customer_delete

class TestUrls(SimpleTestCase):

    def test_list_is_resolves(self):
         url = reverse('list')
         print(resolve(url))
         self.assertEqual(resolve(url).func, customer_list)

    def test_add_url_resolves(self):
         url = reverse('add')
         print(resolve(url))
         self.assertEqual(resolve(url).func, customer_insert)

    def test_detail_url_resolved(self):
         url = reverse('detail')
         print(resolve(url))
         self.assertEqual(resolve(url).func, customer_update)

    def test_delete_url_resolved(self):
         url = reverse('delete')
         print(resolve(url))
         self.assertEqual(resolve(url).func, customer_delete)

