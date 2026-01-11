import csv

def match_jobs(skills):
    matched_jobs = []

    with open("dataset/jobs.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            job_skills = row["skills"].lower().split(",")
            score = len(set(skills) & set(job_skills))
            if score > 0:
                matched_jobs.append({
                    "role": row["role"],
                    "match_score": score
                })

    return matched_jobs
