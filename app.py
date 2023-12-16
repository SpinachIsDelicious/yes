from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "gremlim" 
    age = "124234" 

    return render_template('index.html' , name = name , age = age)


@app.route("/father")
def father():

    name = "amongus"
    age = "40123" 

    return render_template('father.html' , name = name , age = age)

@app.route("/mother")
def mother():

    name = "fallgufs" 
    age = "322" 

    return render_template('mother.html' , name = name , age = age)

@app.route("/friend")
def friend():

    name = "impasta" 
    age = "super monkey" 

    return render_template('friend.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
