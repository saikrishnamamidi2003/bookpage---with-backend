# from django.db import models

# from datetime import datetime
# Create your models here.


# class Useradd(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=250)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username
    

# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     message = models.TextField()
#     is_resolved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name



from django.db import models

class Useradd(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

from django.contrib.auth.models import User

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.user.username} - {self.product.name} ({self.quantity})"
    


class Product(models.Model):
    title = models.CharField(max_length=200, default='Unknown Title')
    author = models.CharField(max_length=100, default='Unknown Author')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default='No description available')
    image = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title

