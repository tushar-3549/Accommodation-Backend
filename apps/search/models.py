from django.db import models

class SearchSuggestion(models.Model):
    class EntityType(models.TextChoices):
        CITY = "CITY", "City"
        LANDMARK = "LANDMARK", "Landmark"
        PROPERTY = "PROPERTY", "Property"

    entity_type = models.CharField(max_length=20, choices=EntityType.choices)
    display = models.CharField(max_length=200)
    ref_id = models.PositiveIntegerField()  # FK id for target model (denorm)
    extra = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.display} [{self.entity_type}]"
