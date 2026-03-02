# Script running the website and combining the frontend and backend!
from flask import Flask, render_template, jsonify, request
import threading
import os
import sys
import subprocess

app = Flask(__name__, template_folder='frontend')

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to serve data to the frontend (route is redundant for now)
@app.route('/api/data')
def get_data():
    data = {"message": "Hello world!"}
    return jsonify(data)

# Running our first script!
@app.route('/first_finch_test', methods=['POST'])
def first_finch_test():
    script_path = os.path.join('backend', 'meow.py')
    try:
        result = subprocess.check_output(
            [sys.executable, script_path],
            text = True,
            stderr = subprocess.STDOUT
        )
        return jsonify({"status": "success", "output": result.strip()})   
    # This should point directly to the script you want to run
    # WRITE HERE

    except FileNotFoundError:
        error_msg = f"Error: The file '{script_path}' was not found."
        print(error_msg)
        return jsonify({"status": "error", "message": error_msg}), 500

    except Exception as e:
        print(f"General Error: {str(e)}")
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

