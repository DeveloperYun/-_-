import csv

def save_to_file(jobs):
    file = open("jobs.scv", mode="w")
    writer = csv.writer(file)
    writer .writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return