from django.db import models
NAME_CHOICES = ( 
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5"),
	("6", "6"),
	("7", "7"),
	("8", "8"),
	)

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100, choices=NAME_CHOICES, default='null')

class Expenses(models.Model):
	cateogry = models.ForeignKey(Category, on_delete=models.CASCADE)
	date = models.DateField(null=True)
	descrption=models.CharField(max_length=100, default="desc")
	to = models.DecimalField(max_digits=10, decimal_places=2, default=True)


#print(dir(models))
