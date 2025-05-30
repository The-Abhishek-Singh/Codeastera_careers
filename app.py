from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id":
        1,
        "Title":
        "Data Analyst",
        "Location":
        "Bengaluru, India",
        "Salary":
        "Rs. 10,00,000",
        "Job Description":
        "Data Analyst is responsible for collecting, processing, and performing statistical analyses on data to help the organization make informed decisions. They may also create reports and visualizations to communicate findings to stakeholders."
    },
    {
        "id":
        2,
        "Title":
        "Data Scientist",
        "Location":
        "Delhi, India",
        "Salary":
        "Rs. 15,00,000",
        "Job Description":
        "Data Scientist is responsible for developing and implementing machine learning models and algorithms to extract insights from data. They may also work on data preprocessing, feature engineering, and model evaluation."
    },
    {
        "id":
        3,
        "Title":
        "Backend Engineer",
        "Location":
        "Remote",
        "Salary":
        "Rs. 20,00,000",
        "Job Description":
        "Backend Engineer is responsible for developing and maintaining the server-side components of web applications. They may work on databases, APIs, and other backend technologies to ensure smooth operation of the application."
    },
    {
        "id":
        4,
        "Title":
        "Machine Learning Engineer",
        "Location":
        "Pune, India",
        "Salary":
        "Rs. 25,00,000",
        "Job Description":
        "Machine Learning Engineer is responsible for designing, building, and deploying machine learning models and algorithms. They may also work on data preprocessing, feature engineering, and model evaluation."
    },
]


@app.route("/")
def hello():
    return render_template("Home.html", jobs=JOBS, company_name="CodeAstera")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
