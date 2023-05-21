from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    plot = models.TextField()

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.title

class Rating(models.Model):
    rating = models.FloatField()
    comment = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ratings'

    def __str__(self):
        return f'Rating of {self.rating} by {self.user}'