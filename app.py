import streamlit as st
import pandas as pd

from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from agents.interview_agent import generate_questions

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.subheader("AI Internship Recommendation System")

# -----------------------------
# User Inputs
# -----------------------------
name = st.text_input("Enter Your Name")

resume = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

# -----------------------------
# Internship Recommendation Function
# -----------------------------
def recommend_internships(user_skills):

    df = pd.read_csv("data/internships.csv")

    recommendations = []

    for _, row in df.iterrows():

        required_skills = [skill.strip() for skill in row["Skills"].split(",")]

        matched = len(set(user_skills).intersection(required_skills))

        score = (matched / len(required_skills)) * 100

        recommendations.append({
            "Company": row["Company"],
            "Role": row["Role"],
            "Match": round(score, 2),
            "Apply_Link": row["Apply_Link"]
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["Match"],
        reverse=True
    )

    return recommendations


# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit"):

    if name and resume:

        st.success("✅ Resume Uploaded Successfully!")

        # -----------------------------
        # Read Resume
        # -----------------------------
        resume_text = extract_text(resume)

        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=250
        )

        # -----------------------------
        # Extract Skills
        # -----------------------------
        skills = extract_skills(resume_text)

        st.subheader("🛠 Skills Found")

        st.write(skills)

        # -----------------------------
        # Internship Recommendation
        # -----------------------------
        internships = recommend_internships(skills)

        st.subheader("🎯 Recommended Internships")

        for internship in internships:

            st.markdown(f"### 🏢 {internship['Company']}")

            st.write(f"**Role:** {internship['Role']}")

            st.write(f"**Match Score:** {internship['Match']} %")

            st.progress(int(internship["Match"]))

            st.link_button(
                "🚀 Apply Now",
                internship["Apply_Link"]
            )

            st.divider()

        # -----------------------------
        # Interview Preparation Agent
        # -----------------------------
        questions = generate_questions(skills)

        st.subheader("🎤 Interview Preparation")

        for q in questions:
            st.write("•", q)

    else:

        st.warning("⚠ Please enter your name and upload your resume.")