import screen_effect.element_effect

from chess_interaction.move_in_board import *
from chess_interaction.trapSetting import load_trapPos, generate_trap_pos

from chessSetting.chess import *
from chessSetting.position_store import final_PosLists, image_store, base_pos, gate_list, position, bg_pic, magic_pic


#==============================================
pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode([screen_width, screen_height])

screen.fill((255, 255, 255))
pg.display.set_caption("TRIWIZARD MAZE GAME")

bg_img = pg.image.load(bg_pic)
bg_img = pg.transform.scale(bg_img, (screen_width, screen_height))
magic_img = pg.image.load(magic_pic).convert_alpha()
#==============load trap and its Icon............
trap_pos = generate_trap_pos()
load_trapPos(position,trap_pos)
for eachIcon in trap_pos:
    magic_rect = magic_img.get_rect(center=(position[eachIcon][0], position[eachIcon][1]))
    bg_img.blit(magic_img, magic_rect)

#=====draw the trap icon=========
screen.blit(bg_img, (0, 0))
pg.display.flip()
#==prompt text===============
draw_text(screen,"Remember these star-shaped magic signal!!! please!!!",(640,220),40,(255,0,0))
time.sleep(3)
draw_text(screen,"Open [CAPS LOCK]!",(639,470),100,(255,0,0))
time.sleep(3)
#=========loading audio and timer effect...........
screen_effect.element_effect.load_and_play_music("audioNvidio/7secs.mp3",0.7)
screen_effect.element_effect.countdown_timer(screen,8,bg_img)
screen_effect.element_effect.load_and_play_music("audioNvidio/anywhere_is.mp3",0.7)

"""
mForward_more_steps(screen,player_lists[0][0],5)

print(f"p_1_1: playerNum: {player_lists[0][0].player} steps: {player_lists[0][0].totalStep_forward}; pos: {player_lists[0][0].pos} "
      f"\n Whether start: {player_lists[0][0].start_flag}")

move_interact(screen,1,1,6)
#mForward_more_steps(screen,player_lists[0][0],2)
print(f"p_1_1: steps: {player_lists[0][0].totalStep_forward}; pos: {player_lists[0][0].pos} "
      f"\n Whether start: {player_lists[0][0].start_flag}")
time.sleep(5)

#=====================
mForward_more_steps(screen,player_lists[0][0],5)
print(f"p_1_1: playerNum: {player_lists[0][0].player} steps: {player_lists[0][0].totalStep_forward}; pos: {player_lists[0][0].pos} "
      f"\n Whether start: {player_lists[0][0].start_flag}")
print(position[player_lists[0][0].pos])
"""


if __name__=='__main__':
    while True:



        for player in range(4):
            refresh_pawn(screen)
            player+=1
            draw_text(screen, f"player {player}'s turn",(122,324))

            die_num = random.randint(1, 6)
            screen_effect.element_effect.pop_Die(screen, die_num)
            pawn_num = screen_effect.element_effect.prompt_and_show_p_num(screen)
            print(die_num)
            move_interact(screen,player,pawn_num,die_num)
            screen.blit(bg_img, (0, 0))

            print(f"player_{player}: pos:{player_lists[player-1][pawn_num-1].pos}; "
                  f"steps:{player_lists[player-1][pawn_num-1].totalStep_forward}; "
                  f"start_flag: {player_lists[player-1][pawn_num-1].start_flag}")

            pinfo_1 = (f"------turn: player {player}------")
            pinfo_2 = (
                f"pawn 1: start?: {player_lists[player - 1][0].start_flag}; steps: {player_lists[player - 1][0].totalStep_forward}")
            pinfo_3 = (
                f"pawn 2: start?: {player_lists[player - 1][1].start_flag}; steps: {player_lists[player - 1][1].totalStep_forward}")
            pinfo_4 = (
                f"pawn 3: start?: {player_lists[player - 1][2].start_flag}; steps: {player_lists[player - 1][2].totalStep_forward}")
            pinfo_5 = (
                f"pawn 4: start?: {player_lists[player - 1][3].start_flag}; steps: {player_lists[player - 1][3].totalStep_forward}")

            text_rect_1 = screen_effect.element_effect.draw_text(screen, pinfo_1, (127,437),14)
            text_rect_2 = screen_effect.element_effect.draw_text(screen, pinfo_2, (127, 457),14)
            text_rect_3 = screen_effect.element_effect.draw_text(screen, pinfo_3, (127, 477),14)
            text_rect_4 = screen_effect.element_effect.draw_text(screen, pinfo_4, (127, 497),14)
            text_rect_5 = screen_effect.element_effect.draw_text(screen, pinfo_5, (127, 517),14)

            time.sleep(3)


