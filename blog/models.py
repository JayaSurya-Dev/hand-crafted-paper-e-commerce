from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    """
    Database model for Posts
    """
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name="blog_posts")
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT)
    featured_image = models.ImageField(
        upload_to="blog_images/",
        null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        """Set the order of posts by descending date """
        ordering = ["-created_on"]

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Post: {self.title} by {self.author}"

    def save(self, *args, **kwargs):
        """Save method override with slugify"""
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """ Get the post detail absolute url """
        return reverse("blog:post_detail", args=[self.slug])


class Comment(models.Model):
    """
    Database model for post comments
    """
    post = models.ForeignKey(
        Post, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name="comments")
    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name="blog_comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ["created_on"]

    def __str__(self):
        """Returns comment username"""
        return self.user.username
