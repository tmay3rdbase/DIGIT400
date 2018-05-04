from flask import Flask, render_template, flash, url_for, redirect, request, session, make_response, send_file, send_from_directory
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from datetime import datetime, timedelta
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc
import os
from functools import wraps
from content_management import Content
from db_connect import connection
from pages import dates
from search import search, link


APP_CONTENT = Content()
PAGE_CONTENT = dates()

UPLOAD_FOLDER = '/var/www/FlaskApp/FlaskApp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, instance_path='/var/www/FlaskApp/FlaskApp/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Please login.")
            return redirect(url_for('login_page'))
    return wrap

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''Example
@app.route('/lower/', methods=["GET","POST"])
def uppercase():
    try:
        uppered = ""
        if request.method == "POST":
            lower = request.form['upper']
            uppered = library(lower)
            
              return render_template("uppercase.html", uppered = uppered)

        return render_template("uppercase.html", uppered = uppered)

    except Exception as e:
        return str as e
    '''
    
@app.route("/navbar/", methods=["GET","POST"])
def navbar():
    return render_template("navbar.html", PAGE_CONTENT = PAGE_CONTENT)    

@app.route("/", methods=["GET","POST"])
def main():
	return render_template("MemeLine.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/about/", methods=["GET","POST"])
def about():
	return render_template("about.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/Beginning/", methods=["GET","POST"])
def Beginning():
	return render_template("Beginning.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/Development/", methods=["GET","POST"])
def Development():
	return render_template("Development.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/Psychological/", methods=["GET","POST"])
def Psychological():
	return render_template("Psychological.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/futureTrends/", methods=["GET","POST"])
def futureTrends():
	return render_template("future.html", PAGE_CONTENT = PAGE_CONTENT)

'''@app.route("/1999/", methods=["GET","POST"])
def ninetyNine():
	return render_template("1999.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2000/", methods=["GET","POST"])
def twoThousand():
	return render_template("2000.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2001/", methods=["GET","POST"])
def twoThousandOne():
	return render_template("2001.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2002/", methods=["GET","POST"])
def twoThousandTwo():
	return render_template("2002.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2003/", methods=["GET","POST"])
def twoThousandThree():
	return render_template("2003.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2004/", methods=["GET","POST"])
def twoThousandFour():
	return render_template("2004.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2005/", methods=["GET","POST"])
def twoThousandFive():
	return render_template("2005.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2006/", methods=["GET","POST"])
def twoThousandSix():
	return render_template("2006.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2007/", methods=["GET","POST"])
def twoThousandSeven():
	return render_template("2007.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2008/", methods=["GET","POST"])
def twoThousandEight():
	return render_template("2008.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2009/", methods=["GET","POST"])
def twoThousandNine():
	return render_template("2009.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2010/", methods=["GET","POST"])
def twoThousandTen():
	return render_template("2010.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2011/", methods=["GET","POST"])
def twoThousandEleven():
	return render_template("2011.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2012/", methods=["GET","POST"])
def twoThousandTwelve():
	return render_template("2012.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2013/", methods=["GET","POST"])
def twoThousandThirteen():
	return render_template("2013.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2014/", methods=["GET","POST"])
def twoThousandFourteen():
	return render_template("2014.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2015/", methods=["GET","POST"])
def twoThousandFifteen():
	return render_template("2015.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2016/", methods=["GET","POST"])
def twoThousandSixteen():
	return render_template("2016.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/2017/", methods=["GET","POST"])
def twoThousandSeventeen():
	return render_template("2017.html", PAGE_CONTENT = PAGE_CONTENT)'''

@app.route("/randomize/", methods=["GET","POST"])
def randomIMG():
	return render_template("random.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/dashboard/", methods=["GET","POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", APP_CONTENT = APP_CONTENT)

@app.route("/introduction-to-app/")
# @login_required
def intro_to_app():
    try:
        output = ['Digit 400 is good', 'Python, java, php, \C++', '<p><strong>Hello World!<strong><p>', 42,'42']

        return render_template("templating_demo.html", output = output)

    except Exception as e:
        return(str(e))
    

@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        c, conn = connection()
        if request.method == "POST":
            data = c.execute("SELECT * FROM users WHERE username = ('{0}')".format(thwart(request.form['username'])))

            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash("You are now logged in")
                return redirect(url_for("dashboard"))

            else:
                error = "Invalid credentials, try again."

        gc.collect()

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        error = "Invalid credentials, try again."
        return render_template("login.html", error = error)
    
    
@app.route('/search/', methods=['GET', 'POST'])
def searching():
    try:
        codeStuff = ''
        linkStuff = ''
        if request.method == "POST":
            stuff = request.form['search']
            codeStuff = search(stuff)
            linkStuff = link(stuff)

            return render_template("search.html", codeStuff = codeStuff, linkStuff = linkStuff,  PAGE_CONTENT = PAGE_CONTENT)

        return render_template("search.html", codeStuff = codeStuff, linkStuff = linkStuff, PAGE_CONTENT = PAGE_CONTENT)
    except Exception as e:
        return str(e)

'''@app.route('/uploads/', methods=['GET', 'POST'])
#@login_required
def upload_file():
    try:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('File upload successful')
                return render_template('uploads.html', filename = filename)
        return render_template('uploads.html')
    except:
        flash("Please upload a valid file")
        return render_template('uploads.html')
    return render_template('uploads.html')

@app.route('/download/')
def download():
    try:
        return send_file('/var/www/FlaskApp/FlaskApp/uploads/screencap.png', attachment_filename='screencap.png')
    except Exception as e:
        return str(e)

@app.route('/downloader/', methods=['GET', 'POST'])
#@login_required
def downloader():
    try:
        if request.method == "POST":
            filename = request.form['filename']
            return send_file('/var/www/FlaskApp/FlaskApp/uploads' + filename, attachment_filename = 'download')
        
        else:
            return render_template('downloader.html', error = error)
        error = "Please enter a valid file name"
        return render_template('downloader.html', error = error)
    
    except:
        error = "Please enter a valid file name"
        return render_template('downloader.html', error = error)'''

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice', [validators.Required()])
    

'''@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = ('{0}')".format(thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another.")
                return render_template('register.html', form = form)

            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES ('{0}','{1}','{2}','{3}')".format(thwart(username), thwart(password), thwart(email), thwart("/dashboard/")))

                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template("register.html", form = form)

    except Exception as e:
        return(str(e)) #remove for production
        
@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('main'))'''

@app.route("/updates/", methods=["GET","POST"])
def updates():
    return render_template("updates.html", PAGE_CONTENT = PAGE_CONTENT)

@app.route("/sitemap.xml/", methods=["GET","POST"])
def sitemap():
    try:
        pages = []
        week = (datetime.now() - timedelta(days = 7)).date().isoformat()
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and len(rule.arguments)==0:
                pages.append(
                    ["http://138.197.95.77"+str(rule.rule),week]
                )
        sitemap_xml = render_template('sitemap_template.xml', pages = pages)
        response = make_response(sitemap_xml)
        response.headers["Content-Type"] = "application/xml"
        return response
    except Exception as e:
        return(str(e))
    
@app.route('/robots.txt/')
def robots():
    #return("User-agent: *\nDisallow /") #Disallows all robot traffic
    return("User-agent: *\nDisallow: /register/\nDisallow: /login/") #Disallows robot traffic to sensitive urls

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):
    return render_template("405.html")

@app.errorhandler(500)
def int_server_error(e):
    return render_template("500.html", error = e)

if __name__ == "__main__":
	app.run()