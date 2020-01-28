# REPORT.PY
#
# This file is responsible for printing the
# arboretum's collection of biomes and their
# inhabitants to the console.
#
# Author(s): Ken Boyd


import os


def build_facility_report(arboretum):
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """ +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n"""
    )

    biomes = ["coastlines", "forests", "grasslands", "mountains", "rivers", "swamps"]
    for biome_name in biomes:
        for arboretum_biome in arboretum.biomes[biome_name]:
            # check if there are entries in the plant or animal dictionaries
            if (
                len(arboretum_biome.animals.keys()) > 0
                or len(arboretum_biome.plants.keys()) > 0
            ):
                # combine the plant and animal dictionaries
                arboretum_biome_inhabitants = {
                    **arboretum_biome.animals,
                    **arboretum_biome.plants,
                }
                # print the biome name [with id], then join the result of a list comprehension that returns the quantity and name of each inhabitant
                print(
                    f"{arboretum_biome} ({', '.join(f'{len(arboretum_biome_inhabitants[inhabitant])} {inhabitant}' for inhabitant in arboretum_biome_inhabitants)})"
                )
    input("\n\nPress any key to continue...")
