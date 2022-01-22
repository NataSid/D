from django.db import models
from django.core.validators import MinValueValidator


class News(models.Model):
    name = models.CharField(
        max_length=180,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'