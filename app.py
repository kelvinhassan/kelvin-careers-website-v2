from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nairobi, Kenya',
        'salary': 'Kes. 100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Nakuru, Kenya',
        'salary': 'Kes. 150,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'remote',

    },
    {
        'id': 1,
        'title': 'Backend Engineer',
        'location': 'San Fransisco, USA',
        'salary': 'USD. 120,000'
    },

]


@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS, company_name='kelvin')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
