from pyairtable import Api
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")

api = Api(TOKEN)
table = api.table(BASE_ID, TABLE_NAME)

def insert_to_airtable(record):
    try:
        table.create(record)
        print("✅ Inserted:", record)
    except Exception as e:
        print("❌ Error inserting record:", e)