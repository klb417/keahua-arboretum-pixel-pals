def build_facility_report(arboretum):
    biomes = ["coastlines", "forests", "grasslands", "mountains", "rivers", "swamps"]
    for biome_name in biomes:
        for arboretum_biome in arboretum.biomes[biome_name]:
            if (
                len(arboretum_biome.animals.keys()) > 0
                or len(arboretum_biome.plants.keys()) > 0
            ):
                arboretum_biome_inhabitants = {
                    **arboretum_biome.animals,
                    **arboretum_biome.plants,
                }
                print(
                    f"{arboretum_biome.name} ({', '.join(f'{len(arboretum_biome_inhabitants[inhabitant])} {inhabitant}' for inhabitant in arboretum_biome_inhabitants)})"
                )
    input("\n\nPress any key to continue...")
