#encoding:utf-8
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlktqa import app
from  exts import db
from models import User,Question,Answer

manage=Manager(app)

#使用Migrate绑定app,db
migrate=Migrate(app,db)

#添加迁移脚本的命令到manage
manage.add_command('db',MigrateCommand)

if __name__=='__main__':
    manage.run()
