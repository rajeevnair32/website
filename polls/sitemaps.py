from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Question

class PollSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Question.objects.all()
