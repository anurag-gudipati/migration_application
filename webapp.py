from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

post = [
    {
        'author': 'pavan Dandu',
        'title': 'first post',
        'content': 'content of the post',
        'date_posted': 'may 12,2020'

    },
    {
        'author': 'chaitanya Thummoju',
        'title': 'latest  post',
        'content': 'content of the post',
        'date_posted': 'may 12,2020'
    },
    {
        'author': 'Anurag Gudipati',
        'title': 'Random post',
        'content': 'content of the post',
        'date_posted': 'may 12,2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=post)


@app.route("/about")
def about():
    return render_template('abou.html', title='About')


@app.route("/sql", methods=['GET', 'POST'])
def sq():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        host = request.form['host']
        user = request.form['User']
        passwd = request.form['password']
        dbname = request.form['DBName']
        print(host)
        if len(host) == 0 or len(user) == 0 or len(passwd) == 0 or len(dbname) == 0:
            error = "Please fill all the fields"

    return render_template('SQ.html', title='SQL', message=error)


@app.route("/mongo", methods=['GET', 'POST'])
def md():
    error = ""
    if request.method == 'POST':
        url = request.form['URL']
        dbname = request.form['DBName']
    return render_template('MDB.html', title='mongo', message=error)


@app.route("/dec")
def dec():
    return render_template('dec.js', title='dec')


@app.route("/sub")
def de():
    return render_template('sub.php', title='sub')


if __name__ == "__main__":
    app.run(debug=True)
