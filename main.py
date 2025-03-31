from flask import Flask, render_template

app = Flask(__name__)

cards = [
             {'title': 'ქართველი ჩემპიონები',
             'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.'},
             {'title': 'მსოფლიო რეკორდები',
              'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.'},
             {'title': 'ქართველი ჩემპიონები',
              'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.'},
             {'title': 'მსოფლიო რეკორდები',
              'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.'},
             {'title': 'მსოფლიო რეკორდები',
              'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.'}
             ]


@app.route('/')
def index():
    return render_template('index.html', cards=cards)

@app.route('/add_item/<title>/<description>')
def add_item(title,description):
    cards.append({'title': title, 'description': description})
    return render_template('index.html', cards=cards)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    names = ['გიორგი', 'სანდრო', 'რეზი', 'ერეკლე', 'ლიზი']
    return render_template('contact.html', names = names)

if __name__ == '__main__':
    app.run(debug=True)