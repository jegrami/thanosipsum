import json
import random 
from flask import abort

class QuoteDataService:
    def __init__(self):
        self.quotes = []
        self.load_data()

    
    def load_data(self):
        try:
            with open ('quotes_data.json', 'r') as f:
                self.quotes = json.load(f)
        except FileNotFoundError:
            print('either the quotes_data.json cannot be found or there is something wrong with this loading logic.')
            self.quotes = []
    

    def get_all_quotes(self):
        if self.quotes:
            return self.quotes
        else:
            abort(404, 'I tried to get all quotes but there was an error.')
    
    def get_quotes(self, limit):
        if self.quotes:
            selected = random.sample(self.quotes, min(limit, len(self.quotes)))
            return selected if len(selected) > 1 else selected[0]
        else:
            abort(404, 'I tried to fetch that number of quotes but there was an error')
    
    def get_quotes_by_movie(self, limit, movie):
        movie_quotes = [q for q in self.quotes if movie.lower() in q['movie'].lower() ]


        if movie_quotes:
            selected = random.sample(movie_quotes, min(limit, len(movie_quotes)))
            return selected if len(selected) > 1 else selected[0]
        else:
            abort(404, f'could  not find quotes frm {movie}')
    
    def get_all_from_movie(self, movie):
        movie_quotes = [q for q in self.quotes if movie.lower in q['movie'].lower()]

        if movie_quotes:
            return movie_quotes
        else:
            abort(404, f'failed to scoop all quotes from {movie}')


quote_service = QuoteDataService()