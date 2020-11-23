Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /Users/jiggs/Downloads/graphics.py =================
>>> from graphics import graphics
>>> import random
>>> def gradient_color_randomizer():
	red = random.randint(0,255)
	green = random.randint(0,255)
	blue = random.randint(0,255)
	return red,green,blue

>>> def color_gradient(color_value1,color_value2):
	color_difference = color_value2-color_value1
	if color_difference < 0:
		color_change = -1
	elif color_difference > 0:
		color_change = 1
	else:
		color_change = 0

	if color_difference != 0:
	modulus = int((1/abs(color_difference)/700))+1

	else:
                modulus = 1
        return color_change, modulus

def gradient_layer(gui, red1, green1, blue1, red2, green2, blue2):
        red_change, red_modulus = color_calc(red1,red2)
        green_change,green_modulus = color_calc(green1,green2)
        blue_change,blue_modulus = color_calc(blue1,blue2)
        y_gradient = 1

def random_color(gui):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return gui.get_color_string(red, green, blue) 

def sun(gui):
        x = (gui.mouse_x//50)+343
        y = (gui.mouse_y//50)+343
        gui.ellipse(x+150,y-250,100,100,'yellow')

def middle_mountain(gui,middle_color):
        x = (gui.mouse_x//30)+338
        y = (gui.mouse_y//30)+338
        gui.triangle(x-250,y+350,x,y-150,x+250,y+350,middle_color)

def side_mountains(gui,left_side_color,right_side_color):
        x = (gui.mouse_x//14)+325
        y = (gui.mouse_y//14)+325
        gui.triangle(x-600,y+412,x-200,y-100,x+200,y+412,left_side_color)
        gui.triangle(x-200,y+412,x+200,y-100,x+600,y+412,right_side_color)

def foreground(gui):
        x = (gui.mouse_x//5)+280
        y = (gui.mouse_y//5)+280
        gui.rectangle(x-500,y+250,1000,500,'spring green3')
        x_grass = -2
        while x_grase < 710:
                gui.line(x_grass,y+220,x_grass,y+250, 'spring green3',3)
                x_grass += 7
        gui.rectangle(x+130,y+200,30,100,'saddle brown')
        gui.ellipse(x+145,y+175,100,150,'forest green')
def bird(gui,x_bird)
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
        middle_color = random_color(gui)
        left_side_color = random_color(gui)
        right_side_color = random_color(gui)
        x_bird = 450
        while True:
                gui.clear()
                gradient_layer(gui,red1,green1,blue1,red2,green2,blue2)
                sun(gui)
                middle_mountain(gui,left_side_color,right_side_color)
                foreground(gui)
                bird(gui,x_bird)
                x_bird += 2
                if x_bird > 1125:
                        x_bird = -50
                gui.update_frame(60)

main()


                
	
