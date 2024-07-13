from django.db import models
from django.contrib.auth.models import User

class Discounts(models.Model):
    amount_in_percent = models.PositiveIntegerField(default=0, verbose_name="chegirma foizi")
    start_date = models.DateField(verbose_name="Boshlanish sana")
    end_date = models.DateField(verbose_name="Tugash sana")
    
    class Meta:
        verbose_name = "Chegirma"
        verbose_name_plural = "Chegirmalar"
        
    def __str__(self):
        return str(self.start_date  + "-" + self.end_date + "-" + self.amount_in_percent + "%")


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    
    class Meta:
        verbose_name = "Mahsulot Kategoriyasi"
        verbose_name_plural = "Mahsulot Kategoriyalari"
    
    def __str__(self):
        return self.name
    

    

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="nomi")
    dimensions = models.CharField(max_length=100, verbose_name="o'lchamlari")
    frame = models.CharField(max_length=100, verbose_name="ramkasi")
    material = models.CharField(max_length=200, verbose_name="Materiali")
    paint_type = models.CharField(max_length=250, verbose_name="Bo'yoq turi")
    price = models.CharField(max_length=200, verbose_name="narxi")
    description = models.TextField(max_length=200, verbose_name="tavsifi")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_items", verbose_name="Kategoriyasi")
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, related_name="discount_items", verbose_name="Chegirmasi",blank=True, null=True,)
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
    
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    image = models.ImageField(verbose_name="Mahsulot rasmi", upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Mahsulot")
    class Meta:
        verbose_name = "Mahsulot rasmlari"
        verbose_name_plural ="Mahsulot Rasmi"
        
    def __str__(self):
        return self.product.name + "-" + str(self.product.id)    


class ColorImages(models.Model):
    image = models.ImageField(upload_to="color_images/")
    class Meta:
        verbose_name = "Rang rasmi"
        verbose_name_plural ="Rang rasmlari"
        
    def __str__(self):
        return self.image.name
    
class Order(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        
        
    def __str__(self):
        return self.full_name
    

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    
    
    color = models.ForeignKey(ColorImages, on_delete=models.CASCADE, related_name="item", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name= "items")
    
    
    def __str__(self):
        return self.product.name
    

class ChatId(models.Model):
    chat_id = models.CharField(max_length=250)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="chat_ids", blank=True, null=True)
    
    class Meta:
        verbose_name = "ChatId"
        verbose_name_plural = "ChatId"
        
    def __str__(self):
        return self.chat_id + "-" + self.owner.username
    