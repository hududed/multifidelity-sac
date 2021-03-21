import numpy as np

def disp_corner(structure):
    a = structure.cart_coords[:,:-1]
    return abs(a[::a.shape[0]-1, ::a.shape[1]-1]).round(2)

def find_corner_idx(structure):
    a = structure.cart_coords[:,:-1]
    corners = (a[::a.shape[0]-1, ::a.shape[1]-1]).round(2) # absolute, sometimes 0 can be -1e-10 or 1e-10
    ix = []
    for i,coords in enumerate((structure.cart_coords[:,:-1].round(2))):
        if (coords[0]==corners[0][0]) and \
        (coords[1]==corners[0][1]): ix.append(i)
        elif (coords[0]==corners[0][0]) and \
        (coords[1]==corners[1][1]): ix.append(i)
        elif (coords[0]==corners[1][0]) and \
        (coords[1]==corners[0][1]): ix.append(i)
        elif (coords[0]==corners[1][0]) and \
        (coords[1]==corners[1][1]): ix.append(i)
    return ix

def find_corner_ix(structure,mid=True):
    a = structure.cart_coords[:,:-1].round(2)
    if mid==True:
        corners = []
        corners.append(second_min_med(a[:,0]))
        corners.append(second_max_med(a[:,0]))
        corners.append(third_min_med(a[:,1]))
        corners.append(third_max_med(a[:,1]))
        corners.append(min(a[:,0]))
        corners.append(max(a[:,0]))
        corners.append(min(a[:,1]))
        corners.append(max(a[:,1]))

        #print(corners)
        ix = []
        for i,coords in enumerate(a):
            if (coords[0]==corners[0]) and \
            (coords[1]==corners[6]): ix.append(i) # min x+1, min y
            elif (coords[0]==corners[0]) and \
            (coords[1]==corners[7]): ix.append(i) # min x+1,max y
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[6]): ix.append(i)
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[7]): ix.append(i)

            if (coords[0]==corners[4]) and \
            (coords[1]==corners[2]): ix.append(i) # min x, min y+1
            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[3]): ix.append(i) # min x+1,max y
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[2]): ix.append(i)
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[3]): ix.append(i)
        return ix
    else:
        corners = []
        corners.append(second_min_large(a[:,0])) # 0
        corners.append(second_max_large(a[:,0]))
        corners.append(third_min_large(a[:,1]))
        corners.append(third_max_large(a[:,1]))
        corners.append(min(a[:,0]))        # 4
        corners.append(max(a[:,0]))
        corners.append(min(a[:,1]))        # 6
        corners.append(max(a[:,1]))
        corners.append(second_min_large(a[:,1])) # 8
        corners.append(second_max_large(a[:,1]))
        corners.append(third_min_large(a[:,0]))  # 10
        corners.append(third_max_large(a[:,0]))
        corners.append(fifth_min_large(a[:,1]))  # 12
        corners.append(fifth_max_large(a[:,1]))
        #print(corners)
        ix = []
        for i,coords in enumerate(a):
            if (coords[0]==corners[4]) and \
            (coords[1]==corners[6]): ix.append(i) 
            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[7]): ix.append(i) 
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[6]): ix.append(i)
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[7]): ix.append(i)

            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[8]): ix.append(i) 
            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[9]): ix.append(i) 
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[8]): ix.append(i)
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[9]): ix.append(i)
            
            elif (coords[0]==corners[10]) and \
            (coords[1]==corners[6]): ix.append(i) 
            elif (coords[0]==corners[10]) and \
            (coords[1]==corners[7]): ix.append(i) 
            elif (coords[0]==corners[11]) and \
            (coords[1]==corners[6]): ix.append(i)
            elif (coords[0]==corners[11]) and \
            (coords[1]==corners[7]): ix.append(i)
                
            elif (coords[0]==corners[0]) and \
            (coords[1]==corners[2]): ix.append(i) 
            elif (coords[0]==corners[0]) and \
            (coords[1]==corners[3]): ix.append(i) 
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[2]): ix.append(i)
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[3]): ix.append(i)
                
            elif (coords[0]==corners[0]) and \
            (coords[1]==corners[2]): ix.append(i) 
            elif (coords[0]==corners[0]) and \
            (coords[1]==corners[3]): ix.append(i) 
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[2]): ix.append(i)
            elif (coords[0]==corners[1]) and \
            (coords[1]==corners[3]): ix.append(i)
                
            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[12]): ix.append(i)
            elif (coords[0]==corners[4]) and \
            (coords[1]==corners[13]): ix.append(i) 
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[12]): ix.append(i)
            elif (coords[0]==corners[5]) and \
            (coords[1]==corners[13]): ix.append(i)

        return ix

def middle_element(lst,around=False,shift=0):
    """Finds the middle elements of a list lst.
       if around=True, returns +1 and -1 indices from middle
       if shift != 0, shift the middle element(s) by shift
    """
    half_len = int((len(lst) / 2))
    
    if around:
        if len(lst) % 2 == 0:
            return (lst[half_len-2],lst[half_len+1])
        else:
            return (lst[half_len-1],lst[half_len+1])
    
    elif shift != 0:
        if len(lst) % 2 == 0:
            return (lst[half_len-1+shift],lst[half_len+shift])
        else:
            return lst[half_len+shift]
    
    else:
        if len(lst) % 2 == 0:
            return (lst[half_len-1],lst[half_len])
        else:
            return lst[half_len]
            


def mid_idx(structure):
    x = middle_element(np.unique(abs(structure.cart_coords[:,0]).round(2)))
    y = middle_element(np.unique(abs(structure.cart_coords[:,1]).round(2)))
    
    ix = []
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if len(y)==2:
            if (coords[0]==x) and (coords[1]==y[0]): ix.append(i)
            elif (coords[0]==x) and (coords[1]==y[1]): ix.append(i)
        else:
            if (coords[0]==x) and (coords[1]==y[0]): ix.append(i)
    return ix
    
def mid_idx_co(structure):
    """(array([ 9.84, 11.07, 12.3 , 13.53]), (11.36, 12.07))
    """
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))[6:10]
    y = middle_element(np.unique(abs(structure.cart_coords[:,1]).round(2)),shift=1)
    
    ix = []
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if (coords[0]==x[0]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[2]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[1]) and (coords[1]==y[1]): ix.append(i)
        elif (coords[0]==x[3]) and (coords[1]==y[1]): ix.append(i)
    return ix

def around_idx(structure):
    x = middle_element(np.unique(abs(structure.cart_coords[:,0]).round(2)),around=True)
    y = middle_element(np.unique(abs(structure.cart_coords[:,1]).round(2)),around=True)
    
    ix = []
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if (coords[0]==x[0]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[0]) and (coords[1]==y[1]): ix.append(i)
        elif (coords[0]==x[1]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[1]) and (coords[1]==y[1]): ix.append(i)
    return ix

def around_idx_co(structure):
    """ (8.61,12.07) (11.07,13.49), (13.53,13.49)
        (9.84, 9.94) (12.3,9.94), (14.76,11.36)
    """
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))[5:11]
    y = np.unique(abs(structure.cart_coords[:,1]).round(2))[8:12]
    
    ix = []
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if (coords[0]==x[0]) and (coords[1]==y[2]): ix.append(i)
        elif (coords[0]==x[2]) and (coords[1]==y[3]): ix.append(i)
        elif (coords[0]==x[4]) and (coords[1]==y[3]): ix.append(i)
        elif (coords[0]==x[1]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[3]) and (coords[1]==y[0]): ix.append(i)
        elif (coords[0]==x[5]) and (coords[1]==y[1]): ix.append(i)
    return ix


def h_idx(structure):
    ix=[]
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))
    y = np.unique(abs(structure.cart_coords[:,1]).round(2))
    
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if coords[0] == min(x) : ix.append(i)
        elif coords[0] == max(x) : ix.append(i)
        elif coords[1] == min(y) : ix.append(i)
        elif coords[1] == max(y) : ix.append(i)
        elif (coords[0] == x[1]) and (coords[1] == y[-2]) : ix.append(i)
        elif (coords[0] == x[1]) and (coords[1] == y[1]) : ix.append(i)
        elif (coords[0] == x[-2]) and (coords[1] == y[-2]) : ix.append(i)
        elif (coords[0] == x[-2]) and (coords[1] == y[1]) : ix.append(i)
    return ix

def h_idx2(structure):
    ix=[]
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))
    y = np.unique(abs(structure.cart_coords[:,1]).round(2))
    
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if (coords[0] == x[1]) and (coords[1] == y[3]) : ix.append(i)
        elif (coords[0] == x[1]) and (coords[1] == y[-4]) : ix.append(i)
       
        elif (coords[0] == x[2]) and (coords[1] == y[1]) : ix.append(i)
        elif (coords[0] == x[2]) and (coords[1] == y[-2]) : ix.append(i)     
        
        elif (coords[0] == x[-3]) and (coords[1] == y[-2]) : ix.append(i)   
        elif (coords[0] == x[-3]) and (coords[1] == y[1]) : ix.append(i)
        
        elif (coords[0] == x[-2]) and (coords[1] == y[-4]) : ix.append(i)
        elif (coords[0] == x[-2]) and (coords[1] == y[3]) : ix.append(i) 
            
    return ix

def xcorner_idx(structure):
    ix=[]
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))
    y = np.unique(abs(structure.cart_coords[:,1]).round(2))
    
    for i,coords in enumerate(abs(structure.cart_coords[:,:-1].round(2))):
        if (coords[0] == x[0]) and (coords[1] == y[-2]) : ix.append(i)
        elif (coords[0] == x[0]) and (coords[1] == y[1]) : ix.append(i)
        elif (coords[0] == x[-1]) and (coords[1] == y[-2]) : ix.append(i)
        elif (coords[0] == x[-1]) and (coords[1] == y[1]) : ix.append(i)
    return ix

def find_x_center(structure):
    x = structure.cart_coords[:,0]
    return (np.mean([min(x),max(x)]))

def find_y_center(structure):
    y = structure.cart_coords[:,1]
    return (np.mean([min(y),max(y)]))
    
def find_x_center_co(structure):
    x = np.unique(abs(structure.cart_coords[:,0]).round(2))[6:10]
    return np.mean([x[0],x[1]]),np.mean([x[2],x[3]])

def find_y_center_co(structure):
    y = middle_element(np.unique(abs(structure.cart_coords[:,1]).round(2)),shift=1)
    return np.mean([y[0],y[1]])

from heapq import nsmallest, nlargest

### medium

def second_min_med(num):
    return np.unique(nsmallest(10, num))[-1]
def second_max_med(num):
    return np.unique(nlargest(10, num))[0]
def third_min_med(num):
    return np.unique(nsmallest(15, num))[-1]
def third_max_med(num):
    return np.unique(nlargest(15, num))[0]

### large

def second_min_large(num):
    return np.unique(nsmallest(20,num))[1] 
def second_max_large(num):
    return np.unique(nlargest(20,num))[-2]

def third_min_large(num):
    return np.unique(nsmallest(20,num))[2]
def third_max_large(num):
    return np.unique(nlargest(20,num))[-3]

def fifth_min_large(num):
    return np.unique(nsmallest(35,num))[4]
def fifth_max_large(num):
    return np.unique(nlargest(35,num))[-5]
