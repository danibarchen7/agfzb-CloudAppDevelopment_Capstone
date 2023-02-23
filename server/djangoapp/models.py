from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarMake(models.Model):
    Name = models.CharField(max_length=255)
    Description  = models.CharField(max_length=255)
    def __str__():
        print(Name,Description)

class CarModel(models.Model):
    Name = models.CharField(max_length=255)
    carmake = models.ManyToManyField(CarMake)
    Type= models.CharField(max_length=255) 
    year = models.DateField()
    def __str__():
        print(Name,carmake,Type,year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
