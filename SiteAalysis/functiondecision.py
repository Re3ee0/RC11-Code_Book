import csv
import pandas as pd

df = pd.read_csv("Plotdata.csv")
df['label'] = ''
for i in range(len(df)):
    if df['mediaFunction'][i] == "retail and other commercial":
        if df['urbanFunction'][i] == "retail and other commercial":
            df['label'][i] = "1"    
        elif df['urbanFunction'][i] == "integration and services":
            df['label'][i] = "2"    
        elif df['urbanFunction'][i] == "Business and_Professional Services":
            df['label'][i] = "3"    
        else:
            df['label'][i] = "4"        

    elif df['mediaFunction'][i] == "Business and_Professional Services":
        if df['urbanFunction'][i] == "retail and other commercial":
            df['label'][i] = "5"    
        elif df['urbanFunction'][i] == "integration and services":
            df['label'][i] = "6"    
        elif df['urbanFunction'][i] == "Business and_Professional Services":
            df['label'][i] = "7"    
        else:
            df['label'][i] = "8"        

    elif df['mediaFunction'][i] == "Arts and Entertainment":
        if df['urbanFunction'][i] == "retail and other commercial":
            df['label'][i] = "9"    
        elif df['urbanFunction'][i] == "integration and services":
            df['label'][i] = "10"    
        elif df['urbanFunction'][i] == "Business and_Professional Services":
            df['label'][i] = "11"    
        else:
            df['label'][i] = "12"        

    elif df['mediaFunction'][i] == "landmarks and outdoors":
        if df['urbanFunction'][i] == "retail and other commercial":
            df['label'][i] = "13"    
        elif df['urbanFunction'][i] == "integration and services":
            df['label'][i] = "14"    
        elif df['urbanFunction'][i] == "Business and_Professional Services":
            df['label'][i] = "15"    
        else:
            df['label'][i] = "16"                  
print(df)
