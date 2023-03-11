from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


RATING = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]


class Category(models.Model):
    """
    Database model for Category
    """
    parent = models.ForeignKey('self',
                               null=True, blank=True,
                               related_name='children',
                               on_delete=models.CASCADE)
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
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/',
                              null=True, blank=True)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    wishlist = models.ManyToManyField(User, related_name='wishlist',
                                      blank=True, default=None)

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

    def get_absolute_url(self):
        """ Get the product detail absolute url """
        return reverse('products:product_detail',
                       args=[self.id, self.slug])

    def get_rating(self):
        """ Get product average rating """
        total = sum(int(review['stars']) for review in self.reviews.values())
        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class ProductReview(models.Model):
    """
    Database Model for Product Reviews
    """
    product = models.ForeignKey(Product,
                                related_name="reviews",
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name="reviews",
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.DecimalField(choices=RATING,
                                max_digits=6, decimal_places=2,
                                default=3,
                                null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
