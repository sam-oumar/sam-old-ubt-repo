from django.db import models
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES = (
		('action', 'ACTION'),
		('drama', 'DRAMA'),
		('comedy', 'COMEDY'),
		('romance', 'ROMANCE'),
	)

LINK_CHOICES = (
		('d', 'Download'),
		('w', 'Watch Link'),
	)

class Movies(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=1000)
	year_of_production = models.DateField()
	views_count = models.IntegerField(default=0)
	slug = models.SlugField(max_length=100, unique=True, editable=True)

	def __str__(self):
		return f"{self.title}"

	def save(self, *args, **kwargs):
		# if not self.slug:
		self.slug = slugify(f"{self.category}-{self.title}")
		super().save(*args, **kwargs)

class MovieLinks(models.Model):
	movie = models.ForeignKey(Movies, related_name="movielinks", on_delete=models.CASCADE)
	type_link = models.CharField(choices=LINK_CHOICES, max_length=1)
	link = models.URLField()

	def __str__(self):
		return f"{self.movie}-{self.type_link}"