from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["POST",'GET']) #added methods for handling the post request 
def index():
    note = request.form.get("note") # Changed request.args to request.form to received the form elements      
    if note:
        notes.append(note)
        return render_template("home.html", notes=notes)
        
if __name__ == '__main__':
    app.run(debug=True)
