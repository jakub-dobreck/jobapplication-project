from django.db import models
from datetime import datetime
import re

class Candidate(models.Model):
    first_name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)
    picture_url = models.CharField(max_length = 50)
    cv_url = models.CharField(max_length = 50)
    date_time = models.DateTimeField

    def __str__(self):
        return(self.first_name + " " + self.last_name)

    def date(self):
        self.date_time = datetime.now()
        return(self.date_time.strftime('%d/%m/%Y'))

    def time(self):
        self.date_time = datetime.now()
        return(self.date_time.strftime('%H:%M'))

    def avatar(self):
        url_pattern = r"([^/]*\.[^/!(com)]+)"
        m = re.search(url_pattern, self.picture_url)
        return (self.picture_url.replace(m.group(0), "avatar:200/" + m.group(0)))