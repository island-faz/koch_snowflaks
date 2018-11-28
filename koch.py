import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow 
import math
import random

class Point(object):

    def __init__(self, x, y):
        self.X = x
        self.Y = y

def Deg2rad(angle_deg):
	return (angle_deg * math.pi / 180)

def rotate2D(p1, p2, angle):
    _x2 = p1.X - p2.X
    _y2 = p1.Y - p2.Y

    _x2_ = (int)(_x2 * math.cos(angle) + _y2 * math.sin(angle)) + p2.X
    _y2_ = (int)(_y2 * math.cos(angle) - _x2 * math.sin(angle)) + p2.Y

    return Point(_x2_, _y2_)
#	return {'x':_x2_, 'y':_y2_}

def XPoint(p1, p2, value):
	return (Point(p1.X + (p2.X - p1.X) * value, p1.Y + value * (p2.Y - p1.Y)))

#def  draw_rectangle():

def draw_koch(p1, p2, depth):
    if (depth == 1):
        draw.line((p1.X, p1.Y, p2.X, p2.Y), fill=(255,255,255))

    else:
        p3 = XPoint(p1, p2, 1/3)
        p4 = XPoint(p1, p2, 2/3)
        p5 = rotate2D(p3, p4, Deg2rad(60));    	
        draw_koch(p1, p3, depth - 1)
        draw_koch(p3, p5, depth - 1)
        draw_koch(p5, p4, depth - 1)
        draw_koch(p4, p2, depth - 1)

im = Image.new("RGB", (5000 * 2, 5000 * 2))
draw = ImageDraw.Draw(im)

p1 = Point(3850 * 2, 1850 * 2)
p2 = Point(1200 * 2, 1850 * 2)
p3 = rotate2D(p2, p1, Deg2rad(60));

k = 6
draw_koch(p1, p2, k)
draw_koch(p3, p1, k)
draw_koch(p2, p3, k)

im.show()