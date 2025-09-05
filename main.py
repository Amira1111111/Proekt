from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Это главная страница.'

@app.route('/Agidel')
def about():
    return 'Здесь будет информация о городе Агидель.'

@app.route('/Baymak')
def about():
    return 'Здесь будет информация о городе Бфймак.'

@app.route('/Blagovechnsk')
def about():
    return 'Здесь будет информация о городе Благовещенск.'

@app.route('/Agidel')
def about():
    return 'Здесь будет информация о городе Агидель.'

@app.route('/Baymak')
def about():
    return 'Здесь будет информация о городе Бфймак.'
 


if __name__ == '__main__':
    app.run()


