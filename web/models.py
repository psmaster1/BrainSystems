from django.core.cache import cache
from django.db import models

from django.utils import timezone


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


# save all questions into the db
class FAQs(models.Model):
    question = models.TextField(max_length=500)

    def __str__(self):
        return self.question[:100]


# save the contactform
class Contact(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    country_choices = (
        ('Österreich', 'Österreich'),
        ('Deutschland', 'Deutschland'),
        ('Schweiz', 'Schweiz'),
    )
    country = models.CharField(max_length=30)
    house_type = models.CharField(max_length=100)
    living_space = models.CharField(max_length=100)
    message = models.TextField()
    agreed = models.BooleanField()

    def __str__(self):
        return self.first_name


# save the metadescriptions for each page (SEO)
class PageSettings(models.Model):
    page_url = models.URLField(null=True, blank=True)
    PAGE_CHOICES = (
        ('Index', 'Index'),
        ('Contact', 'Contact'),
        ('Login', 'Login'),
        ('Registration', 'Registration'),
    )
    page = models.CharField(choices=PAGE_CHOICES, max_length=100, unique=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255, null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.page


