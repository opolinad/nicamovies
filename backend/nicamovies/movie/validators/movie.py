from datetime import datetime

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
