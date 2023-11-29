from flask import Blueprint
print(__name__)
neosoft_blueprint = Blueprint('neosoft_blueprint', __name__)

@neosoft_blueprint.route('/')
def home():
    return "This is an example home blueprint"