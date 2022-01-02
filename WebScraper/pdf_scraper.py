import tabula
import pandas as pd
import fitz as pdf
# I can just do the historical data then set the current data 
# For date I need to take the column data

Document ="rwservlet.pdf"
doc = pdf.open(Document)
n = len(doc)

# [top,left,bottom,width]
# width starts at the beginnning everytime
#%%
top = 1.15
bottom = 8.0
Date = [.5,3.65,.9,5.5]
county = [top,0.28,bottom,1.07]
Sec_Twp_Rng = [top,1.20,bottom,2]
Company = [top,2,bottom,4.2]
Well = [top,4.2,bottom,5.9]
Location = [top,5.9,bottom,8.2]
Type = [top,8.2,bottom,8.7]
Permit_Number = [top,8.6,bottom,9.1]
API_Number = [top,9.1,bottom,11] 
Objective = [top,10,bottom,11]
fc = 72 # unit converter

# Interats row by row
#%% 
for i in range(0,len(county)):
    Date[i] *= fc
    county[i] *= fc
    Sec_Twp_Rng[i] *= fc
    Company[i] *= fc
    Well[i] *= fc
    Location[i] *= fc
    Type[i] *= fc
    Permit_Number[i] *= fc
    API_Number[i] *= fc
    Objective[i] *= fc

# empty lists
#%%
df_county =[]
df_Sec_Twp_Rng=[]
df_Company    =[]
df_Well = []
df_Location = []
df_Type     = []
df_Permit_Number= []
df_API_Number_objective   = []
df_Objective    = []
columns =[0,1,2,3,4,5,6,7,8]
# capturing the information
#%%
for page in range(0,1):  
    df_Date = tabula.read_pdf("rwservlet.pdf", pages=1,area = Date,multiple_tables = True)
    df_county =(tabula.read_pdf("rwservlet.pdf", pages=1,area = [county],pandas_options ={'header':None}))
    df_Sec_Twp_Rng =(tabula.read_pdf("rwservlet.pdf", pages=1,area = [Sec_Twp_Rng],pandas_options ={'header':None}))
    df_Company += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Company])
    df_Well += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Well])
    df_Location += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Location])
    df_Type += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Type])
    df_Permit_Number += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Permit_Number])
 #    df_others could just make it 2 tables
    df_API_Number_objective += tabula.read_pdf("rwservlet.pdf", pages=1,area = [API_Number])
 #   df_Objective += tabula.read_pdf("rwservlet.pdf", pages=1,area = [Objective])

# use the pandas create dataframe from list

# printing data
#%%     
df=df_county+df_Sec_Twp_Rng
print(df_API_Number_objective)
#df.to_csv('output_test.csv')

