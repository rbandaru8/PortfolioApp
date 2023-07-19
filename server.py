from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)

#writes data to database.txt file from the contact submission form.
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        msg = data["message"]
        subject = data["subject"]
        file = database.write(f'\n{email}, {msg}, {subject}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline ='') as database2:
        email = data["email"]
        msg = data["message"]
        subject = data["subject"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, msg, subject])
        

        
#decorator route. when the / is called, it will run this function hello world.  
 #by default the render_template looks in template folder.

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name+'.html')

@app.route("/submit_form", methods = ['POST', 'GET'])
def submit_form():
   # return 'form submitted succesffully horrray!'
   if request.method == 'POST':
    try: 
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou')
        #print(data)
    except:
        return 'did not save to database'
   else: 
    return 'something went wrong'



'''
@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')


@app.route("/<username>/<int:ID>")
def hello_world(username=None, ID = None):
   # return "<p>Hello, World test debug mode!</p>"
   return render_template('index.html', profilename=username, UserID = ID) 


@app.route("/blog")
def blog():
    return "These are my thoughts!"


@app.route("/favicon.ico")
def imagerender():
    return "These are my thoughts!"
'''