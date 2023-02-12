import os
SECRET_KEY = "-_1'73GtB|t1vi\\ry@iv<Bf;"

FB_APP_ID = 1200420960103822

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')