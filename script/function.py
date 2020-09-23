print("hellow, future data scientist")
#corss group by pedestrain-severity
A_B=['PEDCOUNT','PEDCYLCOUNT', 'COLLISIONTYPE']
B_A=['PEDCYLCOUNT','PEDCOUNT','COLLISIONTYPE']

groupby_sort(A_B,B_A,90)

#corss group by cycle-severity

A_B=['PEDCYLCOUNT','SEVERITYCODE', 'COLLISIONTYPE']
B_A=['SEVERITYCODE', 'PEDCYLCOUNT','COLLISIONTYPE']

groupby_sort(A_B,B_A,90)

#chi-squre, p value, OR

#OR
oddsratio, pvalue = stats.fisher_exact(pv)
print("OddsR: ", oddsratio, "p-Value:", pvalue)

#pivot table
pv=df.pivot_table(values='INC_hour', index='SEVERITYCODE',columns='PEDCOUNT',aggfunc='count')
pv.rename(columns={0:'no',1:'yes'},index={0:'no injury',1:'injury'})

#chi-square
chi2,p_value,freedom_degree,expected_frequencies = stats.chi2_contingency(pv)
print("chi-square: ", chi2, "p-Value:", '{0:.40f}'.format(p_value) )
