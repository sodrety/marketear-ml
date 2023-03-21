from flask import Flask
# from dotenv import load_dotenv
from api.api import api
from logging import FileHandler,WARNING

# load_dotenv()

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

if __name__ == '__main__':
    app.run(debug=True)