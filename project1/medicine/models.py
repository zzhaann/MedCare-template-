from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title


class Remedy(models.Model):
    name = models.CharField(max_length=225)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')
    brandId = models.ForeignKey(Article, on_delete=models.PROTECT)
    def __str__(self):
        return self.name


class Surgeons(models.Model):
    name = models.CharField(max_length=225)
    Lastname = models.CharField(max_length=225)
    number = models.CharField(max_length=225)
    specialization = models.CharField(max_length=225, blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.specialization



class Nurses(models.Model):
    name = models.CharField(max_length=225)
    Lastname = models.CharField(max_length=225)
    number = models.CharField(max_length=225)
    shift = models.CharField(max_length=50, blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)




