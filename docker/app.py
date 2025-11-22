from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if not file:
            return "No file uploaded", 400

        # Load the CSV with pandas.read_csv.
        df = pd.read_csv(file)

        # Calculate average score per student.
        df["average"] = df[["Math", "Science", "English"]].mean(axis=1).round(2)

        # Find subject-wise topper (e.g., highest in Math).
        toppers = {}
        for subject in ["Math", "Science", "English"]:
            topper = df.loc[df[subject].idxmax()]
            toppers[subject] = f"{topper['Name']} ({topper[subject]})"

        # Add a new column Result → "Pass" if average ≥ 50 else "Fail".
        df["Result"] = np.where(df["average"] >= 50, "Pass", "Fail")
        result_count = df["Result"].value_counts().to_dict()

        # Group by "Result" and count how many students passed/failed. 
        result_count = df.groupby("Result")["StudentID"].count() 
        print("result_count : ", result_count)

        # Convert marks to NumPy array.
        marks = df[["Math", "Science", "English"]].to_numpy()
        # Compute overall mean, median, and standard deviation.
        stats = {
            "mean": round(np.mean(marks), 2),
            "median": round(np.median(marks), 2),
            "std": round(np.std(marks), 2)
        }

        # Normalize marks (scale between 0–1).
        normalized = ((marks - np.min(marks)) / (np.max(marks) - np.min(marks))).round(2)

        return render_template(
            "results.html",
            df=df.to_html(classes="table table-bordered", index=False),
            toppers=toppers,
            result_count=result_count,
            stats=stats,
            normalized=normalized
        )

    print("Hello, Docker!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
