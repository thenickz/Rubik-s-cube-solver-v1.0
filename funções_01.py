import numpy as np


def rotate(direction, main_face_array, main_face_colour):

    np.rot90(main_face_array, direction)

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
