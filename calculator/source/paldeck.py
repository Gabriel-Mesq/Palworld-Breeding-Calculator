from math import floor

dict_paldeck = {
    1: {'Name': 'Lamball', 'Power': 1470, 'Order': 27},
    2: {'Name': 'Cattiva', 'Power': 1460, 'Order': 46},
    3: {'Name': 'Chikipi', 'Power': 1500, 'Order': 62},
    4: {'Name': 'Lifmunk', 'Power': 1430, 'Order': 7},
    5: {'Name': 'Foxparks', 'Power': 1400, 'Order': 20},
    6: {'Name': 'Fuack', 'Power': 1330, 'Order': 59},
    7: {'Name': 'Sparkit', 'Power': 1410, 'Order': 65},
    8: {'Name': 'Tanzee', 'Power': 1250, 'Order': 107},
    9: {'Name': 'Rooby', 'Power': 1155, 'Order': 138},
    10: {'Name': 'Pengullet', 'Power': 1350, 'Order': 23},
    11: {'Name': 'Penking', 'Power': 520, 'Order': 122},
    12.1: {'Name': 'Jolthog', 'Power': 1370, 'Order': 17},
    12.2: {'Name': 'Jolthog Cryst', 'Power': 1360, 'Order': 18},
    13.1: {'Name': 'Gumoss', 'Power': 1240, 'Order': 112},
    13.2: {'Name': 'Gumoss (Special)', 'Power': 1240, 'Order': 113},
    14: {'Name': 'Vixy', 'Power': 1450, 'Order': 79},
    15: {'Name': 'Hoocrates', 'Power': 1390, 'Order': 82},
    16: {'Name': 'Teafant', 'Power': 1490, 'Order': 14},
    17: {'Name': 'Depresso', 'Power': 1380, 'Order': 47},
    18: {'Name': 'Cremis', 'Power': 1455, 'Order': 135},
    19: {'Name': 'Daedream', 'Power': 1230, 'Order': 106},
    20: {'Name': 'Rushoar', 'Power': 1130, 'Order': 6},
    21: {'Name': 'Nox', 'Power': 1180, 'Order': 121},
    22: {'Name': 'Fuddler', 'Power': 1220, 'Order': 101},
    23: {'Name': 'Killamari', 'Power': 1290, 'Order': 85},
    24.1: {'Name': 'Mau', 'Power': 1480, 'Order': 4},
    24.2: {'Name': 'Mau Cryst', 'Power': 1440, 'Order': 5},
    25: {'Name': 'Celaray', 'Power': 870, 'Order': 128},
    26: {'Name': 'Direhowl', 'Power': 1060, 'Order': 15},
    27: {'Name': 'Tocotoco', 'Power': 1340, 'Order': 8},
    28: {'Name': 'Flopie', 'Power': 1280, 'Order': 91},
    29: {'Name': 'Mozzarina', 'Power': 910, 'Order': 86},
    30: {'Name': 'Bristla', 'Power': 1320, 'Order': 21},
    31.1: {'Name': 'Gobfin', 'Power': 1090, 'Order': 25},
    31.2: {'Name': 'Gobfin Ignis', 'Power': 1100, 'Order': 26},
    32.1: {'Name': 'Hangyu', 'Power': 1420, 'Order': 31},
    32.2: {'Name': 'Hangyu Cryst', 'Power': 1422, 'Order': 32},
    33.1: {'Name': 'Mossanda', 'Power': 430, 'Order': 97},
    33.2: {'Name': 'Mossanda Lux', 'Power': 390, 'Order': 98},
    34: {'Name': 'Woolipop', 'Power': 1190, 'Order': 39},
    35: {'Name': 'Caprity', 'Power': 930, 'Order': 75},
    36: {'Name': 'Melpaca', 'Power': 890, 'Order': 41},
    37.1: {'Name': 'Eikthyrdeer', 'Power': 920, 'Order': 9},
    37.2: {'Name': 'Eikthyrdeer Terra', 'Power': 900, 'Order': 10},
    38.1: {'Name': 'Nitewing', 'Power': 420, 'Order': 90},
    39: {'Name': 'Ribunny', 'Power': 1310, 'Order': 117},
    40.1: {'Name': 'Incineram', 'Power': 590, 'Order': 2},
    40.2: {'Name': 'Incineram Noct', 'Power': 580, 'Order': 3},
    41: {'Name': 'Cinnamoth', 'Power': 490, 'Order': 132},
    42: {'Name': 'Arsox', 'Power': 790, 'Order': 99},
    43: {'Name': 'Dumud', 'Power': 895, 'Order': 136},
    44: {'Name': 'Cawgnito', 'Power': 1080, 'Order': 44},
    45.1: {'Name': 'Leezpunk', 'Power': 1120, 'Order': 57},
    45.2: {'Name': 'Leezpunk Ignis', 'Power': 1140, 'Order': 58},
    46: {'Name': 'Loupmoon', 'Power': 950, 'Order': 30},
    47: {'Name': 'Galeclaw', 'Power': 1030, 'Order': 12},
    48.1: {'Name': 'Robinquill', 'Power': 1020, 'Order': 52},
    48.2: {'Name': 'Robinquill Terra', 'Power': 1000, 'Order': 53},
    49: {'Name': 'Gorirat', 'Power': 1040, 'Order': 16},
    50: {'Name': 'Beegarde', 'Power': 1070, 'Order': 95},
    51: {'Name': 'Elizabee', 'Power': 330, 'Order': 94},
    52: {'Name': 'Grintale', 'Power': 510, 'Order': 131},
    53: {'Name': 'Swee', 'Power': 1300, 'Order': 114},
    54: {'Name': 'Sweepa', 'Power': 410, 'Order': 115},
    55: {'Name': 'Chillet', 'Power': 800, 'Order': 123},
    56: {'Name': 'Univolt', 'Power': 680, 'Order': 19},
    57: {'Name': 'Foxcicle', 'Power': 760, 'Order': 104},
    58.1: {'Name': 'Pyrin', 'Power': 360, 'Order': 35},
    58.2: {'Name': 'Pyrin Noct', 'Power': 240, 'Order': 36},
    59: {'Name': 'Reindrix', 'Power': 880, 'Order': 76},
    60: {'Name': 'Rayhound', 'Power': 740, 'Order': 100},
    61: {'Name': 'Kitsun', 'Power': 830, 'Order': 56},
    62: {'Name': 'Dazzi', 'Power': 1210, 'Order': 24},
    63: {'Name': 'Lunaris', 'Power': 1110, 'Order': 22},
    64.1: {'Name': 'Dinossom', 'Power': 820, 'Order': 63},
    64.2: {'Name': 'Dinossom Lux', 'Power': 810, 'Order': 64},
    65.1: {'Name': 'Surfent', 'Power': 560, 'Order': 42},
    65.2: {'Name': 'Surfent Terra', 'Power': 550, 'Order': 43},
    66: {'Name': 'Maraith', 'Power': 1150, 'Order': 51},
    67: {'Name': 'Digtoise', 'Power': 850, 'Order': 11},
    68: {'Name': 'Tombat', 'Power': 750, 'Order': 96},
    69: {'Name': 'Lovander', 'Power': 940, 'Order': 81},
    70: {'Name': 'Flambelle', 'Power': 1405, 'Order': 137},
    71.1: {'Name': 'Vanwyrm', 'Power': 660, 'Order': 60},
    71.2: {'Name': 'Vanwyrm Cryst', 'Power': 620, 'Order': 61},
    72: {'Name': 'Bushi', 'Power': 640, 'Order': 127},
    73: {'Name': 'Beakon', 'Power': 220, 'Order': 118},
    74: {'Name': 'Ragnahawk', 'Power': 380, 'Order': 126},
    75: {'Name': 'Katress', 'Power': 700, 'Order': 116},
    76: {'Name': 'Wixen', 'Power': 1160, 'Order': 80},
    77: {'Name': 'Verdash', 'Power': 990, 'Order': 103},
    78: {'Name': 'Vaelet', 'Power': 1050, 'Order': 89},
    79: {'Name': 'Sibelyx', 'Power': 450, 'Order': 78},
    80.1: {'Name': 'Elphidran', 'Power': 540, 'Order': 37},
    80.2: {'Name': 'Elphidran Aqua', 'Power': 530, 'Order': 38},
    81.1: {'Name': 'Kelpsea', 'Power': 1260, 'Order': 83},
    81.2: {'Name': 'Kelpsea Ignis', 'Power': 1270, 'Order': 84},
    82: {'Name': 'Azurobe', 'Power': 500, 'Order': 45},
    83: {'Name': 'Cryolinx', 'Power': 130, 'Order': 40},
    84.1: {'Name': 'Blazehowl', 'Power': 710, 'Order': 108},
    84.2: {'Name': 'Blazehowl Noct', 'Power': 670, 'Order': 109},
    85.1: {'Name': 'Relaxaurus', 'Power': 280, 'Order': 54},
    85.2: {'Name': 'Relaxaurus Lux', 'Power': 270, 'Order': 55},
    86.1: {'Name': 'Broncherry', 'Power': 860, 'Order': 71},
    86.2: {'Name': 'Broncherry Aqua', 'Power': 840, 'Order': 72},
    87: {'Name': 'Petallia', 'Power': 780, 'Order': 130},
    88.1: {'Name': 'Reptyro', 'Power': 320, 'Order': 49},
    88.2: {'Name': 'Ice Reptyro', 'Power': 230, 'Order': 50},
    89.1: {'Name': 'Kingpaca', 'Power': 470, 'Order': 110},
    89.2: {'Name': 'Ice Kingpaca', 'Power': 440, 'Order': 111},
    90.1: {'Name': 'Mammorest', 'Power': 300, 'Order': 68},
    90.2: {'Name': 'Mammorest Cryst', 'Power': 290, 'Order': 69},
    91: {'Name': 'Wumpo', 'Power': 460, 'Order': 87},
    91.1: {'Name': 'Wumpo Botan', 'Power': 480, 'Order': 88},
    92: {'Name': 'Warsect', 'Power': 340, 'Order': 119},
    93: {'Name': 'Fenglope', 'Power': 980, 'Order': 48},
    94: {'Name': 'Felbat', 'Power': 1010, 'Order': 70},
    95: {'Name': 'Quivern', 'Power': 350, 'Order': 124},
    96: {'Name': 'Blazamut', 'Power': 0, 'Order': 74},
    97: {'Name': 'Helzephyr', 'Power': 190, 'Order': 125},
    98: {'Name': 'Astegon', 'Power': 150, 'Order': 102},
    99: {'Name': 'Menasting', 'Power': 260, 'Order': 133},
    100: {'Name': 'Anubis', 'Power': 570, 'Order': 1},
    101.1: {'Name': 'Jormuntide', 'Power': 310, 'Order': 28},
    101.2: {'Name': 'Jormuntide Ignis', 'Power': 315, 'Order': 29},
    102.1: {'Name': 'Suzaku', 'Power': 50, 'Order': 33},
    102.2: {'Name': 'Suzaku Aqua', 'Power': 30, 'Order': 34},
    103: {'Name': 'Grizzbolt', 'Power': 200, 'Order': 13},
    104.1: {'Name': 'Lyleen', 'Power': 250, 'Order': 92},
    104.2: {'Name': 'Lyleen Noct', 'Power': 210, 'Order': 93},
    105: {'Name': 'Faleris', 'Power': 370, 'Order': 73},
    106: {'Name': 'Orserk', 'Power': 140, 'Order': 134},
    107: {'Name': 'Shadowbeak', 'Power': 60, 'Order': 77},
    108: {'Name': 'Paladius', 'Power': 80, 'Order': 120},
    109: {'Name': 'Necromus', 'Power': 70, 'Order': 129},
    110.1: {'Name': 'Frostallion', 'Power': 120, 'Order': 66},
    110.2: {'Name': 'Frostallion Noct', 'Power': 100, 'Order': 67},
    111: {'Name': 'Jetragon', 'Power': 90, 'Order': 105}
}