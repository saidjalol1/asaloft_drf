from rest_framework import serializers
from .models import Discounts, Category, ProductImages, Product, ColorImages, OrderItem, Order

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = ('amount_in_percent', 'start_date', 'end_date')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id', 'image')
        

class ColorImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorImages
        fields = ('id', 'image')
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    discount = DiscountsSerializer()
    images = ProductImagesSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'dimensions', 'frame', 'material', 'paint_type', 'price', 'description', 'category', 'discount', 'images')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        if product.discount:
            discount = product.discount.amount_in_percent
            discounted_price = float(product.price) * (1 - (discount / 100))
        else:
            discounted_price = float(product.price)
        data['amount'] = discounted_price * quantity
        return data
    

    

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'address', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
    
    