from calculator.source.paldeck import dict_paldeck

def find_closest_element(target_value):
    closest_element = None
    min_difference = float('inf')  # Inicializa com infinito para garantir que a primeira diferença será menor

    for key, value in dict_paldeck.items():
        current_difference = abs(value['Power'] - target_value)

        if current_difference < min_difference or (current_difference == min_difference and value['Order'] < closest_element['Order']):
            closest_element = value
            min_difference = current_difference

    return closest_element

def get_child(p1, p2):
    
    child_power = (dict_paldeck[p1]['Power'] + dict_paldeck[p2]['Power'])/2
    return find_closest_element(child_power)