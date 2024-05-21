from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

class Category(models.Model):
    name = models.CharField(max_length=3)
    main_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Использование unidecode для преобразования любого Unicode текста в ASCII
            self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Использование unidecode для преобразования любого Unicode текста в ASCII
            self.slug = slugify(unidecode(self.name))
        super(Subcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Использование unidecode для преобразования любого Unicode текста в ASCII
            self.slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
