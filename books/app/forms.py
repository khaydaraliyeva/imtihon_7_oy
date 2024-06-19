from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, Category, Product, ProductImage, ProductVideo, Cart, CartProduct, Comment, LikeProduct


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'address', 'phone', 'date_of_birth', 'status']
        widgets = {
            'status': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'parent']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'author', 'name', 'description', 'price', 'stock', 'available']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']


class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['product', 'video']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']


class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cart', 'product', 'quantity']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class LikeProductForm(forms.ModelForm):
    class Meta:
        model = LikeProduct
        fields = ['user', 'product']

