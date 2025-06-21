from flask import Flask, render_template_string
import pyodbc

app = Flask(__name__)

server = 'serverlg.database.windows.net'
database = 'db14'
username = 'sqluser14'
password = 'Linkin14*'
driver = '{ODBC Driver 17 for SQL Server}'

# Cadena de conexión
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/')
def home():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("select * from [dbo].[Usuarios]")  # Ajusta el nombre de la tabla
        rows = cursor.fetchall()
        conn.close()

        html = "<h1>Datos desde Azure SQL</h1><table border='1'>"
        for row in rows:
            html += "<tr>" + "".join(f"<td>{col}</td>" for col in row) + "</tr>"
        html += "</table>"

        return render_template_string(html)

    except Exception as e:
        return f"<h2>Error al conectar: {e}</h2>"

if __name__ == '__main__':
    app.run(debug=True)










