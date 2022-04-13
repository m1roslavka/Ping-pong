from pygame import *

font.init()


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_y, player_speed_x):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_y = player_speed_y
        self.speed_x = player_speed_x
        self.width = player_width
        self.height = player_height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Gamesprite):
    def moving1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pressed[K_s] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed_y

    def moving2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pressed[K_DOWN] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed_y


class Ball(Gamesprite):
    def ball_moving(self):
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= win_height - 40:
            self.speed_y *= -1
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    def ball_collide(self):
        self.speed_x *= -1


blue = (0, 168, 178)
black = (0, 0, 0)

# Создание окна
win_width = 1200
win_height = 600
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
display.set_caption('Пин-Понг')
clock = time.Clock()

# Создание персонажей
rocket1 = Player('ball.png', 50, 200, 20, 200, 3, 0)
rocket2 = Player('ball.png', 1130, 200, 20, 200, 3, 0)
ball = Ball('ball.png', 585, 285, 30, 30, 4, 4)

# Создание шрифта
font = font.Font(None, 80)
f_l = font.render('ЛЕВЫЙ ПОБЕДИЛ', True, (255, 255, 255))
f_r = font.render('ПРАВЫЙ ПОБЕДИЛ', True, (255, 255, 255))

finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.blit(background, (0, 0))

        rocket1.reset()
        rocket1.moving1()
        rocket2.reset()
        rocket2.moving2()
        ball.reset()
        ball.ball_moving()

        if sprite.collide_rect(rocket1, ball):
            ball.ball_collide()

        if sprite.collide_rect(rocket2, ball):
            ball.ball_collide()

        if ball.rect.x <= -40:
            window.blit(f_r, (330, 250))
            finish = True

        if ball.rect.x >= win_width + 10:
            window.blit(f_l, (340, 250))
            finish = True

    else:
        finish = False
        time.delay(2000)
        ball.rect.x = 585
        ball.rect.y = 285
        rocket1.rect.x = 50
        rocket1.rect.y = 200
        rocket2.rect.x = 1130
        rocket2.rect.y = 200

    display.update()
    clock.tick(90)
