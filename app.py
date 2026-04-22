import streamlit as st
import joblib
import pandas as pd

# =========================
# LOAD MODELS
# =========================
clf = joblib.load('artifacts/model_classification.pkl')
reg = joblib.load('artifacts/model_regression.pkl')


def main():
    st.title('🎓 Student Placement & Salary Prediction')

    st.subheader("Input Student Data")

    # =========================
    # INPUT FEATURES (SESUIKAN A.csv)
    # =========================
    cgpa = st.number_input("CGPA", 0.0, 10.0)
    twelfth_percentage = st.number_input("12th Percentage", 0.0, 100.0)
    backlogs = st.number_input("Backlogs", 0, 20)

    study_hours_per_day = st.number_input("Study Hours per Day", 0.0, 24.0)
    sleep_hours = st.number_input("Sleep Hours", 0.0, 24.0)
    attendance_percentage = st.number_input("Attendance %", 0.0, 100.0)

    projects_completed = st.number_input("Projects Completed", 0, 20)
    internships_completed = st.number_input("Internships Completed", 0, 10)

    coding_skill_rating = st.slider("Coding Skill Rating", 1, 10)
    communication_skill_rating = st.slider("Communication Skill Rating", 1, 10)
    aptitude_skill_rating = st.slider("Aptitude Skill Rating", 1, 10)

    hackathons_participated = st.number_input("Hackathons Participated", 0, 20)
    certifications_count = st.number_input("Certifications Count", 0, 20)

    extracurricular_involvement = st.selectbox(
        "Extracurricular Involvement",
        ["Yes", "No", "Unknown"]
    )

    # =========================
    # CREATE DATAFRAME
    # =========================
    data = {
        'cgpa': cgpa,
        'twelfth_percentage': twelfth_percentage,
        'backlogs': backlogs,
        'study_hours_per_day': study_hours_per_day,
        'attendance_percentage': attendance_percentage,
        'projects_completed': projects_completed,
        'internships_completed': internships_completed,
        'coding_skill_rating': coding_skill_rating,
        'communication_skill_rating': communication_skill_rating,
        'aptitude_skill_rating': aptitude_skill_rating,
        'hackathons_participated': hackathons_participated,
        'certifications_count': certifications_count,
        'sleep_hours': sleep_hours,
        'extracurricular_involvement': extracurricular_involvement
    }

    df = pd.DataFrame([data])

    # =========================
    # PREDICTION
    # =========================
    if st.button("Predict"):
        try:
            # classification
            pred_class = clf.predict(df)[0]
            placement = "Placed" if pred_class == 1 else "Not Placed"

            st.subheader("📊 Result")
            st.write(f"Placement Status: **{placement}**")

            # regression (conditional)
            if pred_class == 1:
                salary = reg.predict(df)[0]
                st.write(f"Estimated Salary: **{round(float(salary), 2)} LPA**")
            else:
                st.write("Estimated Salary: ❌ Not Applicable")

        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()