<<<<<<< HEAD
from  flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)



=======
from  flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",Nombre="Carlos")


if __name__ == '__main__':
    app.run(debug=True)













>>>>>>> a229e18 (Hemos Agregado una variable nombre carlos)
