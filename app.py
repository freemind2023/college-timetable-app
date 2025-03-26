import streamlit as st

st.title("🎓 College Timetable Builder")
st.header("📋 Enter College Details")

# Form start
with st.form("college_form"):
    college_name = st.text_input("College Name")
    department = st.text_input("Department")
    year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    semester = st.selectbox("Semester", ["Semester 1", "Semester 2", "Semester 3", "Semester 4",
                                         "Semester 5", "Semester 6", "Semester 7", "Semester 8"])
    
    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"✅ Details Submitted! College: {college_name}, Dept: {department}, Year: {year}, Sem: {semester}")
