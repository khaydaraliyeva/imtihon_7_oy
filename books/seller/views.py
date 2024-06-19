from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product, ProductImage, ProductVideo, UserProfile
from app.forms import ProductVideoForm
from .forms import ProductImageForm, ProductForm

# Create your views here.


def check_status(request):
    user = UserProfile.objects.get(user=request.user)
    if user.status == 'seller':
        return True
    else:
        return False


def index(request):
    if check_status(request):
        return render(request, 'seller/base.html')
    return render(request, 'seller/error.html')


def create_product(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('seller-product_list')
        else:
            form = ProductForm()
        return render(request, 'seller/product_form.html', {'form': form})


def product_list(request):
    if check_status(request):
        products = Product.objects.filter(user=request.user)
        return render(request, 'seller/product_list.html', {'products': products})


def product_detail(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'seller/product_detail.html', {'product': product})


def update_product(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('seller-product_detail', pk=product.pk)
        else:
            form = ProductForm(instance=product)
        return render(request, 'seller/product_form.html', {'form': form})


def delete_product(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('pseller-roduct_list')
        return render(request, 'seller/product_confirm_delete.html', {'product': product})


# ProductImage CRUD
def create_product_image(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('seller-product_image_list')
        else:
            form = ProductImageForm()
        return render(request, 'seller/product_image_form.html', {'form': form})


def product_image_list(request):
    if check_status(request):
        images = ProductImage.objects.filter(product__user=request.user)
        return render(request, 'seller/product_image_list.html', {'images': images})


def product_image_detail(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        return render(request, 'seller/product_image_detail.html', {'image': image})


def update_product_image(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        if request.method == 'POST':
            form = ProductImageForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                form.save()
                return redirect('seller-product_image_detail', pk=image.pk)
        else:
            form = ProductImageForm(instance=image)
        return render(request, 'seller/product_image_form.html', {'form': form})


def delete_product_image(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        if request.method == 'POST':
            image.delete()
            return redirect('seller-product_image_list')
        return render(request, 'seller/product_image_confirm_delete.html', {'image': image})


# ProductVideo CRUD
def create_product_video(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductVideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('seller-roduct_video_list')
        else:
            form = ProductVideoForm()
        return render(request, 'seller/product_video_form.html', {'form': form})


def product_video_list(request):
    if check_status(request):
        videos = ProductVideo.objects.all()
        return render(request, 'seller/product_video_list.html', {'videos': videos})


def product_video_detail(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        return render(request, 'seller/product_video_detail.html', {'video': video})


def update_product_video(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        if request.method == 'POST':
            form = ProductVideoForm(request.POST, request.FILES, instance=video)
            if form.is_valid():
                form.save()
                return redirect('seller-product_video_detail', pk=video.pk)
        else:
            form = ProductVideoForm(instance=video)
        return render(request, 'seller/product_video_form.html', {'form': form})


def delete_product_video(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        if request.method == 'POST':
            video.delete()
            return redirect('pseller-roduct_video_list')
        return render(request, 'seller/product_video_confirm_delete.html', {'video': video})
