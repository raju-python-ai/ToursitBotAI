from fuzzywuzzy import process
import sqlite3

def get_response(user_input):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM chatbot_responses")
    data = cursor.fetchall()  

    conn.close()

    questions = [row[0] for row in data]  
    best_match, score = process.extractOne(user_input, questions)

    if score > 75:  # Only accept if similarity score is high
        for q, a in data:
            if q == best_match:
                return a
    return "I'm sorry, I didn't understand. Can you rephrase?"
