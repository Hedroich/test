from rest_framework import serializers
from .models import Product, Rating, Comment, Category, News
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"]


class RatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Rating
        fields = ["id", "rating"]




class CommentSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Comment
        fields = ["id", "message"]


class RatingCommentSerializer(serializers.Serializer):
    product_rating = serializers.FloatField()
    product_comments = serializers.CharField(max_length=500)

    def get_product_info(self, product_id):
        product = Product.objects.filter(id=product_id)
        rating = Rating.objects.filter(product=product)
        comments = Comment.objects.filter(product=product)
        result = f"{product.name}: рэйтинг = {rating}, комментарии: {comments}"
        return result


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

# class NewsSerializer(serializers.Serializer):
#     header = serializers.CharField(max_length=256)
#     lan = serializers.CharField(max_length=5)
#     message = serializers.CharField()
#     publication_data = serializers.DateField()

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "header", "lan", "message",)

