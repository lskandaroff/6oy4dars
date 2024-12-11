from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='posts/photos/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

