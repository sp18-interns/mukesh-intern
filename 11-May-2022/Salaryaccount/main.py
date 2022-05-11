from Salary import Salary_account

sal = Salary_account('Mukesh', 500.0, 12.0, 24000.0)
# print(sal)


print('Dearness Allowance of this employee :', sal.DA())
print('House Rent Allowance:', sal.HRA())
print('Total Gross Salary:', sal.Gross_salary())
print('Daily wage paid by the Company:', sal.Daily_wage())
print('Income Tax paid by the Employee:', sal.Incometax())
print('Provident fund saved by the Employee:', sal.ProvidentFund())
print('Daily wage earn per hour by the Employee:', sal.Wageperhour())
print('***********************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++************************>')
