# Приложение по поиску постов

## Приложение на Flask

***
Приложение позволяет загружать посты и находить существующие посты в приложении
***

* loader
* main

'''

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['POST_PATH'] = POST_PATH

'''