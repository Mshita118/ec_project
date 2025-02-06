from django.test import TestCase, Client
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse('product_list')
        self.add_product_url = reverse('add_product')

        # テスト用の画像を作成
        self.image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )

        # テスト用のプロダクトを作成
        self.product = Product.objects.create(
            name="Test Product",
            price=1000,
            image=self.image
        )

    def test_product_list_view(self):
        """ product_listビューの動作確認 """
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertContains(response, "Test Product")

    def test_add_product_view_get(self):
        """ add_productビューのGETリクエスト確認 """
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_add_product_view_post(self):
        """ add_productビューのPOSTリクエスト確認 """
        post_data = {
            "name": "New Product",
            "price": 2000,
        }
        file_data = {
            "image": SimpleUploadedFile("new_image.jpg", b"new_content", content_type="image/jpeg")
        }
        response = self.client.post(
            self.add_product_url, data=post_data, files=file_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name="New Product").exists())
        self.assertRedirects(response, self.product_list_url)
