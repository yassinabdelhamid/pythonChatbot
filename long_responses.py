import random

R_EATING = "I don't like food because I am a bot obviously!"

def unknown():
    response = ['Could you please re-phrase that?',
                '...',
                'Sounds about right',
                'What does that mean?'][random.randrange(4)]

    return response