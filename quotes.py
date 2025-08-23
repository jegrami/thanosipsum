
from data_service import quote_service

def get_quotes(limit):
    return quote_service.get_quotes(limit)


def get_quotes_by_movie(limit, movie):
    return quote_service.get_quotes_by_movie(limit, movie)


def get_all_from_movie(movie):
    return quote_service.get_all_from_movie(movie)


def get_all_quotes():
    return quote_service.get_all_quotes()