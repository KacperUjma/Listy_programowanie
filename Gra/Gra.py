import pygame
from pygame.locals import *
import random
import os
pygame.init()
screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Arcade Game')
font = pygame.font.SysFont('freesansbold.ttf',30)
animation_rate = 0
game_paused = True
menu_state = "main"

def GIF_convert(Folder, size):
    List = []
    for FolderName, SubFolder, files in os.walk(Folder):
        for file in files:
            if file != "Thumbs.db":
                file_path = os.path.join(FolderName, file)
                Frame = pygame.image.load(file_path).convert_alpha()
                Frame = pygame.transform.scale(Frame, size)
                List.append(Frame)
            else: continue
    return List
# Menu
class button():
    def __init__(self, pos, text, size = (180,70)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

    def draw_button(self):
        action = False
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pygame.draw.rect(screen, (50,50,50), self.rect)

        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0,0,0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0,0,0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        text_img = font.render(self.text, True, "white")
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action
    
    def soundeffect(self):
        if self.draw_button():
            sound_channel_menu.play(menu_select_sound)  
start_button = button((screen_size[0]/2-90,100),"Start Game")
bestscores_button = button((screen_size[0]/2-90,200),"Best Scores")
rules_button = button((screen_size[0]/2-90,300),"Rules")
credits_button = button((screen_size[0]/2-90,400),"Credits" )
quit_button = button((screen_size[0]/2-90,500),"Quit")
back_button = button((screen_size[0]/4*3,600),"Back",size=(100,50))
resume_button = button((screen_size[0]/2-90,300),"Resume")
class button_img():
    def __init__(self, x, y, file, size):
        self.image = GIF_convert(file,size)
        self.rect = self.image[0].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.frame = 1

    def click(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if self.frame >= len(self.image)-1:
                    self.frame = 0
                else:
                    self.frame += 1
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
        
    def show(self):
        screen.blit(self.image[self.frame], self.rect)
sound_button = button_img(680, 20,"D:\Programowanie\Semestr2\Gra\sound_button",(30,30))               
# mixer
pygame.mixer.init()
class sound(pygame.mixer.Sound):
    def __init__(self,file,volume):
        pygame.mixer.Sound.__init__(self,file)
        self.s = pygame.mixer.Sound(file)
        self.s.set_volume(volume)
    def play(self,loop):
        if loop == True:
            self.s.play(-1)
        elif loop == False:
            self.s.play()        
jump_sound = sound("D:\Programowanie\Semestr2\Gra\Music\jump.mp3",0.6)
coin_sound = sound("D:\Programowanie\Semestr2\Gra\Music\coin.wav",0.01)
menu_select_sound = sound("Semestr2/Gra/Music/menu_select.wav",1)
background_sound = sound("D:\Programowanie\Semestr2\Gra\Music\\backgroud.wav",0.01)
death_sound = sound("D:\Programowanie\Semestr2\Gra\Music\deth.mp3",0.5)
sound_channel_jump = pygame.mixer.Channel(0)
sound_channel_jump.set_volume(0.6)
sound_channel_coin = pygame.mixer.Channel(1)
sound_channel_coin.set_volume(0.3)
sound_channel_menu = pygame.mixer.Channel(2)
sound_channel_menu.set_volume(1)
pygame.mixer.music.load("D:\Programowanie\Semestr2\Gra\Music\\backgroud.wav")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
sound_channel_death = pygame.mixer.Channel(4)
sound_channel_death.set_volume(0.5)
sounds = {sound_channel_jump:0.6, sound_channel_coin:0.3, sound_channel_menu:1,  sound_channel_death:0.5}

class TextInput():
    def __init__(self, pos, size = (180,70)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = ''
        self.active = False
        self.font = pygame.font.Font(None, 24)
        self.entered_text = "Guest"

    def write(self, event):
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == K_RETURN:
                    self.entered_text = self.text
                    print("Wprowadzony tekst:", self.entered_text)
                    self.text = ''
                else:
                    if len(self.text) < 16:
                        self.text += event.unicode
                    else: pass
        elif event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

    def show(self):
        pygame.draw.rect(screen, (50,50,50), self.rect)
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0,0,0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0,0,0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        text_surface = self.font.render(self.text, True, (255,255,255))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
player_name = TextInput((screen_size[0]//2-75,600),size=(150,25))
# Obsluga player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = pygame.Vector2(45,45)
        self.position = pygame.Vector2(screen_size[0]//2-self.size.x//2, screen_size[1]//2-self.size.y//2)
        self.assets = GIF_convert("D:\Programowanie\Semestr2\Gra\\bird_fly_animation",self.size)
        self.animation = 0
        self.rect = self.assets[0].get_rect()
        self.set_to_start()
        # self.rect.inflate_ip(-self.rect.width / 1.5, -self.rect.height / 1.5)
        self.v = pygame.Vector2(200,100)
        self.a = 500
        self.cooldown = 225
        self.last_space = 0

    def movement(self):
        self.rect.x += self.v.x * dt
        self.rect.y += self.v.y * dt

        if self.v.y >= 500:
            self.a = 0
        else:
            self.a = 500
        
        self.v.y += self.a * dt

        if keys[K_SPACE] and (pygame.time.get_ticks()-self.last_space > self.cooldown):
            self.v.y = -200
            self.last_space = pygame.time.get_ticks()
            sound_channel_jump.play(jump_sound)

    def channel(self,direction):
        if direction == "up":
            self.rect.y = -self.size.y/2
        elif direction == "down":
            self.rect.y = screen_size[1]

    def turn(self):
        self.v.x *= -1
        for i in range(len(self.assets)):
            self.assets[i] = pygame.transform.flip(self.assets[i],True,False)

    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    
    def collidelist(self,list):
        return self.rect.collidelist(list)
    
    def set_to_start(self):
        self.rect.center = tuple(self.position)
    
    def show(self):
        self.animation %= len(self.assets)
        screen.blit(self.assets[self.animation], self.rect)
player = Player()
# spikes
class spike(pygame.sprite.Sprite):
    def __init__(self,direction):
        pygame.sprite.Sprite.__init__(self)
        self.size = pygame.Vector2(60,60)
        self.dir = direction
        self.asset = GIF_convert(Folder="D:\Programowanie\Semestr2\Gra\\spike_animation",size=self.size)[0]
        self.col_rect = pygame.Rect(-100, -100, 20, 30)
        if self.dir == "r":
            self.asset = pygame.transform.rotate(self.asset, -90) 
        elif self.dir == "l":
            self.asset = pygame.transform.rotate(self.asset, 90)

        self.rect = self.asset.get_rect(center = (-300,0))
        self.rect.inflate_ip(-self.rect.width // 2, -self.rect.height // 2)
    def set_position(self,pos,pos_col):
        self.rect.center = pos
        if self.dir == 'r':
            self.col_rect.topleft = (pos_col[0],pos_col[1]+14)
        elif self.dir == 'l':
            self.col_rect.topleft = (pos_col[0]-20,pos_col[1]+14)

    def colliderect(self,rect):
        return self.col_rect.colliderect(rect)

    def show(self):
        screen.blit(self.asset, self.rect)
        # pygame.draw.rect(screen,(255,0,0), self.col_rect) 
Spike_Pos_List = [720/12 * i for i in range(12)]
Spikes_l = pygame.sprite.Group()
Spikes_r = pygame.sprite.Group()
def spike_generation(side):
    length = len(Spikes_l)
    pos_list = random.sample(Spike_Pos_List, length)
    if side == "l":
        for i ,Spike_l in enumerate(Spikes_l):
            Spike_l.set_position((Spike_l.rect.width//2, pos_list[i]+Spike_l.size.y/4),(0,pos_list[i]))
    elif side == "r":
        for j, Spike_r in enumerate(Spikes_r):
            Spike_r.set_position((screen_size[0]-Spike_r.rect.width*1.5, pos_list[j]+Spike_r.size.y/4),(screen_size[1],pos_list[j]))
def spike_add():
    global Spikes_l, Spikes_r
    if score.value % 3 == 0 and score.can_add:
        if len(Spikes_l) < 11 and len(Spikes_r) < 11:
            Spike_r = spike("l")
            Spike_l = spike("r")
            Spikes_r.add(Spike_r)
            Spikes_l.add(Spike_l)
            score.can_add = False
# coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = pygame.Vector2(20,20)
        self.assets = GIF_convert("D:\Programowanie\Semestr2\Gra\star coin rotate", self.size)
        self.animation = 0
        self.pos0 = (-100,0)
        self.rect = self.assets[0].get_rect()
        self.rect.center = (500,360)
        self.rect.inflate_ip(self.rect.width / 1.3, self.rect.height / 1.3)
        self.collected = False
        
    def new_position(self):  
        x = random.randint(180,540)
        y = random.randint(60,660)
        vector = (x,y)
        return vector 

    def show(self):
        self.animation %= len(self.assets)
        screen.blit(self.assets[self.animation], self.rect)

    def collect(self):
        self.rect.center = self.pos0
        sound_channel_coin.play(coin_sound)

    def appear(self):
        self.rect.center = self.new_position()
coin = Coin()
# walls
def walls_innit():
    left_wall = pygame.Rect(0, 0, 1, screen_size[1])
    right_wall = pygame.Rect(screen_size[0]-1, 0, 1, screen_size[1])
    top_wall = pygame.Rect(0, -player.size.y, screen_size[0], 1)
    bottom_wall = pygame.Rect(0, screen_size[1]-1+player.size.y, screen_size[0], 1)
    wall_collide_list = [left_wall, right_wall, top_wall, bottom_wall]
    return wall_collide_list
def wall_show():
    for i in range(2):
        pygame.draw.rect(screen, (100,100,100),walls[i])
walls = walls_innit()
# score
class Score():
    def __init__(self,font_size,placement):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.position = (placement)
        self.can_add = True
    
    def show(self):
        self.surface = self.font.render(str(self.value),True,(100,100,100))
        self.rect = self.surface.get_rect(center = self.position)
        screen.blit(self.surface, self.rect)

    def increase(self):
        self.value += 1 
score = Score(score_font_size := 256,(screen_size[0]//2, screen_size[1]//2))
# text boxes
class Text():
    def __init__(self, font_size, placement, text):
        self.text_lines = text.split("\n")
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.position = placement

    def show(self):
        line_height = self.font.get_height()
        for i, line in enumerate(self.text_lines):
            self.surface = self.font.render(str(line), True, (0, 0, 0))
            self.rect = self.surface.get_rect(center=(self.position[0], self.position[1] + i * line_height))
            screen.blit(self.surface, self.rect)
def Read_File(path):
    with open(path,'r') as Odczyt:
        Zawartosc = Odczyt.read()
    return Zawartosc
Text_rules = Text(30,(screen_size[0]//2, screen_size[1]//6),Read_File("D:\Programowanie\Semestr2\Gra\Rules.txt"))
Text_credits = Text(30,(screen_size[0]//2, screen_size[1]//4),Read_File("D:\Programowanie\Semestr2\Gra\Credits.txt"))
Text_player_name = Text(20,(screen_size[0]//2,580),"Wpisz swoj nick")
# high score
best_score = 0
def update_score(score,nick):
    wyniki = []
    names = []
    with open("D:\Programowanie\Semestr2\Gra\BestScores.txt",'r+') as file:
        beef = file.readlines()
        for line in beef:
            wyniki.append(line.split(" ")[-1])
            names.append(line.split(" ")[1])
    with open("D:\Programowanie\Semestr2\Gra\BestScores.txt",'w') as file:
        for i, wynik in enumerate(wyniki):
            if score > int(wynik):
                new_line = "{i}. {nick} {score}\n".format(i=i+1,nick=nick,score=best_score)
                beef.insert(i,new_line)
                while i < 10:
                    corrected_line = "{j}. {nick} {score}".format(j=i+2,nick=names[i],score=wyniki[i])
                    beef.insert(i+1,corrected_line)
                    i += 1
                break
        file.seek(0)
        for i in range(10):
            file.write(beef[i])

for i in range(2):
    score.can_add = True
    spike_add()
for d in ["l","r"]:
    spike_generation(d)

def set_new_game():
    global best_score
    best_score = score.value
    score.value = 0
    score.can_add = True
    player.set_to_start()
    coin.appear()
    Spikes_l.empty()
    Spikes_r.empty()
    for i in range(2):
            score.can_add = True
            spike_add()
    if player.v.x < 0:
        player.turn()
    spike_generation("l")
    spike_generation("r")
    update_score(best_score, player_name.entered_text)

while running:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    
    if game_paused == True:
        screen.fill((134, 57, 250))
        if sound_button.frame == 0:
            for key in sounds:
                # key.set_volume(0)
                pygame.mixer.music.pause()
        elif sound_button.frame == 1:
            for key, value in sounds.items():
                # key.set_volume(value)
                pygame.mixer.music.unpause()
        if menu_state == "main":
            sound_button.show()
            if sound_button.click():
                pass
            if start_button.draw_button():
                game_paused = False
                sound_channel_menu.play(menu_select_sound)
            if bestscores_button.draw_button():
                menu_state = "bestscores"
                sound_channel_menu.play(menu_select_sound)
            if rules_button.draw_button():
                menu_state = "rules"
                sound_channel_menu.play(menu_select_sound)
            if credits_button.draw_button():
                menu_state = "credits"
                sound_channel_menu.play(menu_select_sound)
            if quit_button.draw_button():
                running = False
                sound_channel_menu.play(menu_select_sound)
        if menu_state == "rules":
            Text_rules.show()
            if back_button.draw_button():
                menu_state = "main"
                sound_channel_menu.play(menu_select_sound)
        if menu_state == "credits":
            Text_credits.show()
            if back_button.draw_button():
                menu_state = "main"
                sound_channel_menu.play(menu_select_sound)
        if menu_state == "Game over":
            Text_gameover = Text(60,(screen_size[0]//2,screen_size[1]//3),"GAME OVER\n Your score: {wynik}\n\n Press esc to\n go back to menu".format(wynik=best_score))
            Text_gameover.show()
        if menu_state == "bestscores":
            player_name.show()
            Text_player_name.show()
            Text_bestscores = Text(30,(screen_size[0]//2, screen_size[1]//6),Read_File("D:\Programowanie\Semestr2\Gra\BestScores.txt"))
            Text_bestscores.show()
            if back_button.draw_button():
                menu_state = "main"
                sound_channel_menu.play(menu_select_sound)
        if menu_state == "pause":
            if resume_button.draw_button():
                game_paused = False
                sound_channel_menu.play(menu_select_sound)
            if quit_button.draw_button():
                menu_state = "main"
                set_new_game()
                sound_channel_menu.play(menu_select_sound)
        if keys[K_ESCAPE]:
            menu_state = "main"
    else:
        screen.fill((179,179,179))
        wall_show()
        score.show()
        for x in Spikes_l:
            x.show()
        for x in Spikes_r:
            x.show()
        coin.show()
        player.show()

        player.movement()
        for Spike in Spikes_r:
            if Spike.colliderect(player):
                menu_state = "Game over"
                game_paused = True
                set_new_game()
                sound_channel_death.play(death_sound)
        for Spike in Spikes_l:
            if Spike.colliderect(player):
                menu_state = "Game over"
                game_paused = True
                set_new_game()
                sound_channel_death.play(death_sound)
        if player.colliderect(coin):
            coin.collect()
            coin.collected = True
            score.can_add = True
            score.increase()

        if player.collidelist(walls) in [0,1]:
            spike_add()
            if player.collidelist(walls) == 0:
                spike_generation("r")
            elif player.collidelist(walls) == 1:
                spike_generation("l")
            if coin.collected:
                coin.appear()
                coin.collected = False
            player.turn()
        elif player.collidelist(walls) == 2:
            player.channel("down")
        elif player.collidelist(walls) == 3:
            player.channel("up")

        animation_rate += dt
        if animation_rate > 4*dt:
            player.animation += 1
            coin.animation += 1        
            animation_rate = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player_name.write(event)
            if event.key == pygame.K_p:
                game_paused = True
                menu_state = "pause"
        else:
            player_name.write(event)

    pygame.display.flip() 

pygame.quit()