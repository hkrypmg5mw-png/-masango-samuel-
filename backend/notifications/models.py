from django.db import models

class SMSNotification(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
    ), default='PENDING')

    def __str__(self):
        return f"To {self.phone_number} - {self.status}"

class AppNotification(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} for {self.user}"
