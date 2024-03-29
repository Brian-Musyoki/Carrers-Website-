from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Data Analyst',
        'location': 'Nairobi, Kenya',
        'salary': '$50,000'
    },
     {
        'id': 2,
        'title':'Data Scientist',
        'location': 'Mombasa, Kenya',
        'salary': '$50,000'
    },
     {
        'id': 3,
        'title':'Frontend Engineer',
        'location': 'Remote',
        'salary': '$40,000'
    },
    {
        'id': 4,
        'title':'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)