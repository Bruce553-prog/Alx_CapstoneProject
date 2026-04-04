from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

# In  a case where we delete a category then it will follow that the prouct is equally deleted 
# However, when we delete the product we do not automatically delete the category even if all the category is deleted, for further addition
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category =models.CharField
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name

class Product (models.Model):
    name =models.Charfield 
    description = models.CharField
    price =models.TextField
    stock =models.PositiveInterger(default =0)




    