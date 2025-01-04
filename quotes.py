
from models import Quote, quote_schema, quotes_schema
from flask import make_response, abort
from sqlalchemy import func


def get_all_quotes():
    quotes = Quote.query.all()
    if quotes:
        return quotes_schema.dump(quotes)
    else:
        abort(404, "Could not retrieve quotes. Check your query string and try again.")

def get_quotes(limit):
    quotes = Quote.query.order_by(func.random()).limit(limit).all()

    if quotes:

        if len(quotes) == 1:
            return quote_schema.dump(quotes[0]) # for single quote object
        return quotes_schema.dump(quotes) # for multiple quote objects
    else:
        abort(404, "Could not retrieve quotes. Check your query string and try again.")


def get_quotes_by_movie(limit, movie):
    quotes_by_movie = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).limit(limit).all()

    if len(quotes_by_movie) == 1:
        return quote_schema.dump(quotes_by_movie[0])
    return quotes_schema.dump(quotes_by_movie)

def get_all_from_movie(movie):
    all_quotes = Quote.query.filter(Quote.movie.ilike(f"%{movie}%")).all()

    if all_quotes:
        if len(all_quotes) == 1:
            return quote_schema.dump(all_quotes[0])
        return quotes_schema.dump(all_quotes)
    



