import xmlrpc.client as client

hostname = 'localhost'
port = '8569'
db_name = 'o15-learn'
username = 'admin'
password = 'admin'

modelsession = 'openacademy.session'
modelcourse = 'openacademy.course'

root = f'http://{hostname}:{port}/xmlrpc/2/'
user_id = client.ServerProxy(root + 'common').login(db_name, username, password)
models = client.ServerProxy(f'{root}object')

# 1. search and read
if user_id:
    search_domain = []
    sessions_ids = models.execute_kw(db_name, user_id, password, modelsession, 'search', [search_domain])
    session_data = models.execute_kw(db_name, user_id, password, modelsession, 'read', [sessions_ids, ['name', 'number_seats']])
    for sdata in session_data:
        print(f'Session #{sdata["id"]};name={sdata["name"]};seats={sdata["number_seats"]}')
else:
    print("Can't read an info about sessions!")

# 2. create a new session
if user_id:
    search_domain = [('name','ilike','Изучение Flask')]
    course_id = models.execute_kw(db_name, user_id, password, modelcourse, 'search', [search_domain])[0]

    sdict = [{'name': 'Session 3', 'course': course_id, 'duration': 5}]
    session_id = models.execute_kw(db_name, user_id, password, modelsession, 'create', sdict)
    print("New session created")
else:
    print("Error encountered while session creating!")
