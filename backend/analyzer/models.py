from django.db import models

class Resume(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    resume = models.FileField(
        upload_to='resumes/'
    )

    ats_score = models.IntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name