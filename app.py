from flask import Flask, render_template, request, jsonify
import sqlite3
from chatbot import get_response
from database import create_table, insert_sample_data, create_users_table

app = Flask(__name__)


create_table()
insert_sample_data()
create_users_table()  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_reply = get_response(user_message)
    return jsonify({'response': bot_reply})

@app.route('/submit_contact', methods=['POST'])  
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    location = request.form.get('location', '')  
    message = request.form.get('message')

    if not (name and email and phone and message):
        return jsonify({'status': 'error', 'message': 'All fields are required!'}), 400

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone, location, message) VALUES (?, ?, ?, ?, ?)",
                   (name, email, phone, location, message))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'Your message has been submitted successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
