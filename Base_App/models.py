from django.db import models

# Create your models here.
class Item_List(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Item(models.Model):
    Item_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Item_List, related_name='Name', on_delete=models.CASCADE)

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    description = models.TextField()    

class Feedback(models.Model):
    User_name = models.CharField(max_length=100)
    Description = models.TextField()
    Ratings = models.IntegerField()
    Image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.User_name

class BookTable(models.Model): 
    Name = models.CharField(max_length=100)
    PhoneNumber = models.IntegerField()
    Email = models.EmailField()
    Total_Persons = models.IntegerField()
    Booking_date = models.DateField()

