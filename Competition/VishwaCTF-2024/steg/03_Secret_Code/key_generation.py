def generate_combinations():
    with open("possible_combinations.txt", "w") as file:
        for i in range(1000000):
            combination = str(i).zfill(6)  # Convert the number to a 6-digit string
            file.write(combination + '\n')

if __name__ == "__main__":
    generate_combinations()
