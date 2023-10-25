from django.contrib import admin

from ser.models import Product, Rating, Comment, Category, News


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Rating)
class PostAdmin(admin.ModelAdmin):
    list_display = ("rating", "product",)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ("message", "product",)


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ("header", "lan", "message",)
