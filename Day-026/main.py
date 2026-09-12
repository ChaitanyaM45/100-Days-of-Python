import pandas as pd
df=pd.read_csv("./Day-026/nato_phonetic_alphabet.csv")

new_dict={
    row.letter:row.code for (index,row) in df.iterrows()
}
name=input("Enter Word: ").upper()
output_list=[new_dict[letter] for letter in name]
print(output_list)