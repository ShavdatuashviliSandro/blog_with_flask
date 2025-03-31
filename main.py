from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    item = [{'id': 1, 'name': 'givi', 'email': 'sandro@gmail.com'},
            {'id': 2, 'name': 'luka', 'email': 'sandro@gmail.com'}]

    return render_template('contact.html', items = item)
if __name__ == '__main__':
    app.run(debug=True)