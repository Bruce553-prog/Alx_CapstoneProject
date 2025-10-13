from django.contrib import admin
from .models import Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  
    readonly_fields = ("product", "quantity")  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username", "id")
    inlines = [OrderItemInline]  
    readonly_fields = ("created_at",)

    
    def total_price(self, obj):
        return f"${obj.get_total_price():.2f}"
    total_price.short_description = "Total Price"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    search_fields = ("order__id", "product__name")
