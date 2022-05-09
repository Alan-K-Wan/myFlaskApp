from flask import render_template #allows you to return files instead of strings

from app import app #from app the folder, import app the package

@app.route('/')
@app.route('/index')
def index():

    user = {
        'username':"Alan"
    }

    employees = [
        {
            'id':"696969",
            'name':{'first':"Alan", 'last':"Wan"},
            'role':"ICT Intern"
        },
        {
            'id':"420420",
            'name':{'first':"Haydn", 'last':"Dungey"},
            'role':"Helpdesk Officer"
        },
        {
            'id':"199232",
            'name':{'first':"Lachlan", 'last':"Couldrige"},
            'role':"Helpdesk Officer"
        },
        {
            'id':"000291",
            'name':{'first':"Jeremy", 'last':"Warnock"},
            'role':"Manager of Networks and Communications Technology"
        }
    ]
    return render_template('index.html', user=user, title="Alan's Flask App", employees=employees) #return a String or file using render_template()