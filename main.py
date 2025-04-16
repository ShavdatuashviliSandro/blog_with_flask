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

questions = []
@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add_question', methods=['POST'])
def add_question():
    name = request.form.get('name')
    mail = request.form.get('mail')
    question = request.form.get('question')

    questions.append({'name': name, 'mail': mail, 'question': question})
    return render_template('contact.html', questions=questions)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
