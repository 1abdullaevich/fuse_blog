from django.db import models
from django.contrib.auth.models import AbstractUser


class GenderModel(models.Model):
    gender = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.gender


class UserModel(AbstractUser):
    user_avatar = models.ImageField(upload_to='user_avatars', default='default/avatar.jpg', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    gender = models.ForeignKey(GenderModel, on_delete=models.CASCADE, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=40, null=True, blank=True)
    social_accounts = models.URLField()
    subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def __str__(self):
        return self.username


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images', default='default/default_post.jpg')
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    @property
    def post_count(self):
        return self.post_set.count()

    def __str__(self):
        return self.name


class TagModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


