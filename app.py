from flask import Flask, render_template_string, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background: linear-gradient(135deg, #6a11cb, #2575fc);
      color: white;
      text-align: center;
    }
    .container {
      max-width: 500px;
      padding: 20px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 10px;
    }
    p {
      font-size: 1.2rem;
      margin-bottom: 20px;
    }
    a {
      text-decoration: none;
      color: white;
      background: #ff7f50;
      padding: 10px 20px;
      border-radius: 5px;
      transition: background 0.3s ease;
    }
    a:hover {
      background: #ff4500;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to My Page</h1>
    <p>This is a simple and responsive HTML page. Feel free to explore!</p>
    <a href="#">Get Started</a>
  </div>
</body>
    </html>
    """
    return render_template_string(html)

@app.route('/fetch')
def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[:5]
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@app.route('/health')
def health():
    return jsonify({"status": "App is healthy and running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
