from django.db import models


class Level(models.Choices):
    ISCED0 = "Early childhood education"
    ISCED1 = "Primary Education"
    ISCED2 = "Lower Secondary Education"
    ISCED3 = "Upper Secondary Education"
    ISCED4 = "Post-Secondary non-Tertiary Education"
    ISCED5 = "Short-cycle tertiary education"
    ISCED6 = "Bachelors degree or equivalent education level"
    ISCED7 = "Masters degree or equivalent education level"
    ISCED8 = "Doctoral degree or equivalent education level"
    DEFAULT = "Not Informed"


class Academic(models.model):
    id = models.UUIDField(primary_key=True, unique=True)
    educational_level = models.CharField(max_length=255, choices=Level.choices, default=Level.DEFAULT)
    is_graduated = models.BooleanField(default=False, null=True)
    main_graduation = models.CharField(max_length=128, null=True)
