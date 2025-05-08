from pygame import image as pg_img
import pygame as pg

from chessSetting.position_store import final_PosLists, image_store, base_pos, gate_list, position,bg_pic, win_num

"""
This module for setting each pawns(or chess).

From left_top to right_top, go through clockwise.
4 players(in turn): p_1, p_2, p_3, p_4
Each player has 4 pawns. Construct in list.
"""

class Chess_Parent:



    """
    gate_list = []
    ======================================================================
    including 4 position of each player---the first position of home path.
    An important judge mark.
    """

    def __init__(self, player, pos, img):

        self.player = player
        self.pos = pos
        self.img = pg_img.load(img)
        self.img = pg.transform.scale_by(self.img, 0.7)
        self.home_startFlag = False
        #==================================
        self._start_flag = False  # whether pawn has start from base
        #==================================
        self.win_flag = False
        self.gate = gate_list[player-1]
        self.frozen_flag = False # whether it is frozen by magic :)



class Pawn(Chess_Parent):
    start_counter = [0,0,0,0] #for each player 1~4.
    pawns_lists = [[],[],[],[]]

    def __init__(self, player, pos, img):
        super().__init__(player, pos, img)
        self.start_order = None
        self.final_pos = None
        self.base = 53 #need to be initialize!!!
        self.totalStep_forward = 0 # used in move def_
        Pawn.pawns_lists[self.player-1].append(self)


#=============================================================
    @property
    def start_flag(self):
        return self._start_flag

    @start_flag.setter
    def start_flag(self, value):
        temp = self._start_flag
        self._start_flag = value
        if value and not temp:
            Pawn.start_counter[self.player-1] += 1
            self.start_order = Pawn.start_counter[self.player-1]
            self.final_pos = final_PosLists[self.player-1][4-Pawn.start_counter[self.player-1]]
        elif not value and temp:
            Pawn.start_counter[self.player-1] -= 1
            self.start_order = None
            self.re_order(self.player)


    @classmethod
    def re_order(cls,player):
        """
        This is just used by start_flag.setter!!!
        reorder the whole pawns in pawn_list
        """
        act_pawns = [pawn for pawn in cls.pawns_lists[player-1] if pawn._start_flag]
        act_pawns.sort(key=lambda p: p.start_order)
        for index_, pawn in enumerate(act_pawns, start = 1):
            pawn.start_order = index_

#===========================================================
    def move_forward_1step(self):
        position[self.pos][2] = 0
        self.totalStep_forward += 1
        #base stage=====================
        if self.pos in base_pos[self.player-1]:
            print("base stage")
            self.pos = self.gate
            self.start_flag=True


        #railway stage==================
        elif not self.home_startFlag and self._start_flag:
            print("railway stage")
            self.pos += 1
            self.pos = (self.pos-1) % 28 + 1
            #transition to home path stage=========
            if self.pos == self.gate and self.totalStep_forward == 29:
                self.home_startFlag = True

        #homepath stage==================
        else:
            print("home stage")
            if self.pos == self.gate:
                self.pos = final_PosLists[self.player-1][0]
            elif self.final_pos is not None and self.pos < self.final_pos:
                self.pos += 1
            if self.pos == self.final_pos:
                self.win_flag = True
                win_num[self.player-1]+=1

        position[self.pos][2] = 1


    def move_backward_1step(self):
        position[self.pos][2] = 0
        if self.pos in range(1,29):
            if self.pos != self.gate:
                self.pos = ( self.pos + 28 - 2 ) % 28 + 1
            elif self.pos == self.gate and self.totalStep_forward == 1:
                self.pos=self.base
                self.start_flag = False
            self.totalStep_forward -= 1
        position[self.pos][2] = 1

def mForward_more_steps(screen,pawn, n):
    for i in range(1, n+1):
        try:
            # Initialize mixer only once
            if not pg.mixer.get_init():
                pg.mixer.init()

            # Load and play the sound
            sound = pg.mixer.Sound("audioNvidio/placeOnBoard.mp3")
            sound.set_volume(2)
            sound.play()

        except pg.error as e:
            print(f"Failed to play sound: {e}")


        pawn.move_forward_1step()
        refresh_pawn(screen)
        pg.time.delay(500)
        print(f"{i}th refreshing")


def mBack_more_steps(screen,pawn, n):
    refresh_pawn(screen)
    for i in range(1, n+1):

        try:
            # Initialize mixer only once
            if not pg.mixer.get_init():
                pg.mixer.init()

            # Load and play the sound
            sound = pg.mixer.Sound("audioNvidio/placeOnBoard.mp3")
            sound.set_volume(2)
            sound.play()

        except pg.error as e:
            print(f"Failed to play sound: {e}")

        pawn.move_backward_1step()
        refresh_pawn(screen)
        pg.time.delay(500)



#loading players......
player_lists = [[], [], [], []]
for i in range(4):
    for j in range(4):
        player_lists[i].append(Pawn(i+1,base_pos[i][j],image_store[i][j]))

def refresh_pawn(screen):
    bg_img = pg.image.load(bg_pic)
    screen.blit(bg_img, (0, 0))
    for i in range(4):
        for j in range(4):
            rect = player_lists[i][j].img.get_rect(center = (position[player_lists[i][j].pos][0],position[player_lists[i][j].pos][1]))
            screen.blit(player_lists[i][j].img, rect)
    pg.display.update()













"""
test code:

p1=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")
p2=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")

p3=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")
p4=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")

p1.start_flag = True
p4.start_flag = True
p3.start_flag=True

print(p1.start_order)
print(p2.start_order)
print(p3.start_order)
print(p4.start_order)

p1.start_flag = False
print(p4.start_order)
p4.start_flag = False
print(p3.start_order)
"""
"""
#Test code: for moving on rail:::
p1=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")
p1.pos = base_pos[p1.player-1][1-1]
p1.start_flag = True
p1.move_forward_1step()
print(f"p1: start_order:{p1.start_order}; totalStep: {p1.totalStep_forward}:  pos: {p1.pos}; start：{p1.start_flag}; arrive at home: {p1.home_startFlag}; finalP:{p1.final_pos}")

p2=Pawn(1,1,"C:/Users/靳/Desktop/OIP-C.jpg")
p2.pos = base_pos[p1.player-1][1-1]
p2.start_flag = True
p2.move_forward_1step()
print(f"p2: start_order:{p2.start_order}; totalStep: {p2.totalStep_forward}:  pos: {p2.pos}; start：{p2.start_flag}; arrive at home: {p2.home_startFlag}; finalP:{p2.final_pos}")

p4=Pawn(2,1,"C:/Users/靳/Desktop/OIP-C.jpg")
p4.pos = base_pos[p1.player-1][1-1]
p4.start_flag = True
p4.move_forward_1step()

print(f"p4: start_order:{p4.start_order}; totalStep: {p4.totalStep_forward}:  pos: {p4.pos}; start：{p4.start_flag}; arrive at home: {p4.home_startFlag}; finalP:{p4.final_pos}")

p2.start_flag = False
print(f"p4: start_order:{p4.start_order}; totalStep: {p4.totalStep_forward}:  pos: {p4.pos}; start：{p4.start_flag}; arrive at home: {p4.home_startFlag}; finalP:{p4.final_pos}")
print(Pawn.pawns_lists)
"""