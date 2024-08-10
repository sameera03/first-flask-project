from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static')

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
  },
  {
    "id": 2,
    "title": "Backend Developer",
    "location": "Delhi, India",
    "salary": "Rs. 8,00,000"
  },
  {
    "id": 3,
    "title": "Frontend Developer",
    "location": "Mumbai, India",
    
  },
  {
    "id": 4,
    "title": "Fullstack Developer",
    "location": "San Fransisco, USA",
    "salary": "$120,000"
  }
]

@app.route('/')
def hello_world():
  # return "Hello there"
  return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
