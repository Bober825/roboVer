from pygame import *

win_width = 700
win_height = 500
ct = 0
ctm = 0
img_triger = 0
exp_anim = 0
rtex = 0
exp_anim_trig = False

window = display.set_mode((win_width, win_height))
display.set_caption('Labirint')
pic = transform.scale(image.load('./pygame/images/object_map/background.png'), (win_width, win_height))
go_close = False
fp = 1
aip_stan_right_1 = './pygame/images/player_sprite/TV_bot_v3_stAN1_right.png'
aip_stan_right_2 = './pygame/images/player_sprite/TV_bot_v3_stAN2_right.png'
aip1_right ='./pygame/images/player_sprite/TV_bot_v3_AN1.png'
aip2_right ='./pygame/images/player_sprite/TV_bot_v3_AN2.png'

aip_stan_back_1 = './pygame/images/player_sprite/TV_bot_v3_stAN1_back.png'
aip_stan_back_2 = './pygame/images/player_sprite/TV_bot_v3_stAN2_back.png'
aip1_back ='./pygame/images/player_sprite/TV_bot_v3_AN1_Back.png'
aip2_back ='./pygame/images/player_sprite/TV_bot_v3_AN2_Back.png'

aip_stan_down_1 = './pygame/images/player_sprite/TV_bot_v3_stAN1_down.png'
aip_stan_down_2 = './pygame/images/player_sprite/TV_bot_v3_stAN2_down.png'
aip1_down ='./pygame/images/player_sprite/TV_bot_v3_AN1_down.png'
aip2_down ='./pygame/images/player_sprite/TV_bot_v3_AN2_down.png'

aip_stan_left_1 = './pygame/images/player_sprite/TV_bot_v3_stAN1_left.png'
aip_stan_left_2 = './pygame/images/player_sprite/TV_bot_v3_stAN2_left.png'
aip1_left ='./pygame/images/player_sprite/TV_bot_v3_AN1_left.png'
aip2_left ='./pygame/images/player_sprite/TV_bot_v3_AN2_left.png'
aip3_left ='./pygame/images/player_sprite/TV_bot_v3_AN3_left.png'
aip4_left ='./pygame/images/player_sprite/TV_bot_v3_AN4_left.png'

contf_1 = './pygame/images/contaminated_TV_png/Сonta_TV-frame-1.png'
contf_2 = './pygame/images/contaminated_TV_png/Сonta_TV-frame-2.png'
contf_3 = './pygame/images/contaminated_TV_png/Сonta_TV-frame-3.png'
contf_4 = './pygame/images/contaminated_TV_png/Сonta_TV-frame-4.png'

lazdro_st = './pygame/images/LAZER_drone/LAZER_drone.png'
lazdro_1 = './pygame/images/LAZER_drone/LAZER_drone_AN1.png'
lazdro_2 = './pygame/images/LAZER_drone/LAZER_drone_AN2.png'
lazdro_3 = './pygame/images/LAZER_drone/LAZER_drone_AN3.png'
lazdro_4 = './pygame/images/LAZER_drone/LAZER_drone_AN4.png'

exp_1 = './pygame/images/effect_object/explos_AN_s1.png'
exp_2 = './pygame/images/effect_object/explos_AN_s2.png'
exp_3 = './pygame/images/effect_object/explos_AN_s3.png'
exp_4 = './pygame/images/effect_object/explos_AN_s4.png'
exp_5 = './pygame/images/effect_object/explos_AN_s5.png'
exp_6 = './pygame/images/effect_object/explos_AN_s6.png'
exp_7 = './pygame/images/effect_object/explos_AN_s7.png'
exp_8 = './pygame/images/effect_object/explos_AN_s8.png'





class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Efect(GameSprite):
    def __init__(self, ff, exp_1_AN, exp_2_AN, exp_3_AN, exp_4_AN, exp_5_AN, exp_6_AN, exp_7_AN, exp_8_AN, x, y, width, height,):
        super().__init__(ff, x, y, width, height)
        self.eAN1 = transform.scale(image.load(exp_1_AN), (width, height))
        self.eAN2 = transform.scale(image.load(exp_2_AN), (width, height))
        self.eAN3 = transform.scale(image.load(exp_3_AN), (width, height))
        self.eAN4 = transform.scale(image.load(exp_4_AN), (width, height))
        self.eAN5 = transform.scale(image.load(exp_5_AN), (width, height))
        self.eAN6 = transform.scale(image.load(exp_6_AN), (width, height))
        self.eAN7 = transform.scale(image.load(exp_7_AN), (width, height))
        self.eAN8 = transform.scale(image.load(exp_8_AN), (width, height))
        self.ff = transform.scale(image.load(ff), (width, height))

        self.am = 1

    def animation_exp (self):
        if self.am == 1:
            self.image = self.eAN1
            self.am = 2
            return
        
        if self.am == 2:
            self.image = self.eAN2
            self.am = 3
            return
        
        if self.am == 3:
            self.image = self.eAN3
            self.am = 4
            return
        
        if self.am == 4:
            self.image = self.eAN4
            self.am = 5
            return
        
        if self.am == 5:
            self.image = self.eAN5
            self.am = 6
            return
        
        if self.am == 6:
            self.image = self.eAN6
            self.am = 7
            return
        
        if self.am == 7:
            self.image = self.eAN7
            self.am = 8
            return
        
        if self.am == 8:
            self.image = self.eAN8
            self.am = 9
            return
        
        if self.am == 9:
            self.image = self.ff
            self.am = 1
            return

    

    
        



class Bullet(GameSprite):
    def __init__(self, picture, x, y, width, height, speed_x, speed_y, rotate):
        super().__init__(picture, x, y, width, height)
        self.image = transform.rotate(self.image, rotate)
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > win_width - 40:
            self.kill()
        if self.rect.y > win_height - 40:
            self.kill()

class lazer(GameSprite):
    def __init__(self, picture, x, y, width, height, speed_x, speed_y, rotate):
        super().__init__(picture, x, y, width, height)
        self.image = transform.rotate(self.image, rotate)
        self.lt = 0
    def update(self):
        if self.lt == 15:
            self.kill()
        self.lt += 1
    
    

class Player(GameSprite):
    def __init__(self, picture_stan1_right, picture_stan2_right, picture1, picture2, picture_stan1_back, picture_stan2_back,picture1_back, picture2_back, picture_stan1_down, picture_stan2_down, picture1_down, picture2_down, picture_stan1_left, picture_stan2_left, picture1_left, picture2_left, picture3_left, picture4_left, x, y, width, height, x_speed = 0, y_speed = 0):
        super().__init__(picture_stan1_right, x, y, width, height)
        
        self.image_stan1_an_right = transform.scale(image.load(picture_stan1_right), (width, height))
        self.image_stan2_an_right = transform.scale(image.load(picture_stan2_right), (width, height))
        self.image1an_right = transform.scale(image.load(picture1), (width, height))
        self.image2an_right = transform.scale(image.load(picture2), (width, height))

        self.image_stan1_an_back = transform.scale(image.load(picture_stan1_back), (width, height))
        self.image_stan2_an_back = transform.scale(image.load(picture_stan2_back), (width, height))
        self.image1an_back = transform.scale(image.load(picture1_back), (width, height))
        self.image2an_back = transform.scale(image.load(picture2_back), (width, height))

        self.image_stan1_an_down = transform.scale(image.load(picture_stan1_down), (width, height))
        self.image_stan2_an_down = transform.scale(image.load(picture_stan2_down), (width, height))
        self.image1an_down = transform.scale(image.load(picture1_down), (width, height))
        self.image2an_down = transform.scale(image.load(picture2_down), (width, height))

        self.image_stan1_left = transform.scale(image.load(picture_stan1_left), (width, height))
        self.image_stan2_left = transform.scale(image.load(picture_stan2_left), (width, height))
        self.image1an_left = transform.scale(image.load(picture1_left), (width, height))
        self.image2an_left = transform.scale(image.load(picture2_left), (width, height))
        self.image3an_left = transform.scale(image.load(picture3_left), (width, height))
        self.image4an_left = transform.scale(image.load(picture4_left), (width, height))

        self.height = height
        self.width = width
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.am_stan = 1
        self.am = 1
        self.sap = 1
        self.am_back = 1
        self.am_down = 1
        
    def fire_left(self):
        
        bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.left + 16, self.rect.centery, 21, 21, -15, 0, 180)
        bullets.add(bullet)

    def fire_right(self):
        bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.right - 13, self.rect.centery - 4, 21, 21, 15, 0, 0)
        bullets.add(bullet)

    def fire_up(self):
        bullet_sw = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.x + 5, self.rect.y - self.width / 21, 21, 20, 0, -15, 90)
        bullets_w.add(bullet_sw)

    def fire_down(self):
        bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.x + self.height / 2, self.rect.y + self.width - 10, 21, 20, 0, 15, 270)
        bullets.add(bullet)
 
    
    def update(self):
        if self.rect.x <= win_width - 80 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        
        platform_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platform_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0:
            for p in platform_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        
        if self.rect.y <= win_height - 85 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        
        platform_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platform_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top) 
        elif self.y_speed < 0:
            for p in platform_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        platform_touched = sprite.spritecollide(self, explos_barrel, False)
        if self.y_speed > 0:
            for p in platform_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top) 
        elif self.y_speed < 0:
            for p in platform_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

    def animation(self):
        if self.x_speed > 0:
            if self.am == 1:
                self.image = self.image1an_right
                self.am = 2
                self.sap = 1
                return
            if self.am == 2:
                self.image = self.image2an_right
                self.am = 1
                self.sap = 1
                return
                
        if self.x_speed < 0:
            if self.am == 1:
                self.image = self.image1an_left
                self.am = 2
                self.sap = 2
                return
            if self.am == 2:
                self.image = self.image2an_left
                self.am = 3
                self.sap = 2
                return
            if self.am == 3:
                self.image = self.image3an_left
                self.am = 4
                self.sap = 2
                return
            if self.am == 4:
                self.image = self.image4an_left
                self.am = 1
                self.sap = 2
                return
                
        if self.y_speed < 0:
            if self.am_back == 1:
                self.image = self.image1an_back
                self.am_back = 2
                self.sap = 3
                return
            if self.am_back == 2:
                self.image = self.image2an_back
                self.am_back = 1
                self.sap = 3
                return
            
        if self.y_speed > 0:
            if self.am_down == 1:
                self.image = self.image1an_down
                self.am_down = 2
                self.sap = 4
                return
            if self.am_down == 2:
                self.image = self.image2an_down
                self.am_down = 1
                self.sap = 4
                return
            
        if self.x_speed == 0:
            if self.sap == 1:
                if self.am_stan == 1:
                    self.image = self.image_stan1_an_right
                    self.am_stan = 2
                    return
                if self.am_stan == 2:
                    self.image = self.image_stan2_an_right
                    self.am_stan = 1
                    return
            
            if self.sap == 2:
                if self.am_stan == 1:
                    self.image = self.image_stan1_left
                    self.am_stan = 2
                    return
                if self.am_stan == 2:
                    self.image = self.image_stan2_left
                    self.am_stan = 1
                    return

        if self.y_speed == 0:
            if self.sap == 3:
                if self.am_stan == 1:
                    self.image = self.image_stan1_an_back
                    self.am_stan = 2
                    return
                if self.am_stan == 2:
                    self.image = self.image_stan2_an_back
                    self.am_stan = 1
                    return
                 
            if self.sap == 4:
                if self.am_stan == 1:
                    self.image = self.image_stan1_an_down
                    self.am_stan = 2
                    return
                if self.am_stan == 2:
                    self.image = self.image_stan2_an_down
                    self.am_stan = 1
                    return
        

class Enemy_Drone(GameSprite):
    def __init__(self, picture_st, picture1, picture2, picture3, picture4, x, y, width, height, speed):
        super().__init__(picture_st, x, y, width, height)
        self.image_anim_st = transform.scale(image.load(picture_st), (width, height))
        self.image_anim_1 = transform.scale(image.load(picture1), (width, height))
        self.image_anim_2 = transform.scale(image.load(picture2), (width, height))
        self.image_anim_3 = transform.scale(image.load(picture3), (width, height))
        self.image_anim_4 = transform.scale(image.load(picture4), (width, height))
        self.side = 1
        self.am = 1
        self.speed = speed
        self.shbul = 0
        self.dt = False
    
    def update(self, x1, x2, y1, y2, trigger_y):
        '''
        if self.rect.y <= y1:
            self.side = 2
        if self.rect.y >= y2:
            self.side = 1
        
        if self.side == 1:
            self.rect.x -= self.speed
            if self.shbul >= 15:
                bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.left + 16, self.rect.centery, 21, 21, -15, 0, 180)
                bullets_en.add(bullet)
                self.shbul = 0
                
        elif self.side == 2:
            self.rect.x += self.speed
            if self.shbul >= 15:
                bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.right - 13, self.rect.centery - 4, 21, 21, 15, 0, 0)
                bullets_en.add(bullet)
                self.shbul = 0
        '''

        if trigger_y:
            if self.rect.y <= y1:
                self.side = 2
            if self.rect.y >= y2:
                self.side = 1
            if self.side == 1:
                self.rect.y -= self.speed
            elif self.side == 2:
                self.rect.y += self.speed
            if self.shbul >= 15 and self.dt != True:
                bullet = Bullet('./pygame/images/projectile_sprite/qnt_bulet.png', self.rect.left + 16, self.rect.centery, 21, 21, -15, 0, 180)
                bullets_en_qnt.add(bullet)
                self.shbul = 0


    def animation_d(self):
        if self.side == 1:
            if self.am == 1:
                self.image = self.image_anim_1
                self.am = 2
                return
            if self.am == 2:
                self.image = self.image_anim_2
                self.am = 3
                return
            if self.am == 3:
                self.image = self.image_anim_3
                self.am = 4
                return
            if self.am == 4:
                self.image = self.image_anim_4
                self.am = 1
                return
            
                
        if self.side == 2:
            if self.am == 1:
                self.image = self.image_anim_4
                self.am = 2
                return
            if self.am == 2:
                self.image = self.image_anim_3
                self.am = 3
                return
            if self.am == 3:
                self.image = self.image_anim_2
                self.am = 4
                return
            if self.am == 4:
                self.image = self.image_anim_1
                self.am = 1
                return
class Enemy(GameSprite):
    def __init__(self, picture1, picture2, picture3, picture4, x, y, width, height, speed):
        super().__init__(picture1, x, y, width, height)

        self.image_anim_1 = transform.scale(image.load(picture1), (width, height))
        self.image_anim_2 = transform.scale(image.load(picture2), (width, height))
        self.image_anim_3 = transform.scale(image.load(picture3), (width, height))
        self.image_anim_4 = transform.scale(image.load(picture4), (width, height))
        self.side = 1
        self.am = 1
        self.speed = speed
        self.shbul = 0
    
    def update(self, x1, x2, y1, y2, trigger_y):
        if self.rect.x <= x1:
            self.side = 2
        if self.rect.x >= x2:
            self.side = 1

        if self.side == 1:
            self.rect.x -= self.speed
            if self.shbul >= 15 and self.alive():
                bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.left + 16, self.rect.centery, 21, 21, -15, 0, 180)
                bullets_en.add(bullet)
                self.shbul = 0
                
        elif self.side == 2:
            self.rect.x += self.speed
            if self.shbul >= 15 and self.alive():
                bullet = Bullet('./pygame/images/projectile_sprite/en_bulet.png', self.rect.right - 13, self.rect.centery - 4, 21, 21, 15, 0, 0)
                bullets_en.add(bullet)
                self.shbul = 0




        '''
        if trigger_y:
            if self.rect.y <= y1:
                self.side = 'up'
            if self.rect.y >= y2:
                self.side = 'down'
            if self.side == 'up':
                self.rect.y -= self.speed
            elif self.side == 'down':
                self.rect.y += self.speed
        ''' 

    def animation_m(self):
        if self.side == 1:
            if self.am == 1:
                self.image = transform.flip(self.image_anim_1, True, False)
                self.am = 2
                return
            if self.am == 2:
                self.image =transform.flip(self.image_anim_2, True, False)
                self.am = 3
                return
            if self.am == 3:
                self.image = transform.flip(self.image_anim_3, True, False)
                self.am = 4
                return
            if self.am == 4:
                self.image = transform.flip(self.image_anim_4, True, False)
                self.am = 1
                return
            
                
        if self.side == 2:
            if self.am == 1:
                self.image = self.image_anim_1
                self.am = 2
                return
            if self.am == 2:
                self.image = self.image_anim_2
                self.am = 3
                return
            if self.am == 3:
                self.image = self.image_anim_3
                self.am = 4
                return
            if self.am == 4:
                self.image = self.image_anim_4
                self.am = 1
                return
                


    
    

wall2 = GameSprite('./pygame/images/wall/wall_cheh_w.png', 370, 100, 60, 400)
wall1 = GameSprite('./pygame/images/wall/wall_cheh_h.png', win_width / 2 - win_width / 3 - 23, win_height / 2, 300, 60)

win_wall_2 = GameSprite('./pygame/images/object_map/pixil-frame-0.png', 0, 0, 700, 10)
win_wall_1 = GameSprite('./pygame/images/object_map/pixil-frame-0.png', 0, 0, 18, 500)
facke_bulet = GameSprite('./pygame/images/object_map/pixil-frame-0.png', 0, 0, 1, 1)
facke_bulet_w = GameSprite('./pygame/images/object_map/pixil-frame-0.png', 0, 0, 1, 1)
bullet = GameSprite('./pygame/images/object_map/pixil-frame-0.png', 0, 0, 1, 1)

Crash_block = sprite.Group()
barriers = sprite.Group()
bullets = sprite.Group()
bullets_w = sprite.Group()
enemy_bot = sprite.Group()
explos_barrel = sprite.Group()
bullets_en = sprite.Group()
bullets_en_qnt = sprite.Group()
dron = sprite.Group()

barriers.add(win_wall_1)
barriers.add(win_wall_2)
barriers.add(wall2)
barriers.add(wall1)

bullets.add(facke_bulet)
bullets_w.add(facke_bulet_w)

px, py = 30, 410
e1x, e1y = win_width - 80, 180
e2x, e2y = 420, 300
pxp, pyp = (5, 400)
e1xp, e1xyp = (win_width - 80, 180)
e2xp, e2yp = (420, 300)

lazer_drone = Enemy_Drone (lazdro_st, lazdro_1, lazdro_2, lazdro_3, lazdro_4, win_width - 63, win_height - 63, 63, 63, 6)
player = Player(aip_stan_right_1, aip_stan_right_2, aip1_right, aip2_right, aip_stan_back_1, aip_stan_back_2, aip1_back, aip2_back, aip_stan_down_1, aip_stan_down_2, aip1_down, aip2_down, aip_stan_left_1, aip_stan_left_2, aip1_left, aip2_left, aip3_left, aip4_left, px, py, 54, 68)
monster1 = Enemy(contf_1, contf_2, contf_3, contf_4, e1x, e1y, 60, 60, 3)
monster2 = Enemy(contf_1, contf_2, contf_3, contf_4, e2x, e2y, 60, 60, 3)
final = GameSprite('./pygame/images/object_map/teleport_finish.png', win_width - 110, win_height - 90, 60, 70)
ebarrel = GameSprite('./pygame/images/object_map/explos_barrel.png', 375, 35, 50, 60)
explore = Efect('./pygame/images/object_map/pixil-frame-0.png', exp_1, exp_2, exp_3, exp_4, exp_5, exp_6, exp_7, exp_8, ebarrel.rect.x - 50, ebarrel.rect.y - 50, ebarrel.width + 95, ebarrel.height + 95)

enemy_bot.add(monster1)
enemy_bot.add(monster2)
dron.add(lazer_drone)

explos_barrel.add(ebarrel)

run = True
finish_1 = False
finish_2 = False
finish_3 = False

fp = 1 
while run:
    time.delay(40)

    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if go_close:
                go_close = False
                img_triger = 0
                player = Player(aip_stan_right_1, aip_stan_right_2, aip1_right, aip2_right, aip_stan_back_1, aip_stan_back_2, aip1_back, aip2_back, aip_stan_down_1, aip_stan_down_2, aip1_down, aip2_down, aip_stan_left_1, aip_stan_left_2, aip1_left, aip2_left, aip3_left, aip4_left, px, py, 54, 68)                
                explore = Efect('./pygame/images/object_map/pixil-frame-0.png', exp_1, exp_2, exp_3, exp_4, exp_5, exp_6, exp_7, exp_8, ebarrel.rect.x - 50, ebarrel.rect.y - 50, ebarrel.width + 95, ebarrel.height + 95)
                monster1.kill()
                monster2.kill()
                ebarrel.kill()
                lazer_drone.kill()
                bullet.kill()
                enemy_bot.add(monster1)
                enemy_bot.add(monster2)
                explos_barrel.add(ebarrel)
                dron.add(lazer_drone)
                rtex = 0


            if e.key == K_RIGHT or e.key == K_d:        
                player.x_speed = 7
                fp = 1 
            elif e.key == K_LEFT or e.key == K_a:        
                player.x_speed = -7
                fp = 2
            elif e.key == K_UP or e.key == K_w:        
                player.y_speed = -7
                fp = 3
            elif e.key == K_DOWN or e.key == K_s:        
                player.y_speed = 7
                fp = 4
            elif e.key == K_SPACE:
                if fp == 1:
                    player.fire_right()
                elif fp == 2:
                    player.fire_left()
                elif fp == 3:
                    player.fire_up()
                elif fp == 4:
                    player.fire_down()
                
        elif e.type == KEYUP:
            if e.key == K_RIGHT or e.key == K_d:
                player.x_speed = 0
            elif e.key == K_LEFT or e.key == K_a:
                player.x_speed = 0
            elif e.key == K_UP or e.key == K_w:
                player.y_speed = 0
            elif e.key == K_DOWN or e.key == K_s:
                player.y_speed = 0

    
   
    sprite.groupcollide(enemy_bot, bullets, True, True)
    sprite.groupcollide(bullets, barriers, True, False)
    sprite.groupcollide(Crash_block, bullets, True, True)
    if sprite.groupcollide(explos_barrel, bullets, True, True):
        exp_anim_trig = True
        if player.rect.x + player.width <= ebarrel.rect.x + ebarrel.height + 90 and player.rect.x + player.width >= ebarrel.rect.x - 90:
            if player.rect.y + player.height <= ebarrel.rect.y + ebarrel.height + 90 and player.rect.y + player.height >= ebarrel.rect.y - 90:
                finish_1 = False
                img_triger = 1
                player.x_speed = 0
                player.y_speed = 0
                go_close = True
    if sprite.groupcollide(explos_barrel, bullets_w, True, True):
        exp_anim_trig = True
        if player.x + player.width <= ebarrel.rect.x + ebarrel.height + 90 and player.x + player.width >= ebarrel.rect.x - 90:
            if player.y + player.height <= ebarrel.rect.y + ebarrel.height + 90 and player.y + player.height >= ebarrel.rect.y - 90:
                finish_1 = False
                img_triger = 1
                player.x_speed = 0
                player.y_speed = 0
                go_close = True
    sprite.groupcollide(enemy_bot, bullets_w, True, True)
    sprite.groupcollide(bullets_w, barriers, True, False)
    sprite.groupcollide(Crash_block, bullets_w, True, True)
    sprite.groupcollide(bullets_en, barriers, True, False)
    
    
    if not finish_1:
        window.blit(pic, (0, 0))
        dron.draw(window)
        barriers.draw(window)
        enemy_bot.draw(window)
        bullets_w.draw(window)
        explos_barrel.draw(window)
        player.reset()
        final.reset()
        explore.reset()
        

        
        bullets.draw(window)
        bullets_en.draw(window)
        bullets_en_qnt.draw(window)

        player.update()
        if ct >= 4:
            player.animation()
            ct = 0

        if exp_anim >= 2:
            explore.animation_exp()
            exp_anim = 0
            rtex += 1
            if rtex >= 9:
                exp_anim_trig = False

        
        bullets.update()
        bullets_w.update()
        bullets_en.update()
        bullets_en_qnt.update()
        

        monster2.update(420, win_width - 95, 0, 0, False)
        lazer_drone.update(0, 0, 0, win_height - lazer_drone.height, True)
        monster1.update(420, win_width - 95, 0, 0, False)

        if ctm >= 4:
            monster1.animation_m()
            monster2.animation_m()
            lazer_drone.animation_d()
            ctm = 0

        
        if sprite.spritecollide(player, enemy_bot, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.spritecollide(player, bullets_en, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.spritecollide(player, bullets_en_qnt, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.collide_rect(player, final):
            finish_1 = True
            img_triger = 2

    if not finish_1:
        window.blit(pic, (0, 0))
        dron.draw(window)
        barriers.draw(window)
        enemy_bot.draw(window)
        bullets_w.draw(window)
        explos_barrel.draw(window)
        player.reset()
        final.reset()
        explore.reset()
        

        
        bullets.draw(window)
        bullets_en.draw(window)
        bullets_en_qnt.draw(window)

        player.update()
        if ct >= 4:
            player.animation()
            ct = 0

        if exp_anim >= 2:
            explore.animation_exp()
            exp_anim = 0
            rtex += 1
            if rtex >= 9:
                exp_anim_trig = False

        
        bullets.update()
        bullets_w.update()
        bullets_en.update()
        bullets_en_qnt.update()
        

        monster2.update(420, win_width - 95, 0, 0, False)
        lazer_drone.update(0, 0, 0, win_height - lazer_drone.height, True)
        monster1.update(420, win_width - 95, 0, 0, False)

        if ctm >= 4:
            monster1.animation_m()
            monster2.animation_m()
            lazer_drone.animation_d()
            ctm = 0

        
        if sprite.spritecollide(player, enemy_bot, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.spritecollide(player, bullets_en, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.spritecollide(player, bullets_en_qnt, False):
            finish_1 = False
            img_triger = 1
            player.x_speed = 0
            player.y_speed = 0
            go_close = True

        if sprite.collide_rect(player, final):
            finish_1 = True
            img_triger = 2
        
    ct += 1
    ctm += 1 
    monster1.shbul += 1
    monster2.shbul += 1
    lazer_drone.shbul += 1
    if img_triger == 1:
        img = image.load('./pygame/images/object_map/game_over.png')
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    if img_triger == 2:
        img = image.load('./pygame/images/object_map/winner.png')
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    if exp_anim_trig:
        exp_anim += 1 

    display.update()
    
