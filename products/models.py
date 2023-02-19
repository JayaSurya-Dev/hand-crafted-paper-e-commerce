from django.db import models


class Category(models.Model):
    """
    Database model for Category
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        """
        Set the order of categories by ascending order
        Set the plural name for category
        Creates an index of category names in ascending order
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """ Returns category name """
        return self.name

    def get_friendly_name(self):
        """ Get the category friendly name """
        return self.friendly_name


class Product(models.Model):
    """
    Database model for Product
    """
    category = models.ForeignKey(Category, related_name='products',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Set the order of products by ascending order
        Creates indexes of products by id, slug and name in ascending order
        Creates an index of products creation date in descending order
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_on']),
        ]

    def __str__(self):
        """ Returns category name """
        return self.name
