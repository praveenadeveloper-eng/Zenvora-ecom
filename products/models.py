from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug= models.SlugField(unique=True,max_length=100)
    description=models.CharField(max_length=225)
    category_image=models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('products:product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name         = models.CharField(max_length=200,unique=True)
    slug         = models.SlugField(max_length=200,unique=True)
    description  = models.TextField(max_length=500,blank=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('products:product_detail_page',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name