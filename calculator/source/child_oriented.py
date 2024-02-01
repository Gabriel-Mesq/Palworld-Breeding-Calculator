from paldeck import dict_paldeck

def find_closest_element(target_value):
    closest_element = None
    min_difference = float('inf')  # Inicializa com infinito para garantir que a primeira diferença será menor

    for key, value in dict_paldeck.items():
        current_difference = abs(value['Power'] - target_value)

        if current_difference < min_difference or (current_difference == min_difference and value['Order'] < closest_element['Order']):
            closest_element = value
            min_difference = current_difference

    return closest_element

def get_parent(child_power):
    duplas = []
    menor_diferenca = float('inf')  # Inicializa com um valor grande

    for key1, value1 in dict_paldeck.items():
        for key2, value2 in dict_paldeck.items():
            if key1 != key2:
                media = (value1['Power'] + value2['Power']) / 2
                closest = find_closest_element(media)
                if  closest['Power'] == child_power:
                    duplas.append((key1, key2))

    return duplas

# Exemplo de uso:
resultado = get_parent(580)
print(f"Duplas cuja média é {580}: {resultado}")