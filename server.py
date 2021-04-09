from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

app.secret_key = "form data"

# index route will handle rendering form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form_fields' ,methods=['POST']) 
def form_fields():
    print(request.form['name'])
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    return redirect('/users')

@app.route('/users', methods=['GET'])
def users():
    if "name" not in session:
        return redirect('/')
    user_info = {
        "name" : session['name'],
        "dojo_location" : session['dojo_location'],
        "fav_language" : session['fav_language'],
        "comments" : session['comments'],
    }
    return render_template("users.html", user=user_info )
    
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)