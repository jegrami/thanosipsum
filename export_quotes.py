
import sqlite3
import json
from pathlib import Path

def export_quotes():
    basedir = Path(__file__).parent.resolve()
    conn = sqlite3.connect(basedir / 'thanos3.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT quote, movie, keyword FROM quotes")
    quotes = cursor.fetchall()
    
    quotes_data = []
    for quote, movie, keyword in quotes:
        quotes_data.append({
            'quote': quote,
            'movie': movie,
            'keyword': keyword
        })
    
    with open('quotes_data.json', 'w') as f:
        json.dump(quotes_data, f, indent=2)
    
    conn.close()
    print(f"Exported {len(quotes_data)} quotes to quotes_data.json")

if __name__ == '__main__':
    export_quotes()
