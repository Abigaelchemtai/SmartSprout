from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name, self.email, self.subject, self.message

class Orders(models.Model):
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=255)
    price = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=500)


    def __str__(self):
        return self.name, self.product, self.phone, self.message, self.price

