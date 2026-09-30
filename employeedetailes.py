import pandas as pd

df = pd.read_csv("employee.csv")

print("Employee Dataset:")
print(df)

average_salary = df["Salary"].mean()

print("\nAverage Salary:")
print(average_salary)

department_count = df["Department"].value_counts()

print("\nEmployee Count by Department:")
print(department_count)

threshold = 50000

high_salary_employees = df[df["Salary"] > threshold]

print("\nEmployees with Salary Above", threshold)
print(high_salary_employees)

high_salary_employees.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered employee data exported successfully!")
