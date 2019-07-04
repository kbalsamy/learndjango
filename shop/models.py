from django.db import models
from django.urls import reverse

# Create your models here.


class Catagory(models.Model):

    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):

        return self.name

    def get_absoulte_url(self):

        return reverse('shop:product_list_by_catagory', args=[self.slug, ])


class Product(models.Model):

    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='catagory',)
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):

        return self.name

    def get_absoulte_url(self):

        return reverse('shop:product_detail', args=[self.id, self.slug])
