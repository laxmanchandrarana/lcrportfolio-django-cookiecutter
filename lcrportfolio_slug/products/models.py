from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='products/thumbnails/')
    description = models.TextField()
    tags = models.CharField(max_length=100)  # You might want to use a ManyToManyField for tags in a real app

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    graduation_date = models.DateField()

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional link

    def __str__(self):
        return self.title