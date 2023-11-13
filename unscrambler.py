name = sorted(list(input("Name: ").strip()))

with open("pokemon.txt", "r") as file:
    line = file.readline()
    while line:
        chars = sorted(list(line.strip()))
        if chars == name:
            print(line)
        line = file.readline()