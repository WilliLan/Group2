from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return(self.name)
    
    # Changes name to categories instead of categorys
    class Meta:
        verbose_name_plural = 'categories'

class Profile(models.Model):
    ACCOUNT_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default='', blank=True)
    address1 = models.CharField(max_length=100, default='', blank=True)
    address2 = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)
    zipcode = models.CharField(max_length=10, default='', blank=True)
    old_cart= models.CharField(max_length=200, blank=True, null=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)
    approved = models.BooleanField(default=True)


    def __str__(self):
        account_type = f"{self.account_type}" if self.account_type else "admin"
        return f'{self.user.username} - {account_type}'
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)
        

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.CharField(max_length=1000, default='', blank=False)
    image = CloudinaryField('image')
    # On Sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
     # Seller
     # related_name='products': Adds a reverse relationship, allowing access all products of a seller with user.products.all().
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products') 



    def __str__(self):
        return self.name

