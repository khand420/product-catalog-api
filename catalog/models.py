from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory_count = models.IntegerField()
#     category = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name



class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sales_count = models.IntegerField(default=0)  # To calculate popularity

    @property
    def popularity_score(self):
        return self.sales_count  # You can further calculate this
