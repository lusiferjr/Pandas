import pandas as ps
# READ CSV
data=ps.read_csv('book.csv',na_values=[-9999])
#FIRST
"""  - The numerical values for rainfall and temperature read in as numbers
  - The second row of the datafile should be skipped, but the text labels for the columns should be from the first row
  - The no-data values should properly be converted to `NaN`"""
data=data.drop([0])
print(data)
#SECOND
"""- How many non-NaN values are there for `TAVG`?
- What about for `TMIN`?
- How many days total are covered by this data file?
- When is the first observation?
- When is the last?
- What was the average temperature of the whole data file (all years)?
- What was the `TMAX` temperature of the ``Summer 69`` (i.e. including months May, June, July, August of the year 1969)?"""

temp=data['TAVG'].isnull().sum()
print('total not nan values in TAVG:',data['TAVG'].__len__()-temp)
temp=data['TMIN'].isnull().sum()
print('total not nan values in TMIN:',data['TMIN'].__len__()-temp)
print('total days in data',data['DATE'].__len__())
print('First observation:',data['DATE'][1],'Last observation:',data['DATE'][data['DATE'].__len__()])
df=data.dropna(subset=['TAVG'])
d=[]
for i in df['TAVG']:
    d.append(int(i))
df=df.drop(['TAVG'],axis=1)
df.insert(6,'TAVG',d)
print('average temp is ',df['TAVG'].mean())
d.clear()
df2=data.dropna(subset=['TMAX'])
d=list(df2['TMAX'].astype(int))
df2=df2.drop(['TMAX'],axis=1)
df2.insert(7,'TMAX',d)
print(df2['DATE'])
tmax=df2['TMAX'].values
d.clear()
c=0
for i in df2['DATE']:
    if (i[:6]=='196905' or i[:6]=='196906' or i[:6]=='196907' or i[:6]=='196908'):
         d.append(tmax[c])
    c+=1
print('max value in TMAX in summer of 69',max(d))
#second
print("SECONDS")
"""1. Calculate the monthly average temperatures for the entire data file using the approach taught in the lecture.
2. Save the output to a new Pandas DataFrame called `monthlyData`.
3. Create a new column in the `monthlyData` DataFrame called `TempsC` that has the monthly temperatures in Celsius.
4. Upload the updated script to your repository for this week's exercise."""

#converting values in int
d=[]
data=data.dropna(subset=['TAVG'])
d=list(data['TAVG'].astype(int))
data=data.drop(['TAVG'],axis=1)
data.insert(7,'TAVG',d)

#converting in c
c=[]
def convert(a):
    c.append((a-32)*(5/9))
for i in data['TAVG']:
    convert(i)
data['TC']=c

#grouping
temp=[]
for i in data['DATE']:
    temp.append(i[:6])
data['mn']=temp
df=data.groupby('mn')

#doing monthly mean
mo=[]
me=[]
mf=[]
for i,j in df:
    mo.append(i)
    me.append(j['TC'].mean())
    mf.append(j['TAVG'].mean())

#creating dataframe
monthlyData=ps.DataFrame({
    'month':mo,
    'mean in c':me,
    'mean in f':mf
})
print(monthlyData)
#T#THIRD
print("third")
"""- You need to calculate a mean temperature *for each month* over the period 1952-1980 using the data in the data file.
   You should end up with 12 values, 1 mean temperature for each month in that period, and store them in a new Pandas DataFrame called `referenceTemps`.
   The columns in the new DataFrame should be titled `Month` and `avgTempsC`, or something similar.
   For example, your `referenceTemps` data should be something like that below, 1 value for each month of the year (12 total):
   
   | Month    | avgTempsC        |
   |----------|------------------|
   | January  | -5.350916        |
   | February | -5.941307        |
   | March    | -2.440364        |
   | ...      | ...              |
   
   Remember, these temperatures should be in degrees Celsius.

- Once you have the monthly mean values for each of the 12 months, you can then calculate a temperature anomaly for every month in the `monthlyData` DataFrame.
    The temperature anomaly we want to calculate is simply the temperature for one month in `monthlyData` minus the corresponding monthly average temperature from the `avgTempsC` column in the `referenceTemps` DataFrame.
    You should thus end up with a new column in the `monthlyData` DataFrame showing the temperature anomaly `Diff`, the difference in temperature for a given month (e.g., February 1960) compared to the average (e.g., for February 1952-1980).
- Upload the updated script to your repository for this week's exercise."""
temp.clear()
for i in monthlyData['month']:
    temp.append(i[:4])
monthlyData['ye']=temp
df=monthlyData.groupby('ye')
final_df=ps.DataFrame()
for i,j in df:
    if int(i) > 1951 and int(i) < 1981:
        final_df=ps.concat([final_df,j])

mo.clear()
for i in final_df['month']:
    mo.append(int(i[4:]))
final_df['mn']=mo
final_df=final_df.groupby('mn')
mo.clear()
me.clear()
mf.clear()
name=['','January','February','March','April','May','June','July','August','September','October','November','December']
for i,j in final_df:
    for k in j['mean in c']:
        mo.append(k)
    me.append(st.mean(mo))
    mf.append(name[int(i)])
df=ps.DataFrame({
    'month':mf,
    'average':me
})
print(df)
mo.clear()
mf.clear()
mf=monthlyData['mean in c'].values
me.clear()
c=0
for i in monthlyData['month']:
    mo.append(mf[c]-df.loc[int(i[4:])-1][1])
    c+=1
monthlyData['diff']=mo
monthlyData=monthlyData.drop('ye',axis=1)
print(monthlyData)

