from fastapi import FastAPI
from pydantic import BaseModel
from ai import generate_career_response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="AI Career Copilot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request body structure
class StudentProfile(BaseModel):
    branch: str
    year: int
    skills: str
    interests: str
    strengths: str
    weaknesses: str


@app.post("/career-copilot")
def career_copilot(profile: StudentProfile):
    try:
        prompt = f"""
You are an AI career mentor for Indian engineering students.

Student Profile:
- Branch: {profile.branch}
- Year: {profile.year}
- Skills: {profile.skills}
- Interests: {profile.interests}
- Strengths: {profile.strengths}
- Weaknesses: {profile.weaknesses}

Output strictly in this format:

Career Paths:
1. <Role>: <1-line reason>
2. <Role>: <1-line reason>
3. <Role>: <1-line reason>

Skill Gaps:
- <gap 1>
- <gap 2>
- <gap 3>

3-Month Roadmap:
Month 1:
Month 2:
Month 3:

Keep it concise and beginner-friendly.
"""
        result = generate_career_response(prompt)
        return {
            "status": "success",
            "generated_by": "Gemini AI",
            "career_guidance": result
        }

    except Exception:
        return {
            "status": "error",
            "message": "Failed to generate career guidance"
        }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AI Career Copilot",
        "version": "1.0"
    }
