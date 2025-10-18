import os
from dotenv import load_dotenv
from utils.TestDataGenerator import TestGenerateData as tgd
load_dotenv()

class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    NEW_NAME = tgd.random_string(5, True)