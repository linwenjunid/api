from app import create_app,db
from app.models.user import User
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from flask import jsonify

app=create_app()
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User)

manager.add_command('db',MigrateCommand)
manager.add_command('shell',Shell(make_context=make_shell_context))

@manager.command
def initAdmin():
    u=User()
    u.username='admin'
    u.password='123'
    u.email='example@example.com'
    db.session.add(u)
    db.session.commit()

if __name__=='__main__':
    manager.run()

