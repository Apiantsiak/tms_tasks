from django.db import models


class HistoryLog(models.Model):
    datetime = models.DateTimeField()
    url = models.CharField(max_length=50)
    result = models.TextField()

    def __str__(self):
        return f'{self.datetime} {self.pk} {self.url} {self.result}'
