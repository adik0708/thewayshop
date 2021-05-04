from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.id])


class Outfit(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('outfit_detail', args=[self.id])


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.author

