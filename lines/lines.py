from sys import argv

def main():
    with open(f"{argv[1]}", "r") as file:
        for row in file:
            
