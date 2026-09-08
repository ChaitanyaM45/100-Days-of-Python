PLACEHOLDER="[name]"

with open(r"C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-024\Input\Names\invited_names.txt") as name_file:
    names=name_file.readlines()

with open(r"C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-024\Input\Letters\starting_letter.txt") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,name)

        with open(fr"C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-024\Output\ReadyToSend\letter_for_{name}.txt",mode="w") as output:
            output.write(new_letter)