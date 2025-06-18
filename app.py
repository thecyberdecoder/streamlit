import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Biodata", layout="centered")

st.title("📋 ATS Employee Biodata")

# Session state to hold biodata
if "biodata" not in st.session_state:
    st.session_state.biodata = []

with st.form("biodata_form"):
    st.subheader("Enter Employee Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    department = st.selectbox("Department", ["HR", "Engineering", "Sales", "Marketing", "Finance", "Operations"])
    experience = st.slider("Years of Experience", 0, 40, 1)
    skills = st.text_area("Skills (comma-separated)")
    submitted = st.form_submit_button("Save")

    if submitted:
        if name and email:
            new_data = {
                "Name": name,
                "Email": email,
                "Department": department,
                "Experience": experience,
                "Skills": [s.strip() for s in skills.split(",") if s.strip()]
            }
            st.session_state.biodata.append(new_data)
            st.success("✅ Biodata saved successfully!")
        else:
            st.warning("⚠️ Please fill in required fields: Name and Email.")

# Display the saved biodata
if st.session_state.biodata:
    st.subheader("🗃️ Saved Biodata")
    df = pd.DataFrame(st.session_state.biodata)
    st.dataframe(df)
else:
    st.info("No biodata entered yet.")

