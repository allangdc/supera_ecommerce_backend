from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Wishlist(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_price = models.FloatField()
    purchase_date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "user: {}; shipping: {}; status: {}".format(self.id_user, 
                                                            self.shipping_price,
                                                            self.status)
