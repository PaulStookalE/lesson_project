from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer



# Створюємо 'диспетчера'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'          # Створюємо базу даних і називаємо її.


# Створюємо базу даних.
db = SQLAlchemy(app)


# Створюємо таблицю.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(24), unique=True)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'), nullable=False, unique=True)


# Створюємо таблицю
class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

    # // one to many //
    # users = db.relationship('User', backref='notebook', lazy=True)


# Створюємо саму БД.
with app.app_context():
    db.create_all()





# Створюємо перший шлях "/", який просто виводитиме текст.
@app.route("/")
def hello():
    return "Hello world!"


# Створюмо функцію, яка братиме HTML-форматування з файлу main.html з папки templates і, за допомогою Jinja об'єднує HTML- та Python код і віддає у веб.
@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    else:
        datas = {
            '1': 'Paul'
        }
        description = 'This is the first lesson about templates'
        header = 'First template'
        # Функція render_template бере передані в неї дані і надсилає їх у HTML-файл, який форматує ці дані і виводить у браузер.
        return render_template(
            "main.html",
            header= header,
            description= description,
            datas= datas,
            title= 'Main'
        )





# Створюємо роут для сторінки 'about'.
@app.route('/about')
def about():
    return render_template('about.html')
    




# Робимо так, щоб код запускався.
if __name__ == '__main__':
    app.run(debug=True)