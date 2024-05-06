from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Pretoria, South Africa",
    "salary": "R10, 000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Gauteng, South Africa",
    "salary": "R20, 000"
  },
  {
    "id": 3,
    "title": "Senior Developer",
    "location": "CapeTown, South Africa",
    "salary": "R50, 000"
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "Remote, USA Ohio",
    "salary": "$20, 000"
  }
]

@app.route("/")
def home():
  return render_template("home.html",jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
