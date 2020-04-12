from flask import Flask, render_template, request, redirect
import os
import csv


app = Flask(__name__)


def write_to_csv(data):
    with open('messages.csv', 'a', newline='') as fh:
        writer = csv.writer(fh, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        email = data['email']
        subject = data['subject']
        message = data['message']

        writer.writerow([email, subject, message])


def write_to_text(data):
    with open('messages.txt', 'a') as fh:

        email = data['email']
        subject = data['subject']
        message = data['message']

        fh.write(f'{email}, {subject}, {message}\n')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to datebase'
    else:
        return 'Something went wrong'
