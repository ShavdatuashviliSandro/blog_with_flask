from flask import Flask, render_template, request
import sqlite3

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


@app.route('/add_question', methods=['POST'])
def add_question():
    name = request.form.get('name')
    mail = request.form.get('mail')
    question = request.form.get('question')

    # Create record to database
    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()

    conn.execute('''
                 INSERT INTO contacts (name, email, question)
                 VALUES (?, ?, ?)
                 ''', (name, mail, question))
    conn.commit()

    # Read our data
    c.execute('SELECT name, question FROM contacts')
    rows = c.fetchall()
    questions = [{'name': row[0], 'question': row[1]} for row in rows]

    conn.close()
    return render_template('contact.html', questions=questions)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()
    c.execute('SELECT name, question FROM contacts')
    rows = c.fetchall()
    conn.close()

    questions = [{'name': row[0], 'question': row[1]} for row in rows]
    return render_template('contact.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
