from app import app #from app the folder, import app the package

@app.route('/')
@app.route('/index')
def index():
    return "Hello world?????" #return a String