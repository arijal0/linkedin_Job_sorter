# predictive_analytics.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Sample dataset with job titles, locations, and salaries
# Ideally, you'd scrape historical job salary data for training this model
job_data = {
    'Job Title': ['Software Engineer', 'Data Scientist', 'Frontend Developer', 'Backend Developer'],
    'Location': ['California', 'Texas', 'New York', 'Florida'],
    'Salary': [120000, 115000, 110000, 105000],
    'Skills': ['Python, C++, AWS', 'Python, Machine Learning, SQL', 'JavaScript, React', 'Python, Node.js, SQL']
}
job_df = pd.DataFrame(job_data)

# Function to train and predict salary based on job title and location
def train_predict_salary_model():
    job_df['Job Title'] = pd.Categorical(job_df['Job Title']).codes
    job_df['Location'] = pd.Categorical(job_df['Location']).codes

    X = job_df[['Job Title', 'Location']]
    y = job_df['Salary']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

# Function to predict salary for a given job and location
def predict_salary(model, job_title_code, location_code):
    new_job = np.array([[job_title_code, location_code]])
    predicted_salary = model.predict(new_job)
    return predicted_salary
