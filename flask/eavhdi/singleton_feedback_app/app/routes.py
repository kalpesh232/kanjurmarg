from flask import Blueprint, render_template, request
from .logger import Logger

main = Blueprint("main" , __name__)
logger = Logger()

@main.route("/", methods=["GET", "POST"])
def my_feedback():
    if request.method == "POST" :
        name = request.form.get("name")
        feedback = request.form.get("feedback")
        message = f"Thanks for feedback {name} : {feedback}"
        logger.log_text(message)
        return  f"Thanks for feedback {name} : {feedback}"
    return render_template("index.html")