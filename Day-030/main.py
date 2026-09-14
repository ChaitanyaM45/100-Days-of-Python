# try:
#     file=open(file="./Day-030/data.txt")
#     a_dict={"key":"value",
#             "new_key":"new_value"}
#     print(a_dict['new_key'])

# except FileNotFoundError:
#     file=open(file="./Day-030/data.txt",mode="w")
#     file.write("something")

# except KeyError as error_msg:
#     print(f"No such {error_msg} found in dictonary")

# else:
#     content=file.read()
#     print(content)

# finally:
#     file.close()
#     print("File was Closed.")
height=float(input("Enter Your Height: "))
weight=float(input("Enter Your Weight: "))
if height>3:
    raise ValueError("The human height cannot be greater than 3 meters")
bmi=weight/height**2
print(bmi)
