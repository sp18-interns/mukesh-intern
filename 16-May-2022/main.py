from Salary import Salary_account

sal = Salary_account('Mukesh', 500.0, 12.0, 24000.0)
# print(sal)


print('Dearness Allowance of this employee :', sal.da())
print('House Rent Allowance:', sal.hra())
print('Total Gross Salary:', sal.gross_salary())
print('Daily wage paid by the Company:', sal.daily_wage())
print('Income Tax paid by the Employee:', sal.incometax())
print('Provident fund saved by the Employee:', sal.providentFund())
print('Daily wage earn per hour by the Employee:', sal.wageperhour())
print('Overtime worked by the Employee:',sal.overtime())
print('***********************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++************************>')
