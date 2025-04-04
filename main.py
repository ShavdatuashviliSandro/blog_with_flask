from flask import Flask, render_template, request

app = Flask(__name__)

items = [
    {'title': 'ქართველი ჩემპიონები',
     'author': 'ლაშა ბახია',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.',
     'photo_url': 'https://foundr.com/wp-content/uploads/2021/09/Best-online-course-platforms.png'},
    {'title': 'მსოფლიო რეკორდები',
     'author': 'ლაშა ჩოხელი',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.',
     'photo_url': 'https://foundr.com/wp-content/uploads/2021/09/Best-online-course-platforms.png'},
    {'title': 'ქართველი ჩემპიონები',
     'author': 'მარიამ კობერიძე',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მოზარდების ძიუდოთი დაინტერესების დადებით თვისებებს.',
     'photo_url': 'https://foundr.com/wp-content/uploads/2021/09/Best-online-course-platforms.png'},
    {'title': 'მზიურის თანაშრომლები',
     'author': 'გიორგი ბაზუაშვილი',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.',
     'photo_url': 'https://foundr.com/wp-content/uploads/2021/09/Best-online-course-platforms.png'},
    {'title': 'მზიურის თანაშრომლები',
     'author': 'გიორგი ბაზუაშვილი',
     'description': 'ამ სტატიაში თქვენ წაიკითხავთ მსოფლიო რეკორდების შესახებ.',
     'photo_url': 'https://foundr.com/wp-content/uploads/2021/09/Best-online-course-platforms.png'}
]


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add_item', methods=['POST'])
def add_item():
    photo_url = request.form.get('photo_url')
    title = request.form.get('title')
    author = request.form.get('author')
    description = request.form.get('description')

    # Process and add the item to the list
    items.append({'photo_url': photo_url, 'title': title, 'author': author, 'description': description})
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
