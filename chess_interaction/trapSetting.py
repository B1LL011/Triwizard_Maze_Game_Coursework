import random
# generate a set of trap's position===============================
def generate_trap_pos():
    av_numList_1 = set(range(2, 8))
    av_numList_2 = set(range(9, 15))
    av_numList_3 = set(range(16, 22))
    av_numList_4 = set(range(23, 29))

    result_set_1 = set()
    set_1_n = random.randint(2,4)
    while len(result_set_1)< set_1_n:
        num=random.choice(list(av_numList_1))
        result_set_1.add(num)

    result_set_2 = set()
    set_2_n = random.randint(2, 4)
    while len(result_set_2) < set_2_n:
        num = random.choice(list(av_numList_2))
        result_set_2.add(num)

    result_set_3 = set()
    set_3_n = random.randint(2, 4)
    while len(result_set_3) < set_3_n:
        num = random.choice(list(av_numList_3))
        result_set_3.add(num)

    result_set_4 = set()
    set_4_n = random.randint(2, 4)
    while len(result_set_4) < set_4_n:
        num = random.choice(list(av_numList_4))
        result_set_4.add(num)


    final_result_set = result_set_4 | result_set_3 | result_set_2 | result_set_1
    return final_result_set


# modify pos_dic's trap flag using trap_pos set=================================
def load_trapPos(pos_dic, trap_pos): #input position dic, trap_pos set
    for num in trap_pos:
        pos_dic[num][3]=random.randint(0,3)
"""
#trapEffect_dict = [ <move: (1~6) | -(1~6)>, <frozen Flag: palyerxxx.frozen_flag = ...>, 
<one more die chance FLAG: true or false> , <attack others [move back; frozen; go back to base]>  ]
"""
def trap_effect(trap_flag):
    self_posi_list=['move','popD']
    self_nega_list = ['moveBack', 'Frozen']
    other_nega_list = ['moveBack', 'Frozen', 'goBase']
    tE_dict = {
        'move': None,
        'moveBack':None, #compusory by random
        'Frozen': None,
        'popD': None,
        'ATK': {'moveBack': None, 'Frozen':None, 'goBase':None}

    }
    if trap_flag == 0:
        return

    elif trap_flag == 1:
        pos_one = random.choice(self_posi_list)
        if pos_one == 'move':
            tE_dict['move']=True
        elif pos_one == 'popD':
            tE_dict['popD']=True

    elif trap_flag == 2:
        neg_one = random.choice(self_nega_list)
        if neg_one == 'moveBack':
            tE_dict['moveBack']=random.randint(1,7)
        elif neg_one == 'Frozen':
            tE_dict['Frozen'] = True

    else:
        other_neg_one = random.choices(other_nega_list, weights=[0.4 ,0.4, 0.2],k=1)[0]
        if other_neg_one == 'moveBack':
            tE_dict['ATK']['moveBack'] = True
        elif other_neg_one == 'Frozen':
            tE_dict['ATK']['Frozen'] = True
        elif other_neg_one == 'goBase':
            tE_dict['ATK']['goBase'] = True


    return tE_dict






