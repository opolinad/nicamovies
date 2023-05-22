from datetime import datetime
from movie.models import Rating

def is_create_movie_info_valid(title: str, release_date:str, genre:str, plot:str):
    is_valid = True
    messages = []
    if title == '' or genre == '' or plot == '' or not release_date:
        is_valid = False
        messages.append('Title, release_date, genre and plot are required')
    else:
        try:
            datetime.strptime(release_date, '%Y-%m-%d')
        except ValueError:
            is_valid = False
            messages.append('Release date must be a valid date on the format: "Y-m-d"')

    return (is_valid, '\n'.join(messages))

def is_create_rating_info_valid(rating:float, comment:str, movie_id:int = None, user_id:int = None):
    is_valid = True
    messages = []

    if movie_id != None and movie_id != None:
        rating = Rating.objects.filter(movie=movie_id, user=user_id)
        if len(rating) > 0:
            is_valid = False
            messages.append('Rating already exists')
    else:
        if comment == '' or rating == None:
            is_valid = False
            messages.append('Rating and comment are required')
        else:
            try:
                rating = float(rating)
                if rating < 0 or rating >5:
                    is_valid = False
                    messages.append('Rating must be a number between 0 and 5')

            except ValueError:
                is_valid = False
                messages.append('Rating must be a number')

    return (is_valid, '\n'.join(messages))
