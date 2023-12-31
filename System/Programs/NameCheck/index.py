number_of_names = int(input("How many names are you comparing: "))
counter = 0
names = []

def compareletters(comparing, name):
    for comletters, nameletters in zip(comparing, name):
        if comletters == "*":
            pass

        elif comletters == nameletters:
            pass

        else:
            return False
    
    return True

def check_names(names):
    comparing = input("what are you comparing to: ")
    for name in names:
        if compareletters(comparing, name):
            print(f"{name}.Pass")

        else:
            print(f"{name}.Fail")

    return None

while counter < number_of_names:
    names.append(input(f"{counter + 1}."))
    counter+=1
check_names(names)
input("Press Enter to close")