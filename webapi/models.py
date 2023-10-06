from django.db import models


class TypeOffFood(models.Model):
    title = models.TextField(default="")

    def __str__(self):
        return self.title
    

# class SpecialFunction(models.Model):
#     title = models.TextField()
#     description = models.TextField()
#     price = models.IntegerField()

#     def __str__(self):
#         return self.title
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)
    carbohydrates = models.CharField(max_length=100)
    proteins = models.CharField(max_length=100)
    fats = models.CharField(max_length=100)
    recipe = models.TextField(default="")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    type = models.ForeignKey(TypeOffFood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Dishes'

class OrderDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.dish.name
    
    class Meta:
        ordering = ['dish']
        verbose_name_plural = 'Order Dishes'

class Order(models.Model):
    dishes = models.ManyToManyField(OrderDish)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Orders'

# class Menu(models.Model):
#     title = models.TextField()
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
#     special_function = models.ForeignKey(SpecialFunction, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    

# class Special_menu_for_children(models.Model):
#     title = models.TextField()
#     description = models.TextField()
#     price = models.IntegerField()
#     calories = models.IntegerField(default=0)
#     carbohydrates = models.IntegerField(default=0)
#     proteins = models.IntegerField(default=0)
#     fats = models.IntegerField(default=0)
#     recipe = models.TextField(default="")
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     type = models.ForeignKey(TypeOffFood, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['title']
#         verbose_name_plural = 'Menu for children'




    # clasS = models.ForeignKey(Class, on_delete=models.CASCADE)