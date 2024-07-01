import pandas as pd

df = pd.read_json('C:/Users/student/Desktop/Plotly363/studentdashboard/pp3-4_2566_province.json')
df_change_province_name = pd.read_json("C:/Users/student/Desktop/Plotly363/studentdashboard/api_province.json")
df_thailand_location = pd.read_json("C:/Users/student/Desktop/Plotly363/studentdashboard/thailand.json")
result_dict = dict(zip(df_change_province_name['name_th'], df_change_province_name['name_en']))

