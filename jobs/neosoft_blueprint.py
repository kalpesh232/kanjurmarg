from flask import Blueprint
print(__name__)
neosoft_blueprint = Blueprint('neosoft_blueprint1', __name__)

@neosoft_blueprint.route('/')
def home():
    return "This is an example home blueprint"