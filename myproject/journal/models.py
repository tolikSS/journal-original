from django.db import models

class Entry(models.Model):
    street = models.CharField(max_length=255)
    user_code = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)  # Новое поле для статуса "Выполнено"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street} - {self.user_code} {'(===Выполнено===)' if self.is_completed else ''}"
