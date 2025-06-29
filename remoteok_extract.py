import requests

def fetch_remoteok_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}  # Required by RemoteOK
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        jobs = response.json()[1:]  # First item is metadata
        cleaned_jobs = []

        for job in jobs[:10]:  # Limit to first 10 for testing
            cleaned_jobs.append({
                "Job Title": job.get("position"),
                "Company Name": job.get("company"),
                "Location": job.get("location") or "Remote",
                "Job Type": "Full-time",  # Placeholder (RemoteOK doesn't always list it)
                "Job URL": job.get("url"),
                "Posted Date": job.get("date", "").split("T")[0]  # ISO format
            })

        return cleaned_jobs
    else:
        print("❌ Failed to fetch jobs. Status:", response.status_code)
        return []

# Preview output
if __name__ == "__main__":
    jobs = fetch_remoteok_jobs()
    for job in jobs:
        print(job)