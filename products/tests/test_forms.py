from django.test import TestCase
from products.forms import ProductForm
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image


class ProductFormTest(TestCase):

    def generate_image_file(self):
        img = Image.new("RGB", (100, 100), color=(255, 0, 0))
        img_io = io.BytesIO()
        img.save(img_io, format="PNG")
        img_io.seek(0)
        return SimpleUploadedFile("test_image.png", img_io.getvalue(), content_type="image/png")

    def test_product_form_valid(self):
        """ フォームのバリデーションが正しく動作するか確認 """
        form_data = {
            "name": "Test Product",
            "description": "This is a test description.",
            "price": 1999.99,
        }
        file_data = {
            "image": self.generate_image_file(),
        }
        form = ProductForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_product_form_name_invalid(self):
        form_data = {
            "name": " ",
            "description": "This is a test description",
            "price": 1999.99,
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_product_form_price_invalid(self):
        form_data = {
            "name": "Test Product",
            "description": "This is a test description",
            "price": "invalid_price",
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)
