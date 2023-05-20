from pygame import * 
w = 900 
h = 740 
window = display.set_mode((w,h))  
display.set_caption("Пінг-Понг") 
background = transform.scale(image.load("pic.jpg"),(w,h)) 
font.init() 
font1 = font.Font(None, 60) 
FPS = 65 
clock = time.Clock() 
p1_win = font1.render("PLAYER 1 WIN!", True, (232, 251, 200)) 
p2_win = font1.render("PLAYER 2 WIN!", True, (232, 251, 200)) 
class Player(sprite.Sprite): 
    def init(self, hidth, weight, player_image, player_x, player_y,): 
        super().__init__() 
        self.hidth = hidth 
        self.weigth = weight 
        self.image = transform.scale(image.load(player_image),(hidth,weight)) 
        self.rect = self.image.get_rect() #Створити рамку навколо картинки спрайту 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self):#Функція для тоого щоб намалювати спрайт на екрані 
        window.blit(self.image,(self.rect.x, self.rect.y)) 
class Raket_l(Player): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y >= 30: 
            self.rect.y -= 4 
        if keys[K_DOWN] and self.rect.y <= 570: 
            self.rect.y += 4 
class Raket_r(Player): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y >= 30: 
            self.rect.y -= 4 
        if keys[K_s] and self.rect.y <= 570: 
            self.rect.y += 4 
game = True 
raket_r = Raket_r(30,170,"platform_left.png",30,340) 
raket_l = Raket_l(30,170,"platform_right.png",840,340) 
ball = Player(50,50,"Ball_pic.png",300,200) 
finish = False 
dx = 4 
dy = 4 
while game: 
    window.blit(background,(0,0)) 
    for e in event.get():    
        if e.type == QUIT:    
            game = False   
    if finish != True: 
        raket_r.update() 
        raket_l.update() 
        ball.reset() 
        raket_r.reset() 
        raket_l.reset() 
        ball.reset()
        ball.rect.x += dx 
        ball.rect.y += dy 
        if ball.rect.x == raket_l.rect.x or ball.rect.x == raket_r.rect.x: 
            dx = -dx*1.0025 
        if ball.rect.y == raket_l.rect.y or ball.rect.y == raket_r.rect.y: 
            dy = -dy*1.0025
        if ball.rect.y >= 600 or ball.rect.y <= 30: 
            dy = -dy*1.0025
        if ball.rect.x == 870: 
            finish = True 
        if ball.rect.x == 5: 
            finish = True  
    clock.tick(FPS) 
    display.update()
