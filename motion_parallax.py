from graphics import graphics
import random

def gradient_color_randomizer():
#chooses randomized colors for the mountains

    red = random.randint(0,255)
    green= random.randint(0,255)
    blue = random.randint(0,255)
    return red,green,blue

def color_gradient(color_value1,color_value2):
    #here we do a calculation to determine color values and gradients
    color_difference = color_value2 - color_value1
    if color_difference < 0:
        color_change = -1
    elif color_difference > 0:
        color_change = 1
    else:
        color_change = 0

    if color_difference != 0:
            modulus = int((1/(abs(color_difference)/700)))+1
    else:
        modulus = 1
    return color_change, modulus

def gradient_layer(gui, red1, green1, blue1, red2, green2, blue2):
    red_change, red_modulus = color_gradient(red1,red2)
    green_change, green_modulus = color_gradient(green1,green2)
    blue_change, blue_modulus = color_gradient(blue1,blue2)
    y_gradient = 1
    while y_gradient <= 700:
        color = gui.get_color_string(red1,green1,blue1)
        gui.line(0,y_gradient,700,y_gradient,color,1)
        if y_gradient % red_modulus == 1:
            red1 + red_change
        if y_gradient % green_modulus == 1:
            green1 + green_change
        if y_gradient % blue_modulus == 1:
            blue1 + blue_change
        y_gradient += 1


def random_color(gui):
    #return a random color
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return gui.get_color_string(red,blue,green)

def sun(gui):
    #animates the sun with mouse movement
    x = (gui.mouse_x//50)+343
    y = (gui.mouse_y//50)+343
    gui.ellipse(x+150, y-250,100,100,'yellow')

#animates the mountain
def first_mountain(gui,first_color):
    x = (gui.mouse_x//30)+338
    y = (gui.mouse_y//30)+338
    gui.traingle(x-250,y+350,x,y-150,x+250,y+350,first_color)

#animates the mountain
def second_third_mountain(gui,second_color,third_color):
    x = (gui.mouse_x//14)+325
    y = (gui.mouse_y//14)+325
    gui.triangle(x-600, y+412, x-200,y-100,x+200,y+412,second_color)
    gui.triangle(x - 200, y + 412, x +200, y - 100, x + 600, y + 412, second_color)

def foreground(gui):
    x = (gui.mouse_x//5)+280
    y = (gui.mouse_y//5)+280
    gui.rectangle(x-500,y+250,1000,500, 'spring green3')
    x_grass = -2
    while x_grass < 710:
        gui.line(x_grass,y+220,x_grass,y+250,'spring green3',3)
        x_grass += 7
    gui.rectangle(x+130,y+220,30,100,'saddle brown')
    gui.ellipse(x+145,y+175,100,150,'forest green')

def birds(gui,x_bird):
    i = 0
    y_bird = 200
    while i < 5:
        gui.line(x_bird-25,y_bird-10,x_bird,y_bird,'black',4)
        gui.line(x_bird+25,y_bird-10,x_bird,y_bird,'black',4)
        i += 1
        x_bird -= 100
        y_bird -= 25

def main():
    gui = graphics(700,700,'Landscape')
    red1,green1,blue1 = gradient_color_randomizer()
    red2,green2,blue2 = gradient_color_randomizer()
    first_color = random_color(gui)
    second_color = random_color(gui)
    third_color = random_color(gui)
    x_bird = 450
    while True:
        gui.clear()
        gradient_layer(gui,red1, green1, blue1,red2,green2,blue2)
        sun(gui)
        first_mountain(gui, first_color)
        second_third_mountain(gui,second_color,third_color)
        foreground(gui)
        birds(gui,x_bird)
        x_bird +=2
        if x_bird > 1125:
            x_bird = -50
            gui.update_frame(60)

main()








