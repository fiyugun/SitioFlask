from  flask import Flask, render_template
#Este Comentario es de un programador de Japon
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

