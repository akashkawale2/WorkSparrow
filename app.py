from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'company': 'Amazon',
    'location': 'Bengluru, India',
    'salary': 'Rs. 7,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'company': 'TCS',
    'location': 'Delhi, India',
    'salary': 'Rs. 9,00,000'
  },
  {
    'id': 3,
    'title': 'Full Stack Engineer',
    'company': 'Wipro',
    'location': 'Mumbai, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'company': 'Infosys',
    'location': 'Mumbai, India',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 5,
    'title': 'Frontend Engineer',
    'company': 'Fyle',
    'location': 'Remote',
    'salary': 'Rs. 8,00,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
