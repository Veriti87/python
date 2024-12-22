from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список подарков</title>
</head>
<body>
    <h1>Список подарков</h1>
    <table border="1">
        <tr>
            <th>ФИО</th>
            <th>Подарок</th>
            <th>Стоимость</th>
            <th>Статус</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    conn = sqlite3.connect('Gifts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Gifts')
    data = c.fetchall()
    conn.close()

    return render_template_string(HTML_TEMPLATE, data=data)

if __name__ == '__main__':
    app.run(debug=True)