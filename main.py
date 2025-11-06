import streamlit as st
import requests

st.title("💼 Job Search AI Assistant")

# User Inputs
job_query = st.text_input("🔍 Enter job title", "Python Developer")

# New Filter Widgets
col1, col2, col3 = st.columns(3)
with col1:
    location = st.text_input("📍 Location", "Bangalore")
with col2:
    experience = st.selectbox("💼 Experience", ["Any", "Fresher", "1-3 years", "3-5 years", "5+ years"])
with col3:
    salary = st.text_input("💰 Min Salary (optional)", "5 LPA")

# Search Button
if st.button("Search Jobs"):
    st.write(f"Searching for **{job_query}** jobs in **{location}** ...")
    # Example: request to your Flask backend or directly scrape here
    jobs = [
        {"title": "Python Developer", "company": "TCS", "location": "Bangalore", "description": "3 years exp, 6 LPA", "link": "#"},
        {"title": "Data Analyst", "company": "Infosys", "location": "Chennai", "description": "2 years exp, 4 LPA", "link": "#"}
    ]

    # Apply simple filter logic
    filtered_jobs = [
        job for job in jobs
        if (location.lower() in job['location'].lower())
        and (experience == "Any" or experience.lower() in job['description'].lower())
        and (salary.lower() in job['description'].lower())
    ]

    if filtered_jobs:
        for job in filtered_jobs:
            st.subheader(job['title'])
            st.write(f"🏢 {job['company']} — 📍 {job['location']}")
            st.write(job['description'])
            st.markdown(f"[View Job]({job['link']})")
            st.divider()
    else:
        st.warning("No jobs found matching your filters.")
