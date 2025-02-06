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
        print(response.status_code)
        print(response.content)

        self.assertRedirects(response, reverse('product_list'))
