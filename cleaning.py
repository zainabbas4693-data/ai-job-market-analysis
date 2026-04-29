import pandas as pd
#Loading data
job = pd.read_csv(r"Z:\Jobs Project\ai_jobs.csv")
skill = pd.read_csv(r"Z:\Jobs Project\skills_demand.csv")

#Removing duplicates
job.drop_duplicates()
skill.drop_duplicates()

#Checking NULL values
job=job.isnull().sum()
skill=skill.isnull().sum()

#Printing columns
print(job.info())
print(skill.info())