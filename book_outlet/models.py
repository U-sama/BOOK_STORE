from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name + ", " + self.code
    
    class Meta:
        verbose_name_plural = "Countries"
    

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries" # change the displayed name of the class ont the book_outlet menu


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    #author = models.CharField(null=True,max_length=100) # Old one 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(null=False, default="",
     db_index=True, blank=True) #editable= False made the variable ont show in the admin page
    published_countries = models.ManyToManyField(Country, related_name="books")

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    # def save(self,*arg,**kwarg) :
    #     self.slug = slugify(self.title)
    #     return super().save(*arg,**kwarg)
    

    def __str__(self):
        return f"{self.title} ({self.rating})"
