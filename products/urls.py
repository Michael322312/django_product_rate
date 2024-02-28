from django.urls import path
from products import views

urlpatterns = [
    path("", views.products_list, name = "products"),
    path("product/<int:product_id>", views.get_product_by_id, name = "product-page"),
    path("rating/<int:product_id>", views.product_review, name = "product-review" )
]