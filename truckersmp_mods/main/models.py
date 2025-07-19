from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=30, null=False)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Mod(models.Model):
    CATEGORY_CHOICES = [
        ('gameplay', 'Улучшенный геймплей'),
        ('lights', 'Световые приборы'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='main/images/',
        default="Update 1.8.jpg",
        verbose_name='Изображение'
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    views_count = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='main/images/',
        default="Update 1.8.jpg",
        verbose_name='Изображение'
    )
    views_count = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
