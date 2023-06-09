import json


def get_data(opt) -> list:
    """Retrieves list of cordinates from json datasources, switches between 3 cities:
        - Djibouti (38 points)
        - Luxembourg (980 points)
        - Oma (1979 points)

    Args:
        opt (location option): value in [1,2,3]

    Returns:
        list[int]: list of cordinates [X,Y] 
    """
    if opt == 1:
        f = open('data/Djibouti.json')
    elif opt == 2:
        f = open('data/Luxembourg.json')
    else:
        f = open('data/Oma.json')

    data_arr = json.load(f)
    return data_arr
