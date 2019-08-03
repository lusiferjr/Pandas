import pandas as ps
"""Readng the given csv and putting NaN values in place of **"""
data=ps.read_csv('6153237444115dat.csv',na_values=['*', '**', '***', '****', '*****', '******'])


#PROBLEM FIRST
print("ANS OF FIRST PROBLEM")

"""- How many rows is there in the data?
- What are the column names?
- What are the datatypes of the columns?
- What is the mean Fahrenheit temperature in the data? (`TEMP` column)
- What is the standard deviation of the Maximum temperature? (`MAX` column)
- How many unique stations exists in the data? (`USAF` column)"""



print('Total no. of row:',data.__len__())
name=data.columns
print('Total columns ')
for i in name:
    print(i)
print('Datatypes:',data.dtypes)
print('mean od temp:',data['TEMP'].mean())
print('deviation of MAX:',data['MAX'].std())
print('unique',data['USAF'].unique())

#PROBLEM TWO
print("ANS OF SECOUND")
""" - Select from the `data` columns `USAF, YR--MODAHRMN, TEMP, MAX, MIN` and assign them into a new variable called `selected`
 - Remove all rows from `selected` that has NoData in column `TEMP` using `dropna()` -function
 - Convert the Fahrenheit temperatures from `TEMP` into a new column `Celsius` using the conversion formula
 - Round the values in `Celsius` to have 0 decimals (**don't** create a new column --> update the current one)
 - Convert the `Celsius` values into integers (**don't** create a new column --> update the current one)"""

selected=ps.concat([data['USAF'],data['YR--MODAHRMN'],data['TEMP'],data['MAX'],data['MIN']],axis=1)

selected=selected.dropna(subset=['TEMP'])

for i in selected['TEMP']:
    convert(i)


selected['Celsius']=a
b=selected['Celsius'].round()
selected.update(b)
a.clear()
for i in selected['Celsius']:
    a.append(int(i))
selected['Celsius']=a

print(selected)

#THIRD
print('ans of two')
"""- Divide the selection into two separate datasets:
  - Select all rows from `selected` DataFrame into variable called `kumpula` where the `USAF` code is `29980`
  - Select all rows from `selected` DataFrame into variable called `rovaniemi` where the `USAF` code is `28450`
- Save `kumpula` DataFrame into `Kumpula_temps_May_Aug_2017.csv` file (CSV format) 
   - separate the columns with `,`
   - use only 2 decimals in the floating point numbers
- Save `rovaniemi` DataFrame into `Rovaniemi_temps_May_Aug_2017.csv` file (CSV format) 
   - separate the columns with `,`
   - use only 2 decimals in the floating point numbers"""

kumpula=selected[selected['USAF']==29980]
rovaniemi=selected[selected['USAF']==28450]

kumpula.to_csv('Kumpula_temps_May_Aug_2017.csv',index=False,float_format='%.2f')
rovaniemi.to_csv('Rovaniemi_temps_May_Aug_2017.csv',index=False,float_format='%.2f')
#FORTH
print("ANS OF FORTH(part 1)")
"""**Part 1**

- What was the median temperature in:
  - Helsinki Kumpula?
  - Rovaniemi?"""
print(kumpula['TEMP'].median())
print(rovaniemi['TEMP'].median())
print("ANS OF FORTH(part 2)")
"""
- Select from `rovaniemi` and `kumpula` DataFrames such rows from the DataFrames where ``YR--MODAHRMN`` values are from May 2017 (see hints for help)
and assign them into variables `rovaniemi_may` and `kumpula_may`
- Do similar procedure for June and assign those values into variables `rovaniemi_june` and `kumpula_june`
- Using those new subsets print the mean, min and max temperatures for both places in May and June."""
rovaniemi_may=rovaniemi[rovaniemi['YR--MODAHRMN']//1000000==201705]
kumpula_may=kumpula[kumpula['YR--MODAHRMN']//1000000==201705]

rovaniemi_june=rovaniemi[rovaniemi['YR--MODAHRMN']//1000000==201706]
kumpula_june=kumpula[kumpula['YR--MODAHRMN']//1000000==201706]

print(kumpula_june['TEMP'].mean())
print(rovaniemi_june['TEMP'].mean())
print(kumpula_may['TEMP'].mean())
print(rovaniemi_may['TEMP'].mean())
#FIFTH
print("ANS OF FIFTH")
""" - create a new DataFrame where you have calculated mean, max and min temperatures for each day separately using the
  hourly values from Rovaniemi and Helsinki Kumpula.
  - this problem is a classical data aggregation problem"""
a.clear()
b=rovaniemi[['YR--MODAHRMN','TEMP']]
for i in b['YR--MODAHRMN']:
    a.append(i//100)
b['YR--MODAHRMN']=a
c=b.groupby('YR--MODAHRMN')
a.clear()
b=[]
ce=[]
h=[]
for x,y in c:
    a.append(y['TEMP'].mean())
    b.append(y['TEMP'].max())
    ce.append(y['TEMP'].min())
    h.append(x)
d=ps.DataFrame({
    'hour':h,
    'mean':a,
    'max':b,
    'min':ce
})
d
