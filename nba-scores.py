from requests import get
from pprint import PrettyPrinter
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.balldontlie.io/v1/"
API_KEY = os.getenv("API_KEY")

headers = {
    'Authorization': API_KEY
}
