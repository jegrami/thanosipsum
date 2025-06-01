
from models import Quote, quote_schema, quotes_schema
from flask import make_response, abort
from sqlalchemy import func, text
import os

database_url = os.environ.get("DATABASE_URL", "")

def get_quotes(limit):
    
    
    
    if database_url and "postgresql" in database_url:
        # PostgreSQL - use raw SQL for proper randomization
        quotes = Quote.query.order_by(text('RANDOM()')).limit(limit).all()
    else:
        # SQLite - use func.random()
        quotes = Quote.query.order_by(func.random()).limit(limit).all()

    if quotes:
        if len(quotes) == 1:
            return quote_schema.dump(quotes[0])
        return quotes_schema.dump(quotes)
    else:
        abort(404, "Could not retrieve quotes. Check your query string and try again.")

def get_quotes_by_movie(limit, movie):
    
    
    if database_url and "postgresql" in database_url:
        quotes_by_movie = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).order_by(text('RANDOM()')).limit(limit).all()
    else:
        quotes_by_movie = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).order_by(func.random()).limit(limit).all()

    if quotes_by_movie:
        if len(quotes_by_movie) == 1:
            return quote_schema.dump(quotes_by_movie[0])
        return quotes_schema.dump(quotes_by_movie)
    else:
        abort(404, f"Could not find quotes from movie: {movie}")

def get_all_from_movie(movie):
    
    
    if database_url and "postgresql" in database_url:
        all_quotes = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).order_by(text('RANDOM()')).all()
    else:
        all_quotes = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).order_by(func.random()).all()

    if all_quotes:
        if len(all_quotes) == 1:
            return quote_schema.dump(all_quotes[0])
        return quotes_schema.dump(all_quotes)
    else:
        abort(404, f"Could not find quotes from movie: {movie}")

def get_all_quotes():
    quotes = Quote.query.all()
    if quotes:
        return quotes_schema.dump(quotes)
    else:
        abort(404, "Could not retrieve quotes. Check your query string and try again.")