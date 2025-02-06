from django.test import TestCase
from products.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=1999.99,
            image=SimpleUploadedFile(
                "test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "This is a test product.")
        self.assertEqual(self.product.price, 1999.99)
        self.assertTrue(self.product.image)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_product_auto_timestamps(self):
        self.assertIsNotNone(self.product.created_at)
        self.assertIsNotNone(self.product.updated_at)
