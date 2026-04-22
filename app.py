import streamlit as st
import joblib
import pandas as pd


clf = joblib.load('model_classification.pkl')
reg = joblib.load('model_regression.pkl')


def main():
    st.set_page_config(page_title="Student Prediction", layout="wide")

st.title("🎓 Student Placement & Salary Prediction")

# ===== SIDEBAR =====
st.sidebar.header("📌 About")
st.sidebar.write("Input data mahasiswa untuk prediksi placement dan salary.")

# ===== FORM =====
with st.form("input_form"):

    st.subheader("📊 Academic Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        cgpa = st.number_input("CGPA", 0.0, 10.0)
        twelfth_percentage = st.number_input("12th Percentage", 0.0, 100.0)
        backlogs = st.number_input("Backlogs", 0, 20)

    with col2:
        study_hours_per_day = st.number_input("Study Hours per Day", 0.0, 24.0)
        sleep_hours = st.number_input("Sleep Hours", 0.0, 24.0)
        attendance_percentage = st.number_input("Attendance %", 0.0, 100.0)

    with col3:
        projects_completed = st.number_input("Projects Completed", 0, 20)
        internships_completed = st.number_input("Internships Completed", 0, 10)
        stress_level = st.number_input("Stress Level", 0, 10)

    st.subheader("💡 Skills")
    col4, col5, col6 = st.columns(3)

    with col4:
        coding_skill_rating = st.slider("Coding Skill", 1, 10)

    with col5:
        communication_skill_rating = st.slider("Communication Skill", 1, 10)

    with col6:
        aptitude_skill_rating = st.slider("Aptitude Skill", 1, 10)

    st.subheader("🏆 Activities")
    col7, col8 = st.columns(2)

    with col7:
        hackathons_participated = st.number_input("Hackathons", 0, 20)

    with col8:
        certifications_count = st.number_input("Certifications", 0, 20)

    st.subheader("👤 Personal Information")
    col9, col10, col11 = st.columns(3)

    with col9:
        gender = st.selectbox("Gender", ["Male", "Female"])
        branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "CE", "Other"])

    with col10:
        city_tier = st.selectbox("City Tier", ["Tier 1", "Tier 2", "Tier 3"])
        internet_access = st.selectbox("Internet Access", ["Yes", "No"])

    with col11:
        family_income_level = st.selectbox("Family Income", ["Low", "Medium", "High"])
        part_time_job = st.selectbox("Part Time Job", ["Yes", "No"])

    extracurricular_involvement = st.selectbox(
        "Extracurricular Involvement",
        ["Yes", "No", "Unknown"]
    )

    submit = st.form_submit_button("🚀 Predict")

    data = {
        "cgpa": cgpa,
        "twelfth_percentage": twelfth_percentage,
        "backlogs": backlogs,
        "study_hours_per_day": study_hours_per_day,
        "attendance_percentage": attendance_percentage,
        "projects_completed": projects_completed,
        "internships_completed": internships_completed,
        "coding_skill_rating": coding_skill_rating,
        "communication_skill_rating": communication_skill_rating,
        "aptitude_skill_rating": aptitude_skill_rating,
        "hackathons_participated": hackathons_participated,
        "certifications_count": certifications_count,
        "sleep_hours": sleep_hours,
        "extracurricular_involvement": extracurricular_involvement,
        "gender": gender,
        "branch": branch,
        "city_tier": city_tier,
        "internet_access": internet_access,
        "family_income_level": family_income_level,
        "part_time_job": part_time_job,
        "stress_level": stress_level
    }

    df = pd.DataFrame([data])

if __name__ == "__main__":
    main()
