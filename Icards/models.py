from django.db import models

# Create your models here.
class Add_category(models.Model):
    category_name = models.CharField(max_length=100)   

    def __str__(self):
        return self.category_name

class Add_subcategory(models.Model):
    main_category = models.ForeignKey(Add_category, on_delete=models.CASCADE) 
    subcategory_name = models.CharField(max_length=20)
    subcategory_image = models.ImageField(default='default.jpg', upload_to='subcategory_images') 

    def __str__(self):
        return self.subcategory_name


class Add_icard(models.Model):
    subcategory = models.ForeignKey(Add_subcategory, on_delete=models.CASCADE) 
    title = models.CharField(max_length=20)  
    title_image = models.ImageField(default='default.jpg', upload_to='title_images')  
 
    def __str__(self):
        return self.title