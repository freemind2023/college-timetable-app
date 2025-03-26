import streamlit as st
import pandas as pd  # Use pandas to show data as tables

st.title("🎓 College Timetable Builder")

# ------------------- COLLEGE FORM -------------------
st.header("📋 Enter College Details")

with st.form("college_form"):
    college_name = st.text_input("College Name")
    department = st.text_input("Department")
    year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    semester = st.selectbox("Semester", ["Semester 1", "Semester 2", "Semester 3", "Semester 4",
                                         "Semester 5", "Semester 6", "Semester 7", "Semester 8"])
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"✅ Details Submitted! College: {college_name}, Dept: {department}, Year: {year}, Sem: {semester}")


# ------------------- SUBJECT FORM -------------------
st.header("📘 Add Subject & Teacher Info")

with st.form("subject_form"):
    subject = st.text_input("Enter Subject Name")
    teacher = st.text_input("Enter Teacher Name")
    hours = st.number_input("Hours per Week", min_value=1, max_value=10, step=1)

    submitted_subject = st.form_submit_button("Add Subject")

    if submitted_subject:
        st.success("✅ Subject added successfully!")

        df = pd.DataFrame({
            'Subject': [subject],
            'Teacher': [teacher],
            'Hours/Week': [hours]
        })

        st.write("📄 Subject Details Table:")
        st.dataframe(df)


# ------------------- TEACHER AVAILABILITY -------------------
st.header("🗓️ Teacher Availability")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
hours = ["9AM-10AM", "10AM-11AM", "11AM-12PM", "12PM-1PM", "2PM-3PM", "3PM-4PM"]

availability = {}

for day in days:
    with st.expander(day):
        availability[day] = {}
        for hour in hours:
            key = f"{day}_{hour}"
            availability[day][hour] = st.checkbox(f"{hour}", key=key)

st.subheader("✅ Selected Availability")
st.write(availability)
