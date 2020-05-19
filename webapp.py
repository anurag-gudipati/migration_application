from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
source_DB=""
target_DB=""
host=""
user=""
passwd=""
dbname=""
#creating home page
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    error = ""

    if request.method == 'POST':
        home.source_DB = request.form['Source']
        home.target_DB = request.form['Target']


    return render_template('home.html')


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
        #print(host,user,passwd,dbname)
        if len(host) == 0 or len(user) == 0 or len(passwd) == 0 or len(dbname) == 0:
            error = "Please fill all the fields"

    return render_template('SQ.html', title='SQL', message=error)


@app.route("/mongo", methods=['GET', 'POST'])
def md():
    error = ""
    if request.method == 'POST':
        url = request.form['URL']

    return render_template('MDB.html', title='mongo', message=error)


@app.route('/thank')
def json():
    return render_template('thank.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print(home.source_DB,home.target_DB)
    return ("nothing")





if __name__ == "__main__":
    app.run(debug=True)
