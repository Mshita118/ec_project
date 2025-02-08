from django.db import models
from django.contrib.auth.models import User
from products.models import Product

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8cb713d (カートモデルの作成)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
<<<<<<< HEAD
=======
>>>>>>> 49d6e58 (productの実装)
=======
>>>>>>> 8cb713d (カートモデルの作成)
