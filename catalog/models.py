from django.db import models
from django.urls import reverse


class My_model(models.Model):
    title = models.CharField(max_length=200, help_text='Enter main group dish')
    text_main = models.CharField(max_length=200, help_text="Enter name dish")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
        return '%s, %s' % (self.title, self.text_main)
