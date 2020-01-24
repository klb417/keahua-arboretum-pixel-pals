def build_facility_report(arboretum):
    biomes = ["coastlines", "forests", "grasslands", "mountains", "rivers", "swamps"]
    for biome_category in biomes:
        for biome in arboretum.biomes[biome_category]:
            if len(biome.animals) > 0 or len(biome.plants) > 0:
                print(f"{biome.name} [{str(biome.id)[:8]}]")
                inhabitants = biome.plants + biome.animals
                for inhabitant in inhabitants:
                    print(f"    {inhabitant}")
                print("")

    input("\n\nPress any key to continue...")
