import numpy,cv2
from skimage.measure import compare_ssim as ssim

def find_blue_border(screens,point):
    blue_color = numpy.array([200,126,78])
    green_color = numpy.array([6,196,130])

    LT_X = point[0]
    LT_Y = point[1]

    RB_X = point[0]
    RB_Y = point[1]

    while (True):
        if ((screens[LT_Y, LT_X - 1] == blue_color).all() or (screens[LT_Y, LT_X - 1] == green_color).all()):
            break
        else:
            LT_X = LT_X - 1
                
    while (True):
        if ((screens[LT_Y - 1, LT_X ] == blue_color).all()) or ((screens[LT_Y - 1, LT_X ] == green_color).all()):
            break
        else:
            LT_Y = LT_Y - 1
                
    while (True):
        if ((screens[RB_Y, RB_X + 1] == blue_color).all()) or ((screens[RB_Y, RB_X + 1] == green_color).all()):
            break
        else:
            RB_X = RB_X + 1

    while (True):
        if ((screens[RB_Y + 1, RB_X ] == blue_color).all()) or ((screens[RB_Y + 1, RB_X ] == green_color).all()):
            if (((screens[RB_Y + 1, RB_X ] == green_color).all())):
                RB_Y+=2
            break
        else:
            RB_Y = RB_Y + 1

    return([[LT_X,LT_Y],[RB_X,RB_Y]])


def sim_percentage(imageA,imageB):
    A = cv2.resize(imageA,(77,60))
    B = cv2.resize(imageB,(77,60))
    A1 = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
    B1 = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)
    RTN = ssim(A1,B1)
    return (RTN)
