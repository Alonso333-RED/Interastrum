from utils import sector_utils

def presentation():
    print("Interastrum")
    print("v1.0.0")

def main():
    presentation()

    universe = sector_utils.generate_universe()
    print(universe[0][0][0].faction_presence)

if __name__ == "__main__":
    main()