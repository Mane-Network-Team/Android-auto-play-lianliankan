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


def sim_hash(imageA,imageB):

    hash1 = img_get_dHash(imageA)
    hash2 = img_get_dHash(imageB)

    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n

def img_get_dHash(img):
    img = cv2.resize(img, (40,30))
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(30):
        for j in range(39):
            if gray[i, j] > gray[i, j+1]:
                hash_str = hash_str+'1'
            else:
                hash_str = hash_str+'0'
    return hash_str
