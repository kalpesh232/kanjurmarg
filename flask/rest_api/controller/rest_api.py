# $env:FLASK_ENV="development"
# $env:PYTHONDONTWRITEBYTECODE=1 ----------- to avoid oychache files
# $env:FLASK_APP = "app"
# __all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
from app import app
@app.route('/home')
def home():
    return "home"