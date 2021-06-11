from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cage(models.Model):
    class Meta:
        verbose_name = 'Cage'
        verbose_name_plural = 'Cages'

    size = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name='Size',
        help_text="Cage size in foot.",
        error_messages="Size must be in number only",
        validators=[
            MaxValueValidator(140),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.size
