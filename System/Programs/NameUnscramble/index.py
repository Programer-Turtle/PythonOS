import random

def checknames(name, rearanged_names):
    for rearangedname in rearanged_names:
        if name == rearangedname:
            return "pass"
        
    return "fail"

def rearange_name(scrambled_name, name, check_per_person):
    counter = 0
    rearanged_names = []
    while counter < check_per_person:
        rearanged_names.append("".join(random.sample(scrambled_name, len(scrambled_name))))
        counter+=1

    return checknames(name, rearanged_names)

def comparenames(possible_names, scrambled_name, check_per_person):
    for int, names in enumerate(possible_names, start=1):
        print(f"{int} {names}.{rearange_name(scrambled_name, names, check_per_person)}")
            

def main():
    #declares variable
    possible_names = []
    scrambled_name = input("Scrambled Name: ")
    numer_of_Posible_names = int(input("How many possible names: "))
    check_per_person = int(input("How many checks per person: "))
    counter = 0

    #updates the possible name list
    while counter < numer_of_Posible_names:
        possible_names.append(input(f"{counter + 1}."))
        counter+=1
    
    #Sends data to comparenames
    comparenames(possible_names, scrambled_name, check_per_person)


if __name__ == "__main__":
    main()

input("Press Enter to Exit")