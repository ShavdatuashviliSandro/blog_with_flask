from flask import Flask, render_template

app = Flask(__name__)

items = [
    {'title': 'ქართველი ჩემპიონები',
     'author': 'ლაშა ბახია',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.'},
    {'title': 'მსოფლიო რეკორდები',
     'author': 'ლაშა ჩოხელი',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.'},
    {'title': 'ქართველი ჩემპიონები',
     'author': 'მარიამ კობერიძე',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.'},
    {'title': 'მზიურის თანაშრომლები',
     'author': 'გიორგი ბაზუაშვილი',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.'}
]


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add_item/<title>/<description>/<author>')
def add_item(title, description, author):
    items.append({'title': title, 'description': description, 'author': author})
    return render_template('index.html', items=items)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    names = ['გიორგი', 'სანდრო', 'რეზი', 'ერეკლე', 'ლიზი']
    return render_template('contact.html', names=names)


if __name__ == '__main__':
    app.run(debug=True)
