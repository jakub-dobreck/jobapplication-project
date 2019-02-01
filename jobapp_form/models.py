from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)
    picture_url = models.CharField(max_length = 50)
    cv_url = models.CharField(max_length = 50)
    date_time = models.DateTimeField

    def __str__(self):
        return(self.first_name + " " + self.last_name)

    def date(self):
        return(self.date_time.strftime('%d/%m/%Y'))

    def time(self):
        return(self.date_time.strftime('%H:%M'))