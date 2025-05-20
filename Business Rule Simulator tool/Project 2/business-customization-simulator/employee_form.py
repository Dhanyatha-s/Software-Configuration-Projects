import streamlit as st

def get_employee_input():
    with st.expander("👤 Enter Employee Data"):
        role_level = st.selectbox("Role Level", ["Junior", "Mid", "Senior"])
        on_probation = st.checkbox("On Probation?", value=False)
        country = st.selectbox("Country", ["India", "Germany", "USA"])
        employment_type = st.radio("Employment Type", ["Full-time", "Contract"])
        department = st.selectbox("Department", ["Engineering", "HR", "Finance", "Sales"])
        rating = st.slider("Performance Rating", 1.0, 5.0, 3.5, 0.1)

        return {
            "role_level": role_level,
            "on_probation": on_probation,
            "country": country,
            "employment_type": employment_type,
            "department": department,
            "performance_rating": rating
        }
