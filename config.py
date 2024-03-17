import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

BOT_TOKEN = os.environ.get('BOT_TOKEN')
