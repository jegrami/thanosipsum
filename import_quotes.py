
import json
from config import app, db
from models import Quote

def import_quotes():
    with app.app_context():
        
        db.create_all()
        
        
        if Quote.query.first():
            print("Quotes already exist")
            return
        
        
        with open('quotes_data.json', 'r') as f:
            quotes_data = json.load(f)
        
        for quote_data in quotes_data:
            quote = Quote(
                quote=quote_data['quote'],
                movie=quote_data['movie'],
                keyword=quote_data['keyword']
            )
            db.session.add(quote)
        
        db.session.commit()
        print(f"Imported {len(quotes_data)} quotes successfully!")

if __name__ == '__main__':
    import_quotes()