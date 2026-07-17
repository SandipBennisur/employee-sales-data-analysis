import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import pandas as pd

data = {
    "Employee_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "Name": ["Emp1","Emp2","Emp3","Emp4","Emp5","Emp6","Emp7","Emp8","Emp9","Emp10"],
    "Department": ["Sales","HR","IT","Finance","Marketing","Sales","IT","HR","Finance","Marketing"],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"],
    "Age": [25,30,28,35,27,29,32,26,40,31],
    "Experience": [2,5,4,8,3,6,7,2,12,5],
    "City": ["Mumbai","Pune","Delhi","Bengaluru","Hyderabad","Chennai","Mumbai","Pune","Delhi","Bengaluru"],
    "Sales": [45000,52000,61000,70000,48000,56000,74000,43000,85000,60000],
    "Profit": [6000,7500,9200,12000,6800,8300,13000,5500,18000,9500],
    "salary": [38000,45000,52000,65000,42000,50000,70000,39000,82000,56000],
    "Rating": [4.2,4.5,4.8,4.6,4.1,4.3,4.9,4.0,4.7,4.4]
}

df = pd.DataFrame(data)
df.to_csv("employee_data.csv", index=False)
df=pd.read_csv("employee_data.csv")
print(df.head())
#check shap of data
print(df.shape)
#print columns name
print(df.columns)
#check the data types
print(df.dtypes)
#display the summery statistics of the data
print(df.describe())
# Find missing values.
print(df.isna())

# Fill missing Salary values with the average salary.
df["salary"]=df["salary"].fillna(df["salary"].mean())
print(df["salary"])

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print(df)

# Employees from the IT department.
IT_employees=df[df["Department"]=="IT"]
print(IT_employees)


# Employees with Salary > 60000.
high_salary=df[df['salary']>60000]
print(high_salary)


# Female employees from HR.
female_hr=df[(df["Department"]=="HR") & (df["Gender"]=="Female")]
print(female_hr)


# Employees with Experience > 5 years.
five_years_experience=df[df["Experience"]>5]
print(five_years_experience)

# Sort by Salary (descending).
df_sorted_salary=df.sort_values(by='salary',ascending=False)
print(df_sorted_salary)

# Sort by Sales and Profit.
df_sorted_sales_profit=df.sort_values(by=['Sales','Profit'])
print(df_sorted_sales_profit)

# Average Salary.
Average_salry=df["salary"].mean()
print(Average_salry)

# Highest Sales.
higest_sales=df['Sales'].max()
print(higest_sales)
# Total Profit.
total_profit=df['Profit'].sum()
print(total_profit)

# Average Rating by Department.
average_rating_by_dept=df.groupby('Department')['Rating'].mean()
print(average_rating_by_dept)

# Line chart of Sales.
plt.plot(df['Sales'],marker='o')
plt.title('Line Chart of Sales')
plt.xlabel('Employee Index')
plt.ylabel('Sales')
plt.savefig('line_chart_sales.png')  # Save the figure as a PNG file
plt.show()



# Line chart of Profit.
plt.plot(df['Profit'],marker='o')
plt.title('Line Chart of Profit')
plt.xlabel('Employee Index')
plt.ylabel('Profit')
plt.savefig('line_chart_profit.png')  # Save the figure as a PNG file
plt.show()


# Bar chart of average Salary by Department.
plt.bar(df['Department'],df['salary'])
plt.title('Bar Chart of Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.savefig('bar_chart_avg_salary.png')  # Save the figure as a PNG file
plt.show()


# Horizontal bar chart of Sales by City.
plt.barh(df['City'],df['Sales'])
plt.title
('Horizontal Bar Chart of Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.savefig('horizontal_bar_chart_sales_city.png')  # Save the figure as a PNG file
plt.show()


# Pie chart of Department distribution.
dept_count=df['Department'].value_counts()
plt.pie(dept_count,labels=dept_count.index,autopct='%1.1f%%')
plt.title('pie chart of Department Distribution')
plt.savefig('pie_chart_dept_distribution.png')  # Save the figure as a PNG file
plt.show()


# Histogram of Salary.
plt.hist(df["salary"],bins=6,color='green',edgecolor='black')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.savefig('histogram_salary.png')  # Save the figure as a PNG file
plt.show()

# Scatter plot of Sales vs Profit.
plt.scatter(df['Sales'],df['Profit'])
plt.title('Scatter Plot of Sales vs Profit')    
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.savefig('scatter_plot_sales_profit.png')  # Save the figure as a PNG file
plt.show()



# Scatter plot of Experience vs Salary.
plt.scatter(df['Experience'],df['salary'])
plt.title('Scatter Plot of Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.savefig('scatter_plot_experience_salary.png')  # Save the figure as a PNG file
plt.show()


# Customize chart with title, labels, legend, and grid.
plt.plot(df['Sales'],marker='o',label='Sales')

plt.legend()
plt.grid()
plt.show()


# Change figure size.
plt.figure(figsize=(10,6))

#export the cleaned csv filr
df.to_csv("cleaned_employee_data.csv", index=False)