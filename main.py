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
    items = 1
    return render_template('contact.html', items = items)

if __name__ == '__main__':
    app.run(debug=True)