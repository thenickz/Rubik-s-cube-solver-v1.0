import numpy as np
from functions import *

# arrays IDs/cordenates
# in the future the inputs will come from the user, from a original ordinary rubik's cube
white = [1 for _ in range(9)]
blue = [2 for _ in range(9)]
green = [3 for _ in range(9)]
yellow = [4 for _ in range(9)]
orange = [5 for _ in range(9)]
red = [6 for _ in range(9)]

# setting the IDs in each cube's face 
face_blue = np.array([(blue[0], blue[1], blue[2]), 
                      (blue[3], blue[4], blue[5]),
                      (blue[6], blue[7], blue[8])])

face_red = np.array([(red[0], red[1], red[2]), 
                     (red[3], red[4], red[5]), 
                     (red[6], red[7], red[8])])

face_white = np.array([(white[0], white[1], white[2]), 
                       (white[3], white[4], white[5]), 
                       (white[6], white[7], white[8])])

face_green = np.array([(green[0], green[1], green[2]), 
                       (green[3], green[4], green[5]), 
                       (green[6], green[7], green[8])])

face_yellow = np.array([(yellow[0], yellow[1], yellow[2]), 
                        (yellow[3], yellow[4], yellow[5]), 
                        (yellow[6], yellow[7], yellow[8])])

face_orange = np.array([(orange[0], orange[1], orange[2]), 
                        (orange[3], orange[4], orange[5]), 
                        (orange[6], orange[7], orange[8])])

'''def rotate(times, main_face_array, main_face_colour):

    np.rot90(main_face_array, times)

    if main_face_colour == 'blue':

        # pre move backup
        saved_w1 = face_white[0, 0]
        saved_w2 = face_white[0, 1]
        saved_w3 = face_white[0, 2]
        
        saved_r1 = face_red[0, 0]
        saved_r2 = face_red[1, 0]
        saved_r3 = face_red[2, 0]
        
        saved_y1 = face_yellow[2, 0]
        saved_y2 = face_yellow[2, 1]
        saved_y3 = face_yellow[2, 2]
        
        saved_o1 = face_orange[0, 2]
        saved_o2 = face_orange[1, 2]
        saved_o3 = face_orange[2, 2]
    
        # giro dos quinas/cantos
        face_white[0, 0] = saved_o1
        face_white[0, 1] = saved_o2 
        face_white[0, 2] = saved_o3

        face_red[0, 0] = saved_w3
        face_red[1, 0] = saved_w2
        face_red[2, 0] = saved_w1

        face_yellow[2, 0] = saved_r1
        face_yellow[2, 1] = saved_r2
        face_yellow[2, 2] = saved_r3

        face_orange[0, 2] = saved_y1
        face_orange[1, 2] = saved_y2
        face_orange[2, 2] = saved_y3

    elif main_face_colour == 'green':
        # pre move backup
        saved_w1 = face_white[2, 0]
        saved_w2 = face_white[2, 1]
        saved_w3 = face_white[2, 2]
        
        saved_r1 = face_red[0, 2]
        saved_r2 = face_red[1, 2]
        saved_r3 = face_red[2, 2]
        
        saved_y1 = face_yellow[0, 0]
        saved_y2 = face_yellow[0, 1]
        saved_y3 = face_yellow[0, 2]
        
        saved_o1 = face_orange[0, 0]
        saved_o2 = face_orange[1, 0]
        saved_o3 = face_orange[2, 0]
    
        # giro dos quinas/cantos
        face_white[2, 0] = saved_o1
        face_white[2, 1] = saved_o2 
        face_white[2, 2] = saved_o3

        face_red[0, 2] = saved_w3
        face_red[1, 2] = saved_w2
        face_red[2, 2] = saved_w1

        face_yellow[0, 0] = saved_r1
        face_yellow[0, 1] = saved_r2
        face_yellow[0, 2] = saved_r3

        face_orange[0, 2] = saved_y1
        face_orange[1, 2] = saved_y2
        face_orange[2, 2] = saved_y3

    elif main_face_colour == 'red':
         # pre move backup
        saved_w1 = face_white[0, 2]
        saved_w2 = face_white[1, 2]
        saved_w3 = face_white[2, 2]
        
        saved_b1 = face_blue[0, 2]
        saved_b2 = face_blue[1, 2]
        saved_b3 = face_blue[2, 2]
        
        saved_y1 = face_yellow[0, 2]
        saved_y2 = face_yellow[1, 2]
        saved_y3 = face_yellow[2, 2]
        
        saved_g1 = face_green[0, 0]
        saved_g2 = face_green[1, 0]
        saved_g3 = face_green[2, 0]
    
        # giro dos quinas/cantos
        face_white[0, 2] = saved_b1
        face_white[1, 2] = saved_b2 
        face_white[2, 2] = saved_b3

        face_blue[0, 2] = saved_y1
        face_blue[1, 2] = saved_y2
        face_blue[2, 2] = saved_y3

        face_yellow[0, 2] = saved_g3
        face_yellow[1, 2] = saved_g2
        face_yellow[2, 2] = saved_g1

        face_green[0, 0] = saved_w3
        face_green[1, 0] = saved_w2
        face_green[2, 0] = saved_w1

    elif main_face_colour == 'orange':
        # pre move backup
        saved_w1 = face_white[0, 0]
        saved_w2 = face_white[1, 0]
        saved_w3 = face_white[2, 0]
        
        saved_b1 = face_blue[0, 0]
        saved_b2 = face_blue[1, 0]
        saved_b3 = face_blue[2, 0]
        
        saved_y1 = face_yellow[0, 0]
        saved_y2 = face_yellow[1, 0]
        saved_y3 = face_yellow[2, 0]
        
        saved_g1 = face_green[0, 2]
        saved_g2 = face_green[1, 2]
        saved_g3 = face_green[2, 2]
    
        # giro dos quinas/cantos
        face_white[0, 0] = saved_g3
        face_white[1, 0] = saved_g2 
        face_white[2, 0] = saved_g1

        face_blue[0, 0] = saved_w1
        face_blue[1, 0] = saved_w2
        face_blue[2, 0] = saved_w3

        face_yellow[0, 0] = saved_b1
        face_yellow[1, 0] = saved_b2
        face_yellow[2, 0] = saved_b3

        face_green[0, 2] = saved_y3
        face_green[1, 2] = saved_y2
        face_green[2, 2] = saved_y1


    elif main_face_colour == 'yellow':
        # pre move backup
        saved_r1 = face_red[0, 0]
        saved_r2 = face_red[0, 1]
        saved_r3 = face_red[0, 2]
        
        saved_b1 = face_blue[0, 0]
        saved_b2 = face_blue[0, 1]
        saved_b3 = face_blue[0, 2]
        
        saved_o1 = face_orange[0, 0]
        saved_o2 = face_orange[0, 1]
        saved_o3 = face_orange[0, 2]
        
        saved_g1 = face_green[0, 0]
        saved_g2 = face_green[0, 1]
        saved_g3 = face_green[0, 2]
    
        # giro dos quinas/cantos
        face_red[0, 0] = saved_b1
        face_red[0, 1] = saved_b2 
        face_red[0, 2] = saved_b3

        face_blue[0, 0] = saved_o1
        face_blue[0, 1] = saved_o2
        face_blue[0, 2] = saved_o3

        face_orange[0, 0] = saved_g1
        face_orange[0, 1] = saved_g2
        face_orange[0, 2] = saved_g3

        face_green[0, 0] = saved_r1
        face_green[0, 1] = saved_r2
        face_green[0, 2] = saved_r3

    elif main_face_colour == 'white':
        # pre move backup
        saved_r1 = face_red[2, 0]
        saved_r2 = face_red[2, 1]
        saved_r3 = face_red[2, 2]
        
        saved_b1 = face_blue[2, 0]
        saved_b2 = face_blue[2, 1]
        saved_b3 = face_blue[2, 2]
        
        saved_o1 = face_orange[2, 0]
        saved_o2 = face_orange[2, 1]
        saved_o3 = face_orange[2, 2]
        
        saved_g1 = face_green[2, 0]
        saved_g2 = face_green[2, 1]
        saved_g3 = face_green[2, 2]
    
        # giro dos quinas/cantos
        face_red[2, 0] = saved_b1
        face_red[2, 1] = saved_b2 
        face_red[2, 2] = saved_b3

        face_blue[2, 0] = saved_o1
        face_blue[2, 1] = saved_o2
        face_blue[2, 2] = saved_o3

        face_orange[2, 0] = saved_g1
        face_orange[2, 1] = saved_g2
        face_orange[2, 2] = saved_g3

        face_green[2, 0] = saved_r1
        face_green[2, 1] = saved_r2
        face_green[2, 2] = saved_r3
'''