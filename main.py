# main.py
import scraping
import resume_parsing
import skill_matching
import location_filtering
import predictive_analytics
import dashboard

# Web scraping for jobs
driver = scraping.get_driver()
scraping.linkedin_login(driver, 'ankitrijal432@gmail.com', '@nkiT9704')
jobs_df = scraping.scrape_linkedin_jobs(driver, 'Computer Science intern', 'Remote')

# Resume parsing
resume_text = resume_parsing.extract_text_from_pdf('resume.pdf')
user_skills = resume_parsing.extract_skills_from_resume(resume_text)

# Skill matching

job_descriptions = jobs_df['Job Description'].tolist()
jobs_df['Match Score'] = skill_matching.match_skills(user_skills, job_descriptions)

# Add location coordinates and visualize jobs
jobs_df = location_filtering.add_coordinates(jobs_df)
location_filtering.visualize_job_locations(jobs_df)

# Train predictive salary model
salary_model = predictive_analytics.train_predict_salary_model()

# Run the Dash dashboard
dashboard.create_dashboard(jobs_df)
