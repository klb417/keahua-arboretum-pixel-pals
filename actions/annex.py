import os
from arboretum import Arboretum
from biome import River, Forest, Grassland

# Function for adding a biome to the arboretum
def annex_biome(arboretum):

    # Clears the terminal of previous contents
    os.system("cls" if os.name == "nt" else "clear")

    # Printing menu options to the console
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

    # Capturing user input and assigning it to "choice" variable
    choice = input("Choose biome to annex > ")

    # if statements check user input, when it evaluates to true the selected biome list is appended in arboretum dictionary
    if choice == "1":
        # mountain = Mountain()
        # arboretum.mountains.append(mountain)
        pass
    if choice == "2":
        # swamp = Swamp()
        # arboretum.swamps.append(swamp)
        pass
    if choice == "3":
        grassland = Grassland("Grassland")
        arboretum.grasslands.append(grassland)
    if choice == "4":
        forest = Forest("Forest")
        arboretum.forests.append(forest)
    if choice == "5":
        river = River("River")
        arboretum.rivers.append(river)
    if choice == "6":
        # coastline = Coastline()
        # arboretum.coastlines.append(coastline)
        pass