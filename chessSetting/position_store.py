import os

current_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(current_path) #../chessSetting
final_dir = os.path.dirname(parent_dir) #../TMG
image_set_path = os.path.join(final_dir, "all_image") #../TMG/all_image

win_num=[0,0,0,0]

bg_pic = os.path.join(image_set_path,"bg_pic.png")
magic_pic = os.path.join(image_set_path, "magic_signal.png")
# 4(each player) X 4(each pawns); from first to last(the closed to the far)
final_PosLists = [(29,30,31,32), (33,34,35,36), (37,38,39,40), (41,42,43,44)]

image_store = [[image_set_path+"/1_1.png",
                image_set_path+"/1_2.png",
                image_set_path+"/1_3.png",
                image_set_path+"/1_4.png"],

               [image_set_path + "/2_1.png",
                image_set_path + "/2_2.png",
                image_set_path + "/2_3.png",
                image_set_path + "/2_4.png"],

               [image_set_path + "/3_1.png",
                image_set_path + "/3_2.png",
                image_set_path + "/3_3.png",
                image_set_path + "/3_4.png"],

               [image_set_path + "/4_1.png",
                image_set_path + "/4_2.png",
                image_set_path + "/4_3.png",
                image_set_path + "/4_4.png"]
               ]
base_pos = [(45,46,47,48),(49,50,51,52),(53,54,55,56),(57,58,59,60)]
gate_list = (1,8,15,22)
position = {
    """
    [x, y, whether be occupied, whether has a trap: 0(none), 
          1(self-positive), 2(self-negative), 3(others)]
    """
    # 1-28:from down to top clockwise
    1: [ 640, 629, 0, 0],
    2: [ 590, 583, 0, 0],
    3: [ 546, 545, 0, 0],
    4: [ 501, 508, 0, 0],
    5: [ 461, 470, 0, 0],
    6: [ 416, 432, 0, 0],
    7: [ 367, 393, 0, 0],

    8: [ 325, 349, 0, 0],
    9: [ 374, 309, 0, 0],
    10: [ 425, 270, 0, 0],
    11: [ 467, 230, 0, 0],
    12: [ 508, 194, 0, 0],
    13: [ 548, 155, 0, 0],
    14: [ 587, 117, 0, 0],

    15: [ 637, 79, 0, 0],
    16: [ 681, 119, 0, 0],
    17: [ 718, 157, 0, 0],
    18: [ 759, 191, 0, 0],
    19: [ 802, 232, 0, 0],
    20: [ 843, 274, 0, 0],
    21: [ 887, 311, 0, 0],

    22: [ 938, 350, 0, 0],
    23: [ 900, 397, 0, 0],
    24: [ 859, 434, 0, 0],
    25: [ 817, 469, 0, 0],
    26: [ 775, 510, 0, 0],
    27: [ 732, 551, 0, 0],
    28: [ 692, 590, 0, 0],
    #==============================================================
    # 29~32: down player's home path: 28+(1~4)+(4*0)
    29: [ 642, 576, 0, 0],
    30: [ 642, 527, 0, 0],
    31: [ 642, 479, 0, 0],
    32: [ 640, 434, 0, 0],
    # 33~36: left player's home path: 28+(1~4)+(4*1)
    33: [ 390, 356, 0, 0],
    34: [ 441, 351, 0, 0],
    35: [ 490, 351, 0, 0],
    36: [ 544, 352, 0, 0],
    # 37~40: top player's home path:
    37: [ 639, 131, 0, 0],
    38: [ 639, 180, 0, 0],
    39: [ 633, 231, 0, 0],
    40: [ 641, 272, 0, 0],
    # 41~44: right player's home path:
    41: [ 876, 360, 0, 0],
    42: [ 830, 358, 0, 0],
    43: [ 778, 362, 0, 0],
    44: [ 724, 360, 0, 0],
    #===============================================================
    # 45~48: downplayer's base:
    45: [ 348, 571, 0, 0],
    46: [ 439, 572, 0, 0],
    47: [ 349, 647, 0, 0],
    48: [ 436, 647, 0, 0],
    # 49~52: left..base
    49: [ 333, 71, 0, 0],
    50: [ 429, 66, 0, 0],
    51: [ 331, 145, 0, 0],
    52: [ 424, 149, 0, 0],
    # 53~56: top base
    53: [ 842,66, 0, 0],
    54: [ 934,68, 0, 0],
    55: [ 841,146, 0, 0],
    56: [ 932,150, 0, 0],
    # 57~60: left base
    57: [ 853, 572, 0, 0],
    58: [ 934, 571, 0, 0],
    59: [ 856, 645, 0, 0],
    60: [ 934, 645, 0, 0],

}
