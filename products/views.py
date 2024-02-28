from django.shortcuts import render, HttpResponse, redirect
from products.models import Product, Rate
# Create your views here.

def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(
        request,
        template_name="products_dj/product_list.html",
        context=context
    )


def get_product_by_id(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
        "ratings": product.ratings.all()
    }
    return render(
        request,
        template_name="products_dj/product_page.html",
        context=context
    )

def product_review(request, product_id):
    if request.method == "POST":
        review_product = product_id
        review_author = request.POST.get("review-author")
        review_text = request.POST.get("review-text")
        try:
            review_rate = request.POST.get("review-rate")
        except:
            return HttpResponse(
                "Wrong value for rate! Please try enter value as the example: 5.0",
                status=404
            )
        
        rate = Rate.objects.create(
            product=Product.objects.get(id=review_product),
            author=review_author,
            text=review_text,
            rating = review_rate
        )

        return redirect("product-page", product_id=product_id)
    else:
        products = Product.objects.all()
        context = {
            "products": products
        }
        return render(request, template_name="products_dj/product_page.html",)
