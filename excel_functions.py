import pandas as pd

def write_data(q1, q2, q3, q4, q5):
	df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
	updated_df = df.append({'Question 1': q1, 'Question 2': q2, 'Question 3': q3, 'Question 4': q4, 'Question 5': q5}, ignore_index=True)
	updated_df.to_excel('data.xlsx', sheet_name="Sheet1")