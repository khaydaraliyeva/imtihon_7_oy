from django.shortcuts import render, get_object_or_404, redirect
from app.models import UserProfile, Category, Product, ProductImage, ProductVideo, Cart, CartProduct, Comment, LikeProduct
from app.forms import UserProfileForm, CategoryForm, ProductForm, ProductImageForm, ProductVideoForm, CartForm, CartProductForm, CommentForm, LikeProductForm


def check_status(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.status.lower() == 'admin':
        return True
    else:
        return False


def index(request):
    if check_status(request):
        return render(request, 'admin1/base.html')
    return render(request, 'admin1/error.html')


def dashboard(request):
    if check_status(request):
        user_profile = UserProfile.objects.all()
        category = Category.objects.all()
        product = Product.objects.all()
        product_image = ProductImage.objects.all()
        product_video = ProductVideo.objects.all()
        cart = Cart.objects.all()
        cart_product = CartProduct.objects.all()
        comment = Comment.objects.all()
        like_product = LikeProduct.objects.all()

        context = {
            'user_profile': user_profile,
            'category': category,
            'product': product,
            'product_image': product_image,
            'product_video': product_video,
            'cart': cart,
            'cart_product': cart_product,
            'comment': comment,
            'like_product': like_product,
            }
        return render(request, 'admin1/dashboard.html', context=context)
    return render(request, 'admin1/error.html')


# UserProfile CRUD
def create_user_profile(request):
    if check_status(request):
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-user_profile_list')
        else:
            form = UserProfileForm()
        return render(request, 'admin1/user_profile_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def user_profile_list(request):
    if check_status(request):
        profiles = UserProfile.objects.all()
        return render(request, 'admin1/user_profile_list.html', {'profiles': profiles})
    return render(request, 'admin1/error.html')


def user_profile_detail(request, pk):
    if check_status(request):
        profile = get_object_or_404(UserProfile, pk=pk)
        return render(request, 'admin1/user_profile_detail.html', {'profile': profile})
    return render(request, 'admin1/error.html')


def update_user_profile(request, pk):
    if check_status(request):
        profile = get_object_or_404(UserProfile, pk=pk)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('admin-user_profile_detail', pk=profile.pk)
        else:
            form = UserProfileForm(instance=profile)
        return render(request, 'admin1/user_profile_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_user_profile(request, pk):
    if check_status(request):
        profile = get_object_or_404(UserProfile, pk=pk)
        if request.method == 'POST':
            profile.delete()
            return redirect('admin-user_profile_list')
        return render(request, 'admin1/user_profile_confirm_delete.html', {'profile': profile})
    return render(request, 'admin1/error.html')


# Category CRUD
def create_category(request):
    if check_status(request):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin-category_list')
        else:
            form = CategoryForm()
        return render(request, 'admin1/category_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def category_list(request):
    if check_status(request):
        categories = Category.objects.all()
        return render(request, 'admin1/category_list.html', {'categories': categories})
    return render(request, 'admin1/error.html')


def category_detail(request, pk):
    if check_status(request):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'admin1/category_detail.html', {'category': category})
    return render(request, 'admin1/error.html')


def update_category(request, pk):
    if check_status(request):
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('admin-category_detail', pk=category.pk)
        else:
            form = CategoryForm(instance=category)
        return render(request, 'admin1/category_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_category(request, pk):
    if check_status(request):
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            category.delete()
            return redirect('admin-category_list')
        return render(request, 'admin1/category_confirm_delete.html', {'category': category})
    return render(request, 'admin1/error.html')


# Product CRUD
def create_product(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return redirect('admin-product_list')
        else:
            form = ProductForm()
        return render(request, 'admin1/product_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def product_list(request):
    if check_status(request):
        products = Product.objects.all()
        return render(request, 'admin1/product_list.html', {'products': products})
    return render(request, 'admin1/error.html')


def product_detail(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'admin1/product_detail.html', {'product': product})
    return render(request, 'admin1/error.html')


def update_product(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('admin-product_detail', pk=product.pk)
        else:
            form = ProductForm(instance=product)
        return render(request, 'admin1/product_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_product(request, pk):
    if check_status(request):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('admin-product_list')
        return render(request, 'admin1/product_confirm_delete.html', {'product': product})
    return render(request, 'admin1/error.html')


# ProductImage CRUD
def create_product_image(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-product_image_list')
        else:
            form = ProductImageForm()
        return render(request, 'admin1/product_image_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def product_image_list(request):
    if check_status(request):
        images = ProductImage.objects.all()
        return render(request, 'admin1/product_image_list.html', {'images': images})


def product_image_detail(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        return render(request, 'admin1/product_image_detail.html', {'image': image})
    return render(request, 'admin1/error.html')


def update_product_image(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        if request.method == 'POST':
            form = ProductImageForm(request.POST, request.FILES, instance=image)
            if form.is_valid():
                form.save()
                return redirect('admin-product_image_detail', pk=image.pk)
        else:
            form = ProductImageForm(instance=image)
        return render(request, 'admin1/product_image_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_product_image(request, pk):
    if check_status(request):
        image = get_object_or_404(ProductImage, pk=pk)
        if request.method == 'POST':
            image.delete()
            return redirect('admin-product_image_list')
        return render(request, 'admin1/product_image_confirm_delete.html', {'image': image})
    return render(request, 'admin1/error.html')


# ProductVideo CRUD
def create_product_video(request):
    if check_status(request):
        if request.method == 'POST':
            form = ProductVideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-product_video_list')
        else:
            form = ProductVideoForm()
        return render(request, 'admin1/product_video_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def product_video_list(request):
    if check_status(request):
        videos = ProductVideo.objects.all()
        return render(request, 'admin1/product_video_list.html', {'videos': videos})
    return render(request, 'admin1/error.html')


def product_video_detail(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        return render(request, 'admin1/product_video_detail.html', {'video': video})
    return render(request, 'admin1/error.html')


def update_product_video(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        if request.method == 'POST':
            form = ProductVideoForm(request.POST, request.FILES, instance=video)
            if form.is_valid():
                form.save()
                return redirect('admin-product_video_detail', pk=video.pk)
        else:
            form = ProductVideoForm(instance=video)
        return render(request, 'admin1/product_video_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_product_video(request, pk):
    if check_status(request):
        video = get_object_or_404(ProductVideo, pk=pk)
        if request.method == 'POST':
            video.delete()
            return redirect('admin-product_video_list')
        return render(request, 'admin1/product_video_confirm_delete.html', {'video': video})
    return render(request, 'admin1/error.html')


# Cart CRUD
def create_cart(request):
    if check_status(request):
        if request.method == 'POST':
            form = CartForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin-cart_list')
        else:
            form = CartForm()
        return render(request, 'admin1/cart_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def cart_list(request):
    if check_status(request):
        carts = Cart.objects.all()
        return render(request, 'admin1/cart_list.html', {'carts': carts})
    return render(request, 'admin1/error.html')


def cart_detail(request, pk):
    if check_status(request):
        cart = get_object_or_404(Cart, pk=pk)
        return render(request, 'admin1/cart_detail.html', {'cart': cart})
    return render(request, 'admin1/error.html')


def update_cart(request, pk):
    if check_status(request):
        cart = get_object_or_404(Cart, pk=pk)
        if request.method == 'POST':
            form = CartForm(request.POST, instance=cart)
            if form.is_valid():
                form.save()
                return redirect('admin-cart_detail', pk=cart.pk)
        else:
            form = CartForm(instance=cart)
        return render(request, 'admin1/cart_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_cart(request, pk):
    if check_status(request):
        cart = get_object_or_404(Cart, pk=pk)
        if request.method == 'POST':
            cart.delete()
            return redirect('admin-cart_list')
        return render(request, 'admin1/cart_confirm_delete.html', {'cart': cart})
    return render(request, 'admin1/error.html')


# CartProduct CRUD
def create_cart_product(request):
    if check_status(request):
        if request.method == 'POST':
            form = CartProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin-cart_product_list')
        else:
            form = CartProductForm()
        return render(request, 'admin1/cart_product_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def cart_product_list(request):
    if check_status(request):
        cart_products = CartProduct.objects.all()
        return render(request, 'admin1/cart_product_list.html', {'cart_products': cart_products})
    return render(request, 'admin1/error.html')


def cart_product_detail(request, pk):
    if check_status(request):
        cart_product = get_object_or_404(CartProduct, pk=pk)
        return render(request, 'admin1/cart_product_detail.html', {'cart_product': cart_product})
    return render(request, 'admin1/error.html')


def update_cart_product(request, pk):
    if check_status(request):
        cart_product = get_object_or_404(CartProduct, pk=pk)
        if request.method == 'POST':
            form = CartProductForm(request.POST, instance=cart_product)
            if form.is_valid():
                form.save()
                return redirect('admin-cart_product_detail', pk=cart_product.pk)
        else:
            form = CartProductForm(instance=cart_product)
        return render(request, 'admin1/cart_product_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_cart_product(request, pk):
    if check_status(request):
        cart_product = get_object_or_404(CartProduct, pk=pk)
        if request.method == 'POST':
            cart_product.delete()
            return redirect('admin-cart_product_list')
        return render(request, 'admin1/cart_product_confirm_delete.html', {'cart_product': cart_product})
    return render(request, 'admin1/error.html')


# Comment CRUD
def create_comment(request):
    if check_status(request):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin-comment_list')
        else:
            form = CommentForm()
        return render(request, 'admin1/comment_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def comment_list(request):
    if check_status(request):
        comments = Comment.objects.all()
        return render(request, 'admin1/comment_list.html', {'comments': comments})


def comment_detail(request, pk):
    if check_status(request):
        comment = get_object_or_404(Comment, pk=pk)
        return render(request, 'admin1/comment_detail.html', {'comment': comment})
    return render(request, 'admin1/error.html')


def update_comment(request, pk):
    if check_status(request):
        comment = get_object_or_404(Comment, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('admin-comment_detail', pk=comment.pk)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'admin1/comment_form.html', {'form': form})
    return render(request, 'admin1/error.html')


def delete_comment(request, pk):
    if check_status(request):
        comment = get_object_or_404(Comment, pk=pk)
        if request.method == 'POST':
            comment.delete()
            return redirect('admin-comment_list')
        return render(request, 'admin1/comment_confirm_delete.html', {'comment': comment})
    return render(request, 'admin1/error.html')
