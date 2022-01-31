from base64 import encode
from re import S
from django.template import engine
import xlsxwriter
import pandas as pd
from datetime import date
import pysrt as py
'''
print('starting')
xls=pd.ExcelFile('9EFC7C50.xlsx') # takes 5 minutes
print('test 2')
df1 = pd.read_excel(xls, 'Pending_Permits')
print(df1.head())
# takes 8 minutes

current_time = (date.today())
# create a list with sheet numbers you want to process
sheets = map(str,range(1,12))
    # for 6 files it took around 1 minute

# convert each sheet to csv and then read it using read_csv
df={}
from subprocess import call
excel='9EFC7C50.xlsx'
for sheet in sheets:
    csv = 'C:/Users/Roscoe/Python Folder/SQL_Alchemy/csv_files/' + sheet + '.csv' 
    call(['cscript.exe', 'C:/Users/Roscoe/Python Folder/SQL_Alchemy/ExcelToCsv1.vbs', excel, csv, sheet])
    df[sheet]=pd.read_csv(csv)
    print(df[sheet])
   
'''
    #write vbscript to file
vbscript="""if WScript.Arguments.Count < 3 Then
    WScript.Echo "Please specify the source and the destination files. Usage: ExcelToCsv2 <xls/xlsx source file> <csv destination file> <worksheet number (starts at 1)>"
    Wscript.Quit
End If

csv_format = 6

Set objFSO = CreateObject("Scripting.FileSystemObject")

src_file = objFSO.GetAbsolutePathName(Wscript.Arguments.Item(0))
dest_file = objFSO.GetAbsolutePathName(WScript.Arguments.Item(1))
worksheet_number = CInt(WScript.Arguments.Item(2))

Dim oExcel
Set oExcel = CreateObject("Excel.Application")

Dim oBook
Set oBook = oExcel.Workbooks.Open(src_file)
oBook.Worksheets(worksheet_number).Activate

oBook.SaveAs dest_file, csv_format

oBook.Close False
oExcel.Quit
""";

f = open('ExcelToCsv2.vbs', 'w+b')
f.write(vbscript.encode('utf-8'))
#f.write(vbscript.encode('utf-8'))
f.close()
