import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#QUESTION ONE
def get_overdue_tasks():

	# Load tasks.csv into a DataFrame
	tasks_df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

	# Convert 'OverDue' column to boolean values
	tasks_df['OverDue'] = tasks_df['OverDue'].astype(bool)

	# Filter rows where tasks are overdue
	overdue_tasks = tasks_df[tasks_df['OverDue']]

	# Get the total number of overdue tasks
	total_overdue_tasks = len(overdue_tasks)

	# Print the result
	print(f'Total number of overdue tasks: {total_overdue_tasks}')

	return total_overdue_tasks

#Calling the function
#get_overdue_tasks()

#-----------------------------------------------------------------------------------

#QUESTION TWO
def get_task_group_status():

	# Load tasks.csv into a DataFrame
	tasks_df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

	# Group tasks by 'Task Group' and 'Report Status'
	grouped_tasks = tasks_df.groupby(['Task Group', 'Report Status']).size().unstack(fill_value=0)

	# Print the result
	print("Total number of tasks by Task Group:")
	print(grouped_tasks)

	return get_task_group_status

#Calling the function
#get_task_group_status()

#-----------------------------------------------------------------------------------

#QUESTION THREE
def get_open_and_closed():
	# Load tasks.csv into a DataFrame
	tasks_df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

	# Filter tasks for open and closed statuses
	open_tasks = tasks_df[tasks_df['Report Status'] == 'Open']
	closed_tasks = tasks_df[tasks_df['Report Status'] == 'Closed']

	# Group tasks by 'Task Group'
	grouped_open_tasks = open_tasks.groupby('Task Group').size()
	grouped_closed_tasks = closed_tasks.groupby('Task Group').size()

	# Create a DataFrame for the grouped data
	grouped_data = pd.DataFrame({'Open': grouped_open_tasks, 'Closed': grouped_closed_tasks})

	# Plotting the grouped bar graph
	grouped_data.plot(kind='bar', figsize=(12, 6))

	# Adding labels and title
	plt.xlabel('Task Group')
	plt.ylabel('Count')
	plt.title('Total Number of Open and Closed Tasks by Task Group')

	# Show the plot
	plt.show()
	return get_open_and_closed

#Calling the function
#get_open_and_closed()

#-----------------------------------------------------------------------------------

#QUESTION FOUR
def get_overdue_by_project():
	# Load Construction_Data_PM_Tasks_All_Projects.csv into a DataFrame
	tasks_df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

	# Convert 'OverDue' column to boolean values
	tasks_df['OverDue'] = tasks_df['OverDue'].astype(bool)

	# Group tasks by 'project' and sum the overdue tasks
	overdue_tasks_by_project = tasks_df.groupby('project')['OverDue'].sum()

	# Plotting the bar graph
	overdue_tasks_by_project.plot(kind='bar', figsize=(12, 6), color='coral')

	# Adding labels and title
	plt.xlabel('Project')
	plt.ylabel('Total Overdue Tasks')
	plt.title('Total Number of Overdue Tasks by Project')

	# Show the plot
	plt.show()
	return get_overdue_by_project

#Calling the function
#get_overdue_by_project()

#-----------------------------------------------------------------------------------

#QUESTION FIVE
def get_percentage_overdue():
	# Load Construction_Data_PM_Tasks_All_Projects.csv into a DataFrame
	tasks_df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

	# Convert 'OverDue' column to boolean values
	tasks_df['OverDue'] = tasks_df['OverDue'].astype(bool)

	# Group tasks by 'project' and calculate the percentage of overdue tasks
	overdue_percentage_by_project = tasks_df.groupby('project')['OverDue'].mean() * 100

	# Plotting the bar graph
	overdue_percentage_by_project.plot(kind='bar', figsize=(12, 6), color='skyblue')

	# Adding labels and title
	plt.xlabel('Project')
	plt.ylabel('Percentage of Overdue Tasks')
	plt.title('Percentage of Overdue Tasks by Project')

	# Show the plot
	plt.show()
	return get_percentage_overdue

#Calling the function
#get_percentage_overdue()

#-----------------------------------------------------------------------------------

#QUESTION SIX
def get_mean_days_elapsed():
	# Load Construction_Data_PM_Forms_All_Projects.csv into a DataFrame
	forms_df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

	# Convert 'Created' and 'Status Changed' columns to datetime objects
	forms_df['Created'] = pd.to_datetime(forms_df['Created'], errors='coerce')
	forms_df['Status Changed'] = pd.to_datetime(forms_df['Status Changed'], errors='coerce')

	# Calculate the number of days elapsed since forms were opened
	forms_df['DaysElapsed'] = (forms_df['Status Changed'] - forms_df['Created']).dt.days

	# Group forms by 'Project' and calculate the mean number of days elapsed
	mean_days_elapsed_by_project = forms_df.groupby('Project')['DaysElapsed'].mean()

	# Print the mean number of days elapsed by project
	print("Mean Number of Days Elapsed Since Forms Were Opened by Project:")
	print(mean_days_elapsed_by_project)
	return get_mean_days_elapsed

#Calling the function
#get_mean_days_elapsed()

#-----------------------------------------------------------------------------------

#QUESTION SEVEN
def get_open_form_by_type():
	# Load Construction_Data_PM_Forms_All_Projects.csv into a DataFrame
	forms_df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

	# Filter forms for open status
	open_forms = forms_df[forms_df['Report Forms Status'] == 'Open']

	# Group open forms by 'Type' and count the occurrences
	open_forms_by_type = open_forms.groupby('Type').size()

	# Plotting the bar chart
	open_forms_by_type.plot(kind='bar', figsize=(12, 6), color='green')

	# Adding labels and title
	plt.xlabel('Type of Form')
	plt.ylabel('Number of Open Forms')
	plt.title('Number of Open Forms by Type of Form')

	# Show the bar chart
	plt.show()
	return get_open_form_by_type

#Calling the function
#get_open_form_by_type()