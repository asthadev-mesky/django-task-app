from django.db import models

# Create your models here.
class Report(models.Model):
    report_name = models.CharField(max_length=255)
    report_subject = models.CharField(max_length=255)
    to = models.TextField()
    cc = models.TextField(null=True, blank=True)
    bcc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    attachment = models.FileField(upload_to='report_attachments/')

    def __str__(self):
        return self.report_name + ' | ' + self.created_at.strftime("%d-%m-%Y, %I:%M %p")

