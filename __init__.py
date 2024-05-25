# У цьому файлі створюємо основні речі, такі як самі додатки чи бази даних.

import os
from dotenv import load_dotenv
from flask import Flask


# Підвантажуємо дані із файлу .env.
load_dotenv()

# Створюємо додаток Flask.
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



from . import routes



# # Потрібно для запуску вебсайту через IDE. При запусканні через термінал код нище не потрібен.
if __name__ == '__main__':
    app.run(debug=True)
