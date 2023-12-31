import random
names = []

def ScrambleName(name):
    shuffledname = "".join(random.sample(name, len(name)))
    return shuffledname


def main(names):
    counter = 0
    number_of_names = int(input("How many names: "))
    while counter < number_of_names:
        names.append(input(f"{counter + 1}."))
        counter+=1

    print('Scrabled Names')
    for id, name in enumerate(names, start=1):
        print(f"{id}.{ScrambleName(name)}")

if __name__ == "__main__":
    main(names)

input("Press Enter to Exit")