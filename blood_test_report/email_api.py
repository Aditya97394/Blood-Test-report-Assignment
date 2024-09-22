from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
from main import execute_crew
from pyngrok import ngrok, conf
from uuid import uuid4
import smtplib
import yagmail
import base64
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

users = {
    "user1": {"password": generate_password_hash("password1")},
    "user2": {"password": generate_password_hash("password2")}
}

port = 5000
conf.get_default().auth_token = os.getenv('NGROK_AUTH_TOKEN')

public_url = ngrok.connect(port).public_url
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

# Function to send email
def send_email(subject, body, recipient_email):
    sender_email = "aditya.soni02@ssipmt.com"
    sender_password = "ssipmt@123"
    yag = yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=recipient_email,
        subject=subject,
        contents=body,
    )

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Generate the access token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Logout route (this can be used to invalidate tokens in case of token blacklisting)
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({"message": "Logout successful"}), 200

@app.route('/send-analysis', methods=['POST'])
@jwt_required()
def send_analysis():
    data = request.get_json()
    recipient_email = data.get('email')
    pdf_file = base64.b64decode(data.get('blood_test_report'))

    pdf_path = os.path.join('/tmp', str(uuid4()))  # Adjust the path as needed
    with open(pdf_path, 'wb') as f:
        f.write(pdf_file)

    pages_to_extract = [1, 3]
    blood_test_summary, found_articles, recommendations = execute_crew(pdf_path, pages_to_extract)

    subject = "Your Blood Test Analysis and Health Recommendations"
    body = f"Blood Test Summary:\n{blood_test_summary}\n\n" \
           f"Health Articles:\n{found_articles}\n\n" \
           f"Health Recommendations:\n{recommendations}"

    send_email(subject, body, recipient_email)

    return jsonify({"message": "Email sent successfully!"}), 200

if __name__ == '__main__':
    app.run()
