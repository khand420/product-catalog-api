# products/views.py

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from .tasks import update_product_inventory  # Import Celery task

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']

    # Custom action to handle inventory update asynchronously
    @action(detail=True, methods=['post'], url_path='update-inventory')
    def update_inventory(self, request, pk=None):
        product = self.get_object()
        inventory_count = request.data.get('inventory_count')

        if not inventory_count:
            return Response({"error": "inventory_count is required"}, status=400)

        # Call Celery task to update inventory
        update_product_inventory.delay(product.id, inventory_count)

        return Response({
            "message": f"Inventory update for product {product.name} is in progress!"
        })



# from rest_framework import viewsets, filters
# from .models import Product
# from .serializers import ProductSerializer

# # class ProductViewSet(viewsets.ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', 'description', 'category__name']