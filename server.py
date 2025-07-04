from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import csv
import os

@app.route('/')
def home_page():
          return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
          return render_template(page_name)

def write_to_file(data):
        with open('database.txt', mode='a') as database:
                email = data['email']
                subject = data['subject']
                message = data['message']
                file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    # Always write to the CSV inside the same folder as server.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'portfo', 'database.csv')

    email = data['email']
    subject = data['subject']
    message = data['message']

    with open(file_path, mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
          if request.method == 'POST':
                  try:
                    data = request.form.to_dict()
                    print(data)
                    write_to_csv(data)
                    return redirect('/thankyou.html')
                  except:
                    return "Something went wrong"
          else:
                  return "something went wrong"
          
