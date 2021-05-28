from random import randint
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.IntegerField(null=True, blank=True)
    social_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    def _get_random(self):
        return randint(1, 1000)


    def save(self, *args, **kwargs):
        if not self.social_code:
            self.social_code = "sc"+str(self._get_random())
        super().save(*args, **kwargs)   	

    def get_absolute_url(self):
    	return reverse("clbaseviews:detail_person", kwargs={"pk": self.pk})


class Company(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name='employees')

    def __str__(self):
        return self.first_name

    def get_employee_company(self, company):
        emp_com = Employees.objects.get(pk=company)
        return emp_com.company


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")


    def __str__(self):
        return self.headline


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

class Reponse(models.Model):
    contenu = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")

    def __str__(self):
        return self.contenu