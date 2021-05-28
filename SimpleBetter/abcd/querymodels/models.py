from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return (f"{self.name}")

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	salutation = models.CharField(max_length=10)
	headshot = models.ImageField(upload_to='author_headshots')


	def __str__(self):
		return (f"{self.first_name} - {self.last_name}")

class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField(null=True, blank=True)
	# objects = BookManager()
	books = models.Manager()

	def __str__(self):
		return (f"{self.title}")


class MaleManager(models.Manager):
	def get_queryset(self):
		return super(MaleManager, self).get_queryset().filter(sex='M')

class FemaleManager(models.Manager):
	def get_queryset(self):
		return super(FemaleManager, self).get_queryset().filter(sex='F')

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
	people = models.Manager()
	men = MaleManager()
	women = FemaleManager()

	def __str__(self):
		return (f"{self.first_name}")


class Personne(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_date = models.DateField()


	def baby_boomer_status(self, test_name):
	# def baby_boomer_status(self):
	# Returns the person's baby-boomer status.
		# import datetime
		
		# if self.birth_date < datetime.date(1945, 8, 1):
		# 	return "Pre-boomer"
		# elif self.birth_date < datetime.date(1965, 1, 1):
		# 	return "Baby boomer"
		# else:
		# 	return "Post-boomer"

		if self.last_name == test_name:
			return "C'est bien l'oeuvre du parametre"
		else:
			return "Section à assimiler le plutot possible"
	
	def _get_full_name(self):
	# Returns the person's full name."
		return (f"{self.first_name} - {self.last_name}")
	full_name = property(_get_full_name)


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def save(self, *args, **kwargs):
		if self.name == "SAM":
			return (f"Veuillez saisir un autre Nom")
		else:
			self.name = self.name+"-Bon"
			super(Blog, self).save(*args, **kwargs)

	def __str__(self):
		return self.name