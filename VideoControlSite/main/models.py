from django.db import models
import uuid

class CamDB(models.Model):
    title = models.CharField(max_length=200)
    camdb_id = models.CharField(max_length=100, primary_key=True, unique=True)
    author = models.CharField(max_length=200)
    views = models.PositiveIntegerField()
    position = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.camdb_id:
            # Генерируем уникальный идентификатор для camdb_id
            self.camdb_id = str(uuid.uuid4())
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title