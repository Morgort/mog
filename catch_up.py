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
3, (x1,y1))
    '''
    if sprite.collide_rect(player, w) or sprite.collide_rect(player, w1) or sprite.collide_rect(playerman, w2) or sprite.collide_rect(player, w3):
        game = False'''
    display.update()
    clock.tick(FPS)
          
