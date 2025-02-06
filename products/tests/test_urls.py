from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import add_product, product_list


class TestUrls(SimpleTestCase):

    def test_add_product_url_resolve(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_product_list_url_resolve(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func, product_list)
