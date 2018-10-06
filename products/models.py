import os
import random
from django.db import models

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = oos.path.splitext(base_name)
	return name, ext
def upload_image_path(instance, filename):
	new_filename = random.randint(1,3000)
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename, final_filename=final_filename)
class ProductManager(models.Manager):
	def featured(self):
		return self.get_queryset().filter(featured=True)
	def get_by_id(self, id):
		qs= self.get_queryset().filter(id=id)
		if qs.count()==1:
			return qs.first()
		else:
			return None
# Create your models here.''
class Product(models.Model):
	tittle = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=120,default=39.99)
	image = models.FileField(upload_image_path, null=True, blank=True)
	objects = ProductManager()
	featured = models.BooleanField(default=False)
	def __str__(self):
		return self.tittle
