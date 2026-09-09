import pandas as pd

df=pd.read_csv("./Day-025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirell=df[df['Primary Fur Color']=="Gray"]
cinnamon_squirell=df[df['Primary Fur Color']=="Cinnamon"]
black_squirell=df[df['Primary Fur Color']=="Black"]

new_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[len(grey_squirell),len(cinnamon_squirell),len(black_squirell)]
}

data_frame=pd.DataFrame(new_dict)
data_frame.to_csv("./Day-025/Pandas Tutorial/squirell_count.csv")


# import pandas as pd
# import numpy as np

# df=pd.read_csv("./Day-025/Pandas Tutorial/weather_data.csv")
# print(df)

# avg=np.mean(df['temp'])
# max=df['temp'].max()
# print(avg)
# print("Avg: ",df['temp'].mean())
# print("Max: ",df['temp'].max())

# print("\n\n\nPrint Row:\n",df[df['day']=="Monday"])
# print("\n\n\nPrint Row where temp is Max:\n",df[df['temp']==max])

# print("\n\n\n")
# monday=df[df['day']=="Monday"]
# print(monday.condition)
# monday_temp_in_F=(monday.temp[0]*9/5)+32
# print(f"Temp in C: {monday.temp[0]}\nTemp in F: {monday_temp_in_F}")

# #create data from scractch
# data_dict={
#     "student":["rohit","pranav","chaitanya"],
#     "score":[95,98,80]
# }

# data_frame=pd.DataFrame(data_dict)
# data_frame.to_csv("./Day-025/Pandas Tutorialstudent.csv")
# print(data_frame)
# # with open("./Day-025/Pandas Tutorial/weather_data.csv") as data_file:
# #     data=data_file.readlines()
# #     print(data)

# # o/p:-
# # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# # import csv

# # with open("./Day-025/Pandas Tutorial/weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     for row in data:
# #         print(row)

# # o/p:
# # ['day', 'temp', 'condition']
# # ['Monday', '12', 'Sunny']
# # ['Tuesday', '14', 'Rain']
# # ['Wednesday', '15', 'Rain']
# # ['Thursday', '14', 'Cloudy']
# # ['Friday', '21', 'Sunny']
# # ['Saturday', '22', 'Sunny']
# # ['Sunday', '24', 'Sunny']
