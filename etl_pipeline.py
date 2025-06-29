from remoteok_extract import fetch_remoteok_jobs
from airtable_connect import insert_to_airtable

def run_etl():
    jobs = fetch_remoteok_jobs()
    print(f"🟡 Inserting {len(jobs)} jobs into Airtable...\n")
    
    for job in jobs:
        insert_to_airtable(job)

run_etl()