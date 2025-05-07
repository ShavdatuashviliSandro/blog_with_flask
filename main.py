from flask import Flask, render_template, request, redirect, url_for
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
    conn.close()
    return render_template('contact.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        conn = sqlite3.connect('my_blogs.db')
        c = conn.cursor()
        c.execute("SELECT email, password FROM users WHERE email = ?", (user_email,))
        rows = c.fetchall() # [('sandro@gmail.com', '12341234')]
        if rows:
            database_password = rows[0][1]

            if database_password == user_password:
                return redirect(url_for('admin'))
        conn.close()


    return render_template('sign_in.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin_contacts')
def admin_contacts():
    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    rows = c.fetchall()
    conn.close()

    questions = []
    for row in rows:
        questions.append({'id': row[0],'name': row[1], 'email': row[2], 'question': row[3]})

    print(questions)
    return render_template('admin_contacts.html', questions = questions)


if __name__ == '__main__':
    app.run(debug=True)
