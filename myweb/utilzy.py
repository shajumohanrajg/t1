import pandas as pd
import requests
import json

# data_path1 = r"D:\SH\5-4-2024\thillai_v1\data\w (1).xlsx"
# data_path2 = r"D:\SH\5-4-2024\thillai_v1\data\07-05-2024 updatesheet.xlsx"
data_path3 = r"C:\Users\RAJKUMAR\Desktop\projectsrini\sh backup\sh backup\Data Fields\w (1).xlsx"

df = pd.read_excel(data_path3)
print(df.columns)

# print(df.count())

# df.drop("Father Name")

# df1 = df[["Name"],["Gender"]]


df1 = df[['name', 'gender', 'date_of_birth', 'time_of_birth', 'place_of_birth',
       'mother_tongue', 'marital_status', 'father_name','father_occupation',
       'mother_name','mother_occupation','no_of_brothers','no_of_married_brothers',
       'no_of_sisters','no_of_married_sisters',
       'height', 'weight', 'physical_status', 'body_type', 'complexion',
       'diet', 'educational_qualification', 'job', 'place_of_job',
       'income_per_month', 'religious', 'caste', 'gothra', 'lagnam', 'raasi',
       'star', 'dosha','raasi_chart','navamsam_chart']]

# new_df1 = df[['Profile_ID', 'Name', 'Gender', 'Date_of_Birth', 'Time_of_Birth',       
#        'Place_of_Birth', 'Mother_Tongue', 'Marital_Status', 'Father_Name',     
#        'Father_Occupation', 'Mother_Name', 'Mother_Occupation',
#        'No_of_Brothers', 'No_of_Married_Brothers', 'No_of_Sisters',
#        'No_of_Married_Sisters', 'Height', 'Weight', 'Physical_Status',        
#        'Body_Type', 'Complexion', 'Diet', 'Educational_Qualification', 'Job',  
#        'Place of Job', 'Income_per_month', 'Religion', 'Caste', 'Gothra', 'Lagnam',
#        'Raasi', 'Star', 'Dosha', 'Raasi Chart', 'Navamsam_Chart',
#        'Contact_Name', 'Phone_Number', 'Whatsapp_Number', 'Country', 'State',
#        'District', 'City'] 
       
#        ['Religion_find', 'Caste_find', 'Diet_find',
#        'Marital_Status_find', 'Educational_Qualification_find', 'Job_find',
#        'Income/month.1', 'Location', 'P1', 'P2', 'P3', 'P4'],]


# df1["time_of_birth"] = df1['time_of_birth'].apply(pd.Timestamp)
# print(type(df1.iloc[2].to_json()))

# to_json = json.loads(df1.iloc[2].to_json())
# print(type(df1.iloc[2].to_json()))
# print(type(to_json))
# print(df1['time_of_birth'])
# headers = ['content-type']


for r in range(50):

# res = requests.get('http://127.0.0.1:8000/api/persons/',headers={"Accept": "application/json"},)
    res = requests.post('http://thirukumaranmatrimony.com/api/person/', json.loads(df1.iloc[r].to_json()),headers={"Accept": "application/json"},)
    print(df1.iloc[r].to_json())
    print(type(df1.iloc[r].to_json()))
print("Done")