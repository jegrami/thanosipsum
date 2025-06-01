
from flask import render_template
import config
from models import Quote

app = config.connexion_app
app.add_api(config.basedir / "swagger.yml")


with config.app.app_context():
    config.db.create_all()
    
    
    if not Quote.query.first():
        print("Database is empty, importing quotes...")
        try:
            import json
            with open('quotes_data.json', 'r') as f:
                quotes_data = json.load(f)
            
            for quote_data in quotes_data:
                quote = Quote(
                    quote=quote_data['quote'],
                    movie=quote_data['movie'],
                    keyword=quote_data['keyword']
                )
                config.db.session.add(quote)
            
            config.db.session.commit()
            print(f"Imported {len(quotes_data)} quotes!")
        except Exception as e:
            print(f"Error importing quotes: {e}")

@app.route('/')
def home():
    quotes = Quote.query.all()
    return render_template('home.html', quotes=quotes)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()