from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Product, Cart, CartProduct, Category, LikeProduct, Comment
from app.forms import CommentForm
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.order_by('-created_at')[:8]
    return render(request, 'client/index.html', {'products': products})


@login_required
def add_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
    cart_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'client-index'))


def chackout(request):
    return render(request, 'client/checkout.html')


def shop(request):
    products_list = Product.objects.all()
    categories = Category.objects.filter(parent=None)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'client/shop.html', {
        "products": products,
        "categories": categories,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.product = product
                comment.save()
                return redirect('client/single-product-details.html', pk=product.pk)
        else:
            comment_form = CommentForm()

        return render(request, 'client/single-product-details.html', {
            'product': product,
            'comments': comments,
            'comment_form': comment_form
        })
    else:
        return redirect('user_login')


def filter_by_category(request, pk):
    products_list = Product.objects.filter(category_id=pk)
    categories = Category.objects.filter(parent=None)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'client/shop.html', {"products": products, "categories": categories})


def filter_by_brand(request, pk):
    products_list = Product.objects.filter(brand_id=pk)
    categories = Category.objects.filter(parent=None)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'client/shop.html', {"products": products, "categories": categories})


def filter_by_price(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products_list = Product.objects.all()
    categories = Category.objects.filter(parent=None)

    if min_price and max_price:
        products_list = products_list.filter(price__gte=min_price, price__lte=max_price)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'client/shop.html', {"products": products, "categories": categories})


@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    like, created = LikeProduct.objects.get_or_create(user=request.user, product=product)

    if not created:
        like.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'client-index'))


@login_required
def liked_products(request):
    liked_products = LikeProduct.objects.filter(user=request.user)
    return render(request, 'client/liked_products.html', {'liked_products': liked_products})


def search_products(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(author__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'client/search_results.html', {'products': products, 'query': query})


def contact(request):
    return render(request, 'client/contact.html')


def search_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    subcategories = Category.objects.filter(parent=category)
    products_list = Product.objects.filter(category__in=subcategories)
    categories = Category.objects.filter(parent=None)

    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'client/shop.html', {'products': products, "categories": categories})
