import pandas as pd


salary=pd.read_excel("Data.xlsx",sheet_name="Salary")
print(salary.head())
print(salary.columns)

bonus=pd.read_excel("Data.xlsx",sheet_name="Bonus")
print(bonus.head())
print(bonus.columns)


salary_bonus=pd.merge(salary,bonus,how="inner",on="Department")

print(salary_bonus.head())


### Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. This command is convenient for testing just a part of a file.



salary_bonus.set_index('Department',inplace=True)
print(salary_bonus.head())



salary_bonus.loc[:,"share"]=salary_bonus.loc[:,"Contribution_Factor"]/salary_bonus.groupby(level=0)["Contribution_Factor"].transform(sum)
print(salary_bonus.head())



salary_bonus.loc[:,"salary_with_bonus"]=salary_bonus.loc[:,"Monthly_Base_Salary"]+salary_bonus.loc[:,"Bonus_Sum"]*salary_bonus.loc[:,"share"]

print(salary_bonus.head())
