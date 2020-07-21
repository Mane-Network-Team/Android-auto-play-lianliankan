import cv2,numpy
from itertools import chain
import mane_img
from skimage.measure import compare_ssim as ssim
import mane_game

import get_screen
import mane_controller


def run_a_round():
    get_screen.take_screen()
    screens = cv2.imread('screen.png')
    Have_elem_List = []

    # calculate if have elem
    blue_color = numpy.array([200,126,78])
    green_color = numpy.array([6,196,130])

    counter = 1
    for y in range(8):
        line_elem = []
        for x in range(19):
            x1 = 131 + 74*x
            y1 = 105 + int(90.2*y)
            #cv2.circle(screens, (x1, y1), 5, (0, 0, 255), 0)
            if ((screens[y1,x1] == blue_color).all() or (screens[y1,x1] == green_color).all()):
                if (screens[y1,x1] == green_color).all():
                    print("find green")
                line_elem.append(counter)
                counter+=1
            else:
                line_elem.append(0)
        Have_elem_List.append(line_elem)

    #print(Have_elem_List)
    # get elem point

    crop_lists = []
    x_line = 0
    y_line = 0
    for y in Have_elem_List:
        for x in y :
            xm = x_line * 74 +131
            ym = y_line * 91 +146
            if (x!=0):
                newpoint = mane_img.find_blue_border(screens,[xm,ym])
                y2 = newpoint[1][1]
                y1 = newpoint[0][1]
                x2 = newpoint[1][0]
                x1 = newpoint[0][0]
                newp = screens[y1:y2,x1:x2]
                
                cv2.imwrite('tmp/'+str(x)+".png",newp)
                crop_lists.append(newpoint)
            x_line += 1
        y_line += 1
        x_line = 0

    # simulation all function 

    Have_elem_List=list(chain(*Have_elem_List))
    check_elem = ['0']*len(Have_elem_List)
    len_Have_elem_List = len(Have_elem_List)

    #print(Have_elem_List)
    #print(len_Have_elem_List)

    # image simulation process
    for x in range(len_Have_elem_List):
        if (Have_elem_List[x]==0):
            continue
        if (check_elem[x]==1):
            continue
        xpic = cv2.imread('tmp/'+str(Have_elem_List[x])+'.png')

        for y in range(x+1,len_Have_elem_List):
            if (Have_elem_List[y]==0):
                continue
            if (check_elem[y]==1):
                continue
        
            ypic = cv2.imread('tmp/'+str(Have_elem_List[y])+'.png')
            pers = mane_img.sim_percentage(xpic,ypic)

            if (Have_elem_List[y] == 5):
                #print("--------98---------")
                print(" +  Read simulation %s <==> %s : %s"%(Have_elem_List[x],Have_elem_List[y],pers))
            #hashs = mane_img.sim_hash(xpic,ypic)
            #print("hashs:" + str(hashs) )
            if (pers>=0.80):
            #if (hashs<=300):
                #print(" +  Find simulation %s <==> %s : %s"%(x,y,pers))
                Have_elem_List[y] = Have_elem_List[x]
                check_elem[y]=1

    Have_elem_List = numpy.array(Have_elem_List).reshape(8, 19).tolist()
    #print(Have_elem_List)
    do_setp = mane_game.calculation_a_setps(Have_elem_List)
    mane_controller.run_list(do_setp)

def check_game_over():
    print("[*] Checking if game over ...")

    get_screen.take_screen()
    screens = cv2.imread('screen.png')

    blue_color = numpy.array([200,126,78])
    green_color = numpy.array([6,196,130])

    counter = 1
    for y in range(8):
        for x in range(19):
            x1 = 131 + 74*x
            y1 = 105 + int(90.2*y)
            #cv2.circle(screens, (x1, y1), 5, (0, 0, 255), 0)
            if ((screens[y1,x1] == blue_color).all() or (screens[y1,x1] == green_color).all()):
                return False
    print("[!] Game Over!")
    return True


round_counter = 1

while(not check_game_over()):
    print("[!] Round %s ..." %(round_counter))
    run_a_round()
    round_counter += 1