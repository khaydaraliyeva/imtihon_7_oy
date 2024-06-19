from django.contrib import admin
from .models import UserProfile, Category, Product, ProductImage, ProductVideo, Cart, CartProduct, Comment, LikeProduct

# Register UserProfile with additional display options


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'phone', 'address', 'date_of_birth')
    search_fields = ('user__username', 'phone', 'address')
    list_filter = ('status',)


# Register Category with hierarchical display
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)


# Register Brand with additional display options
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# Inline for ProductImage and ProductVideo
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1


# Register Product with inlines for images and videos
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'price', 'stock', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'available')
    inlines = [ProductImageInline, ProductVideoInline]


# Register Cart and CartProduct with additional display options
class CartProductInline(admin.TabularInline):
    model = CartProduct
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    inlines = [CartProductInline]


# Register Comment with additional display options
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'parent', 'content', 'created_at')
    search_fields = ('user__username', 'product__name', 'content')
    list_filter = ('product', 'created_at')


# Register LikeProduct with additional display options
class LikeProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('product', 'created_at')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(LikeProduct, LikeProductAdmin)

