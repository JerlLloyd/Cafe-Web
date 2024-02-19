import datetime
from django.db import models
import os

from django.contrib.auth.models import User

def get_file_path(request, filename):
    file_name = filename
    time = datetime.datetime.now().strftime('%y%m%d%H%M:%S')
    filename = "%s%s" % (time, file_name)
    return os.path.join("upload/", filename)



class Category(models.Model):
    sid = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default-1=hidden" )
    trending = models.BooleanField(default=False, help_text="0=default-1=trending" )
    m_title = models.CharField(max_length=150, null=False, blank=False)
    m_keyword = models.CharField(max_length=150, null=False, blank=False)
    m_description = models.TextField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    sid = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    p_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    s_description = models.TextField(max_length=250, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    qty =  models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    s_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="0=default-1=hidden" )
    trending = models.BooleanField(default=False, help_text="0=default-1=trending" )
    tag = models.CharField(max_length=150, null=False, blank=False)
    m_title = models.CharField(max_length=150, null=False, blank=False)
    m_keyword = models.CharField(max_length=150, null=False, blank=False)
    m_description = models.TextField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=150, null=False)
    Lname = models.CharField(max_length=150, null=False)
    Email = models.CharField(max_length=150, null=False)
    Contact = models.CharField(max_length=150, null=False)
    Address = models.CharField(max_length=150, null=False)
    Address = models.TextField(null=False)
    Baranggay = models.CharField(max_length=150, null=False)
    City = models.CharField(max_length=150, null=False)
    Pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=False)
    orderstatus = (
        ('Pending','Pending'),
        ('To Shipped', 'To Shipped'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatus,  default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    

      
    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=50,null=False)
    Address = models.TextField(null=False)
    Baranggay = models.CharField(max_length=150, null=False)
    City = models.CharField(max_length=150, null=False)
    Pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
    
    
    
    
    
    
    