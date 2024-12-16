from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
