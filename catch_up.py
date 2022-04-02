from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(55, 55))
        self.speed = player_speed
        self.rect =  self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if knopka1[K_d]:
            self.rect.x += self.speed 
            ojk=1
        if knopka2[K_a]:
            self.rect.x -= self.speed 
            ojk=11
        if knopka3[K_w]:
            yplayer_y1 -= self.rect.y
            ojk=2
        if knopka4[K_s]:
            yplayer_y1 += self.rect.y
            ojk=22
class Enemy(GameSprite):
    def update(self):
       if self.rect.x <= 470:
           self.side = "right"
       if self.rect.x>= win_win_widht - 85:
           self.side = 'left'
       if self.side == "left":
           self.rect.x -= self.speed
       else:
            self.rect.x += self.speed
class wall(sprite.Sprite):
    def __init__(self,color_1, color_2, color_3, wall_y, wall_x,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        self.rect  = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x , self.rect.y))
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background =  transform.scale(image.load('ggg.png'), (win_width, win_height))

player = Player('ggg.png',5, win_height - 80, 4)
player = Player('fff.png',5, win_height - 80, 4)
player = Player('qqq.png',5, win_height - 80, 4)
player = Player('rrr.png',5, win_height - 80, 4)
monster = Enemy('qqq.png', win_width - 80,280,2)
monster = Enemy('qqq.png', win_width - 80,280,2)
final = GameSprite('qqq.png', win_width - 120,6,60)
       

okno = display.set_mode((500,500))
display.set_caption("...")

backgrond = image.load("zlthysq_dphsd.jpg")
backgrond = transform.scale(backgrond,(500,500))
okno.blit(backgrond,(0,0))
stena = image.load("qqq.png")

sten = transform.scale(stena,(10,50))
stens = transform.scale(stena,(50,10))

gr = image.load("fff.png")
gr = transform.scale(gr,(20,10))
gr1 = image.load("ggg.png")
gr1 = transform.scale(gr1,(20,10))
clock = time.Clock()
gr2 = image.load("qqq.png")
gr2 = transform.scale(gr2,(10,20))
gr3 = image.load("rrr.png")
gr3 = transform.scale(gr3,(10,20))
clock = time.Clock()
FPS = 60
x1 = 20
x2 = 0
w=wall(255,255,255,0,45,2,400)
w1=wall(255,255,255,420,45,2,400)
w2=wall(255,255,255,420,45,50,2)
w3=wall(255,255,255,400,45,50,2)
y1=30
y2=0
##y2 = 0
game = True
ojk=1
speed=5
while game:
    window.blit(backgrond,(0,0))
    w.draw_wall()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()

    '''
    
    '''
    
    
    

    for i in event.get():
        if i.type == QUIT:
            game = False
    knopka1 = key.get_pressed()
    knopka2 = key.get_pressed()
    knopka3 = key.get_pressed()
    knopka4 = key.get_pressed()

    if knopka1[K_d]:
        x1 += speed
        ojk=1
    if knopka2[K_a]:
        x1 -= speed
        ojk=11
    
    if knopka3[K_w]:
        y1 -= speed
        ojk=2
    if knopka4[K_s]:
        y1 += speed
        ojk=22
    # y1 += 10

    
    if ojk==1:
        okno.blit(gr, (x1,y1))
    elif ojk==11:
        okno.blit(gr1, (x1,y1))
    elif ojk==2:
        okno.blit(gr2, (x1,y1))
    else:
        okno.blit(gr3, (x1,y1))
    '''
    if sprite.collide_rect(player, w) or sprite.collide_rect(player, w1) or sprite.collide_rect(playerman, w2) or sprite.collide_rect(player, w3):
        game = False'''
    display.update()
    clock.tick(FPS)
          
