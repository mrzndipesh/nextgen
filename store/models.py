from django.db import models
from django.utils import timezone

class Shop(models.Model):

	shopName = models.CharField(max_length=100)
	shopDesc = models.CharField(max_length=200)
	shopRating = models.IntegerField()
	shopLocation = models.CharField(max_length=100)

	def __str__(self):
		return self.shopName

class Category(models.Model):
	categoryName= models.CharField(max_length=100)
	shop = models.ForeignKey(Shop, related_name="reference", on_delete=models.CASCADE)

	def __str__(self):
		return self.categoryName

class SubCategory(models.Model):
	
	category = models.ForeignKey(Category, related_name='reference', on_delete=models.CASCADE)
	subCategoryName = models.CharField(max_length=100)
	def __str__(self):
		return self.subCategoryName

class Product(models.Model):
	productSubCategory = models.ForeignKey(SubCategory, related_name="reference", on_delete=models.CASCADE)
	productName= models.CharField(max_length=100)
	productDesc = models.CharField(max_length=500)
	productStock = models.IntegerField()
	productPrice = models.IntegerField()
	productCPrice= models.IntegerField(default=0)
	
	def __str__(self):
		return self.productName

class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='reference',on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/img')
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class SliderImage(models.Model):
	image = models.ImageField(upload_to='store/static/slider/img')
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

#class BillGeneration(models.Model):
#	date = models.DateTimeField(default=datetime.now(), blank=True)
#	CustomerName = models.CharField(max_length=100)
#	CustomerAddress = models.CharField(max_length=100)
#	CustomerContact = models.IntegerField()
#	ProductName = Product.productName()
#	ProductPrice = Product.productPrice()
#	ProductQuantity = models.IntegerField(default=0)
#	ProductPreTotal = ProductPrice * ProductQuantity
#	productStock = productStock - ProductQuantity

class DailyEntry(models.Model):
	title = models.CharField(max_length=50)
	amt = models.IntegerField(default=0)
	amount = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	income = models.BooleanField(default=True)
	
	if income==True:
		amt = amt + amount

	elif income==False:
		amt = amt - amount

	def __int__(self):
		return self.amt


