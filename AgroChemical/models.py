from django.db import models

class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_img = models.CharField(max_length=200)
    news_text = models.CharField(max_length=200)
    news_date = models.DateTimeField("date published")
