from django.db import models

class Materi(models.Model):
    GRADE_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    file = models.FileField(upload_to='materi_files/')

    def __str__(self):
        return self.title
