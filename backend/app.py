from flask import Flask, request, jsonify
from resume_parser import extract_skills
from job_matcher import match_jobs

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_text = request.json.get("resume")
    skills = extract_skills(resume_text)
    jobs = match_jobs(skills)
    return jsonify({
        "skills": skills,
        "recommended_jobs": jobs
    })

if __name__ == "__main__":
    app.run(debug=True)
