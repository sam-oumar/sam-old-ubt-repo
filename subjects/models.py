from django.db import models

# Create your models here.
class Subject(models.Model):
    SERIES = (
        ("", "Serie..."),
        ("TSE", "TSE (Terminale Sciences Exactes)"),
        ("TLL", "TLL (Terminale Lettres et Litteratures)"),
        ("TSS", "TSS (Terminale Sciences Sociales)"),
        ("TSECO", "TSECO (Terminale Sciences Economiques)"),
        ("TSEXP", "TSEXP (Terminale Sciences Expérimentales)"),
    )

    year = models.IntegerField()
    duration = models.IntegerField(null=True, blank=True)
    matiere = models.CharField(max_length=200)
    classroom = models.CharField(max_length=100, choices=SERIES)
    coefficient = models.IntegerField()
    pdf_file = models.FileField(null=True, blank=True)
    page_count = models.IntegerField(default=1)

    class Meta:
        ordering = ["-year"]
        unique_together = ("year", "matiere", "classroom")

    def __str__(self):
        return f"{self.classroom} : {self.matiere} {self.year}"


class SubjectImage(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="images"
    )
    page_number = models.IntegerField()
    image_file = models.ImageField(upload_to="subject_img", default="default.png")

    def __str__(self):
        return f"Page {self.page_number}"
