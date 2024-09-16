from celery import shared_task
from .models import Product

# @shared_task
# def update_inventory(product_id, count):
#     product = Product.objects.get(id=product_id)
#     product.inventory_count = count
#     product.save()
#     return product.inventory_count




@shared_task
def update_product_inventory(product_id, inventory_count):
    try:
        product = Product.objects.get(id=product_id)
        product.inventory_count = inventory_count
        product.save()
        return f"Product {product.name} inventory updated to {inventory_count}"
    except Product.DoesNotExist:
        return f"Product with id {product_id} does not exist."

