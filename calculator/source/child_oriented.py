from calculator.source.paldeck import dict_paldeck, unique_combos

def find_closest_element(target_value):
    closest_element = None
    min_difference = float('inf')  # Inicializa com infinito para garantir que a primeira diferença será menor

    for key, value in dict_paldeck.items():
        current_difference = abs(value['Power'] - target_value)

        if current_difference < min_difference or (current_difference == min_difference and value['Order'] < closest_element['Order']):
            closest_element = value
            min_difference = current_difference

    return closest_element

def get_index_by_name(name):
    for index, card_info in dict_paldeck.items():
        if card_info['Name'] == name:
            return index
    return None

def get_parent(child):
    
    if dict_paldeck[child]['Name'] in unique_combos:
        parents = unique_combos[dict_paldeck[child]['Name']].split('+')
        p1 = get_index_by_name(parents[0])
        p2 = get_index_by_name(parents[1])
        return dict_paldeck[p1], dict_paldeck[p2]
    
    duplas = []
    
    child_power = dict_paldeck[child]['Power']

    for key1, value1 in dict_paldeck.items():
        for key2, value2 in dict_paldeck.items():
            if key1 != key2:
                media = (value1['Power'] + value2['Power']) / 2
                closest = find_closest_element(media)
                if  closest['Power'] == child_power:
                    duplas.append((key1, key2))

    return duplas

print(get_parent(103))