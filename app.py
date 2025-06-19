from flask import Flask
from routes.pdf_to_word import pdf_to_word_route
from routes.word_to_pdf import word_to_pdf_route

app = Flask(__name__)
app.register_blueprint(pdf_to_word_route)
app.register_blueprint(word_to_pdf_route)

@app.route('/')
def home():
    return 'خدّام شغال 💪'

if __name__ == '__main__':
    app.run(debug=True)

