from django.db import models

from mainapp.models import User


# Create your models here.

class Peticions(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    date = models.DateTimeField(auto_now_add=True)
    name_surname = models.TextField("name_surname")
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/petitions/{self.id}"

    class Meta:
        verbose_name = "Petition"
        verbose_name_plural = "Petitions"


class Vote(models.Model):
    name = models.CharField(max_length=150)
    petition = models.ForeignKey(Peticions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('petition', 'user'),)
