# Function for returning list of biomes a selected plant can be added to
def get_plant_biomes(plant, arboretum):
    '''Function that returns a list of biomes in an arboretum that
    match the requirements of a given plant.

    ARGUMENTS:
    plant (object)
    arboretum (object)
    '''
    plant_biomes = []

    allowed_biomes = plant.required_locations
    all_biomes = arboretum.biomes
    for biome in allowed_biomes:
        for key, value in all_biomes.items():
            if key == biome:
                # add biomes to plant_biomes
                plant_biomes.extend(all_biomes[key])
            
    return plant_biomes