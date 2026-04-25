import pandas as pd

movies = pd.DataFrame({
    'title': [
        'Interstellar', 'The Martian', 'Gravity',
        'Titanic', 'La La Land', 'The Notebook',
        'The Dark Knight', 'Avengers', 'John Wick',
        'Parasite', 'The Godfather', 'Schindler\'s List'
    ],
    'sci_fi':   [1.0, 0.9, 0.9, 0.0, 0.0, 0.0, 0.2, 0.6, 0.0, 0.0, 0.0, 0.0],
    'action':   [0.7, 0.6, 0.5, 0.1, 0.0, 0.0, 1.0, 1.0, 1.0, 0.2, 0.3, 0.1],
    'romance':  [0.2, 0.1, 0.3, 1.0, 0.8, 1.0, 0.1, 0.2, 0.0, 0.2, 0.3, 0.1],
    'drama':    [0.6, 0.5, 0.4, 0.8, 0.7, 0.7, 0.7, 0.3, 0.2, 1.0, 1.0, 1.0],
    'thriller': [0.5, 0.3, 0.6, 0.1, 0.0, 0.0, 1.0, 0.5, 0.9, 0.8, 0.9, 0.6],
})

print(movies)