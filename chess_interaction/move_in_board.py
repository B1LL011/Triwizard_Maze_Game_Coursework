import sys
import os


import pygame.image

from chess_interaction.trapSetting import trap_effect
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(parent_dir)
from screen_effect.element_effect import *
from chessSetting.chess import *
from chessSetting.position_store import final_PosLists, image_store, base_pos, gate_list, position, bg_pic,win_num

bg_refresh = pygame.image.load(bg_pic)



def move_interact(screen,player, pawn_num ,die_num):
    pawn = player_lists[player-1][pawn_num-1]
    if pawn.frozen_flag:
        player.frozen_flag = False
        #=========================choose another pawn
        new_num = prompt_and_show_p_num(screen)
        move_interact(screen,player,new_num,die_num)
        # =========================
        return
    if pawn.win_flag:
        # =========================choose another pawn
        npawn_num = prompt_and_show_p_num(screen)
        move_interact(screen,player, npawn_num, die_num)
        # =========================
        return
    if not pawn.start_flag: # and pawn.totalStep_forward == 0
        if die_num != 6:

            return
        else:
            mForward_more_steps(screen,pawn,1)
            # =========================have new turn
            ndie_num= random.randint(1,6)
            pop_Die(screen,ndie_num)
            npawn_num = prompt_and_show_p_num(screen)
            move_interact(screen,player, npawn_num, ndie_num)
            # =========================

            return
    if pawn.totalStep_forward+die_num >29: #about to enter home
        print("about to enter home")
        if 0 <= pawn.totalStep_forward+die_num-30 <= 3:
            if final_PosLists[player-1][pawn.totalStep_forward+die_num-29-1]==pawn.final_pos:

                mForward_more_steps(screen,pawn,die_num)
                pawn.win_flag = True
                return
        else:
            # =========================choose another pawn


            npawn_num = prompt_and_show_p_num(screen)
            move_interact(screen,player, npawn_num, die_num)
            return
            # =========================#
    elif 1 <= pawn.totalStep_forward+die_num <=29 and pawn.start_flag and not pawn.home_startFlag: #railway stage
        # wrong:::::mForward_more_steps(screen,pawn,die_num)
        next_pos = (pawn.pos+die_num-1)%28+1
        if position[next_pos][2] !=0: #check occupied?
            rect_text = draw_text(screen, f"CRASH!!!", (1125, 333),30)
            time.sleep(3)
            self_cF = False
            enermy_pos=[]
            for i in range(4):
                if player_lists[player-1][i].pos == next_pos:
                    self_cF = True
                    break
            if self_cF: #friendly force, then choose another pawn
                # =========================choose another pawn
                npawn_num = prompt_and_show_p_num(screen)
                move_interact(screen, player, npawn_num, die_num)
                return
                # =========================
            else: # encounter enemy:
                for i in range(4):
                    goOn=True
                    if i==player-1:
                        continue
                    for j in range(4):
                        if player_lists[i][j].pos==next_pos:
                            enermy_pos.append(i)
                            enermy_pos.append(j)
                            goOn=False
                            break
                    if not goOn:
                        break

                mForward_more_steps(screen, pawn, die_num)

                wretch = player_lists[enermy_pos[0]][enermy_pos[1]]
                wretch.pos=base_pos[enermy_pos[0]][enermy_pos[1]]
                wretch.totalStep_forward=0
                wretch.start_flag=False
                wretch.home_startFlag=False
            clear_text(screen,rect_text,bg_refresh )
        else:
            mForward_more_steps(screen, pawn, die_num)

        if position[next_pos][3] !=0: #check trap
            input_n = None
            rect_text = draw_text(screen, "Maze card there!!!",(1132,308),20)

            try:
                # Initialize mixer only once
                if not pygame.mixer.get_init():
                    pygame.mixer.init()

                # Load and play the sound
                sound = pygame.mixer.Sound("audioNvidio/breaking_glass.mp3")
                sound.set_volume(2)
                sound.play()

            except pg.error as e:
                print(f"Failed to play sound: {e}")

            if position[next_pos][3] == 1:
                trap_list=trap_effect(1)
                if trap_list['move'] is not None:
                    #================
                    rect_text_1 = draw_text(screen,"Enter the number of",(1132,347),13)
                    draw_text(screen, "steps to move forward (1-4):", (1132, 377), 13)
                    while input_n is None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            elif event.type == pygame.KEYDOWN:
                                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                    input_n = int(event.unicode)
                    pygame.display.update()
                    rect_text_2 = draw_text(screen, str(input_n),(1132,401))
                    time.sleep(2)
                    mForward_more_steps(screen,pawn,input_n)

                    #================================
                else:
                    # =========================have new turn
                    draw_text(screen,"Have a new turn!!!",(1132,345),13)
                    time.sleep(3)
                    ndie_num = random.randint(1, 6)
                    pop_Die(screen, ndie_num)
                    npawn_num = prompt_and_show_p_num(screen)
                    move_interact(screen, player, npawn_num, ndie_num)
                    # =========================
            if position[pawn.pos + die_num][3] == 2:
                draw_text(screen,"Oops, you are unlucky!!!",(1132,370),13)
                time.sleep(3)
                trap_list=trap_effect(2)
                if trap_list['moveBack'] is not None:
                    mBack_more_steps(screen,pawn,random.randint(1,7))
                else:
                    pawn.frozen_flag = True
            #need to complete yet...
            if position[pawn.pos + die_num][3] == 3:
                trap_list=trap_effect(3)
                if trap_list['ATK']['moveBack'] is not None:
                    rect_text_1 = draw_text(screen, "Enter an unlucky player(1-4): ", (1132, 347),13)
                    while input_n is None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            elif event.type == pygame.KEYDOWN:
                                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                    input_n = int(event.unicode)
                    pygame.display.update()
                    rect_text_2 = draw_text(screen, str(input_n), (1132, 401))
                    time.sleep(2)
                    for j in range(4):
                        if player_lists[input_n-1][j].start_flag:
                            mBack_more_steps(screen, player_lists[input_n - 1][j], random.randint(1, 6))
                            break

                elif trap_list['ATK']['Frozen'] is not None:
                    rect_text_1 = draw_text(screen, "Enter an unlucky player to froze(1-4): ", (1132, 347),13)
                    while input_n is None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            elif event.type == pygame.KEYDOWN:
                                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                    input_n = int(event.unicode)
                    pygame.display.update()
                    rect_text_2 = draw_text(screen, str(input_n), (1132, 401))
                    time.sleep(2)
                    for j in range(4):
                        if player_lists[input_n-1][j].start_flag:
                            player_lists[input_n - 1][j].frozen_flag = True
                            break

                else:
                    draw_text(screen, "Enter an unlucky player", (1132, 347),13)
                    draw_text(screen, " to go back Base(1-4): ", (1132, 377), 13)
                    while input_n is None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            elif event.type == pygame.KEYDOWN:
                                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                    input_n = int(event.unicode)
                    pygame.display.update()
                    rect_text_2 = draw_text(screen, str(input_n), (1132, 401))
                    time.sleep(2)
                    for j in range(4):
                        if player_lists[input_n-1][j].start_flag:
                            player_lists[input_n - 1][j].pos = base_pos[input_n - 1][j]
                            player_lists[input_n - 1][j].start_flag = False
                            player_lists[input_n - 1][j].home_startFlag = False
                            player_lists[input_n - 1][j].totalStep_forward = 0
                            break



            clear_text(screen,rect_text,bg_refresh)

    for i in win_num:
        if i == 4:
            sys.exit()