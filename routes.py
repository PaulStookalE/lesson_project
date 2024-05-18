from flask import redirect, render_template, request
from models import session, Car
from . import app
from dotenv import load_dotenv
import os
import requests


 
load_dotenv()



# Створюємо сторінку, куди виводимо дані про машину.
@app.route('/cars_list')
def cars_list():
    cars = session.query(Car).all()
    return render_template('cars.html', cars=cars)



# Створення функції, яка надсилатиме у FrontEnd 
@app.route('/view_auto_details/<int:id>')
def view_auto_details(id):
    auto_details = session.query(Car).get(id)
    return render_template('auto_details.html', auto_details=auto_details)



@app.route('/create_data_about_auto', metods=['GET', 'POST'])
def create_data_about_auto():
    if request.method == 'POST':
        model_name = request.form['model_name']
        engine = request.form['engine']
        type_of_fuel = request.form['type_of_fuel']

        new_auto = Car(
            model = model_name,
            engine = engine,
            tof = type_of_fuel
        )

        try:
            session.add(new_auto)
            session.commit()
            return redirect('/cars_list')
        
        except Exception as exc:
            return exc
        
        finally:
            session.close()



    else:
        return render_template('create_data_about_auto.html')



@app.route('/edit_auto_data/<int:id>', methods=['GET', 'POST'])
def edit_auto_data(id):
    auto = session.query(Car).get(id)

    if request.method == 'POST':
        model_name = request.form['model_name']
        engine = request.form['engine']
        type_of_fuel = request.form['type_of_fuel']

        auto.model_name = model_name
        auto.engine = engine
        auto.type_of_fuel = type_of_fuel

        session.commit()
        session.close()

        return redirect('/cars_list')
        
    else:
        return render_template('edit_auto_data.html')




@app.route('/delete_auto_data/<int:id>')
def delete_auto_data(id):
    auto_to_delete = session.query(Car).filter_by(id=id)
    session.delete(auto_to_delete)
    session.close()

    return redirect('/cars_list')











# Створюємо сторінку з полями для вводу і підключаємо сюди по API вебсайт з курсу валют і їх конвертування.
@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    # Перевіряємо чи натискає користувач на кнопку, тим самим надсилаючи дані із полів вводу.
    if request.method == 'POST':
        # Даємо url щоб можна було її передати по API.
        url = f"https://{os.getenv('API_HOST_RAPID')}/exchange"

        # Отримуємо дані з полів вводу.
        from_value = request.form['from']
        to_value = request.form['to']
        count = request.form['count']

        # Підставляємо дані із полів вводу у словник, щоб передати ці дані по API.
        querystring = {"from": from_value,"to": to_value}

        # Виймаємо із .env ключі до API.
        headers = {
            "X-RapidAPI-Key": os.getenv('API_KEY_RAPID'),
            "X-RapidAPI-Host": os.getenv('API_HOST_RAPID')
        }

        # Надсилаємо дані сторонньому API для того щоб взнати курс такої то валюти в таку то.
        response = requests.get(url, headers=headers, params=querystring)

        # По отриманим даним по API рахуємо скільки це вийде по валюті у яку користувач хоче перевести.
        data = response.json()
        result = data * int(count)
        return render_template('exchange.html', result=result)
    
    else:
        # Інакше просто повертаємо ту саму сторінку.
        return render_template('exchange.html')