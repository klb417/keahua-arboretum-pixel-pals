def build_facility_report(arboretum):
    biomes = ["coastlines", "forests", "grasslands", "mountains", "rivers", "swamps"]
    for biome_category in biomes:
        print(biome_category.capitalize())
        for biome in arboretum.biomes[biome_category]:
            print(f"  {biome.name} [{str(biome.id)[:8]}]")
        print("")

    input("\n\nPress any key to continue...")
