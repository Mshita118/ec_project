from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Product


class ProductViewTests(TestCase):
    def test_add_product_valid(self):
        # シンプルな画像ファイルをモック
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )

        response = self.client.post(reverse('add_product'), {
            'name': 'Test Product',
            'price': 1000,
            'description': 'Test description',
            'image': image
        })

        self.assertRedirects(response, reverse('product_list'))
        self.assertEqual(Product.objects.count(), 1)
        product = Product.objects.first()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 1000)
        self.assertEqual(product.description, 'Test description')

    def test_add_product_invalid(self):
        response = self.client.post(reverse('add_product'), {
            'name': '',
            'price': '100',
            'description': 'Product Description'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']

        self.assertTrue(form.errors['name'])
        self.assertIn('This field is required.', form.errors['name'])

    def test_product_list(self):
        product = Product.objects.create(
            name='Test Product',
            price=1000,
            description='Test description',
            image=None
        )

        response = self.client.get(reverse('product_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Test description')
