print("Program Started")
from src.database.connection import engine

try:
    with engine.connect() as connection:
        print("Connected Succesfully")
    
except Exception as e:
    print("Connection Failed")
    print(e)