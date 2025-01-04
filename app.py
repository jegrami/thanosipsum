from flask import render_template
import config


from models import Quote


app = config.connexion_app
app.add_api(config.basedir / "swagger.yml")

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
    app.run(debug=True)


