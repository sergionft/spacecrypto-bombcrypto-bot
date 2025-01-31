# -*- coding: utf-8 -*-    
from cv2 import cv2
from os import listdir
from random import randint
from random import random
import numpy as np
import mss
import pyautogui
import time
import sys
import src.env as env

# Tempo entre ações
pyautogui.PAUSE = 0.5
global x_scroll
global y_scroll
global h_scroll
global w_scroll


def addRandomness(n, randomn_factor_size=None):
    if randomn_factor_size is None:
        randomness_percentage = 0.1
        randomn_factor_size = randomness_percentage * n

    random_factor = 2 * random() * randomn_factor_size
    if random_factor > 5:
        random_factor = 5
    without_average_random_factor = n - randomn_factor_size
    randomized_n = int(without_average_random_factor + random_factor)
    return int(randomized_n)

def moveToWithRandomness(x,y,t):
    pyautogui.moveTo(addRandomness(x,10),addRandomness(y,10),t+random()/2)

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def show(rectangles, img = None):
    if img is None:
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            img = np.array(sct.grab(monitor))
    for (x, y, w, h) in rectangles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,255,255), 2)
    cv2.imshow('img',img)
    cv2.waitKey(0)

def clickBtn(img, timeout=3, threshold = 0.8):
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(img, threshold=threshold)
        if(len(matches)==0):
            has_timed_out = time.time()-start > timeout
            continue
        x,y,w,h = matches[0]
        pos_click_x = x+w/2
        pos_click_y = y+h/2
        moveToWithRandomness(pos_click_x,pos_click_y,0.5)
        pyautogui.click()
        return True

    return False

def printSreen():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = np.array(sct.grab(monitor))
        return sct_img[:,:,:3]

def positions(target, threshold=0.8,img = None):
    if img is None:
        img = printSreen()
    result = cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]
    yloc, xloc = np.where(result >= threshold)
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def scroll_ships():
    global x_scroll
    global y_scroll
    global h_scroll
    global w_scroll
    use_click_and_drag_instead_of_scroll = True
    click_and_drag_amount = 120
    scroll_size = 120

    moveToWithRandomness(x_scroll+(w_scroll/2),y_scroll+400+(h_scroll/2),1)
    if not use_click_and_drag_instead_of_scroll:
        pyautogui.scroll(-scroll_size)
    else:
        pyautogui.dragRel(0,-click_and_drag_amount,duration=1, button='left')


def finish_boss():
    finish_boss = positions(env.images_space['finish_boss'], threshold=0.9)
    if len(finish_boss)!=0 :
        clickBtn(env.images_space['finish_boss'])
        time.sleep(0.8)


def go_to_ship():
    if clickBtn(env.images_space['ship']):
        print('Encontrou ship buttom')
        return True
    else:
        return False

def go_to_fight():
    if clickBtn(env.images_space['fight-boss']):
        print('''Vai para fight boss!!
        ''')

def ships_15_15():
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(env.images_space['15-15-boss'], 0.9)

        if(len(matches)==0):
            has_timed_out = time.time()-start > 3
            continue
        print('Encontrou 15-15 tela naves')
        return True
    return False

def ships_0_15():
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(env.images_space['0-15'], 0.9)

        if(len(matches)==0):
            has_timed_out = time.time()-start > 3
            continue
        print('Encontrou 0-15 tela naves')
        return True
    return False

def ships_15_15_boss():
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(env.images_space['15-15-boss'], 0.9)

        if(len(matches)==0):
            has_timed_out = time.time()-start > 3
            continue
        print('Encontrou 15-15 boss')
        return True
    return False

def time_is_zero():
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(env.images_space['time-zero'], 0.8)

        if(len(matches)==0):
            has_timed_out = time.time()-start > 3
            continue
        print('Encontrou time-zero')
        return True
    print('Time diferente de zero')
    return False

def click_fight_ship_new():
    global x_scroll
    global y_scroll
    global h_scroll
    global w_scroll

    offset_x = 180
    offset_y = 90
    y_ship_final = 0

    green_bars = positions(env.images_space['blue-bar-short'], threshold=0.9)
    #print('Blue bars detected', len(green_bars))
    buttons = positions(env.images_space['fight'], threshold=0.9)
    #print('Buttons fight detected', len(buttons))

    scrollCheck = positions(env.images_space['newlatter'], threshold=0.9)

    for key,(x, y, w, h) in enumerate(buttons):
        #print('key: ', key)
        if key == 0:
            x_scroll = x
            y_scroll = y
            h_scroll = h
            w_scroll = w
        elif key == 2:
            y_ship_final = y
            #print("Y ship final: ", y_ship_final)        

    for key,(x, y, w, h) in enumerate(scrollCheck):
        #print('key: ', key)
        if key == 0:
            x_scroll = x
            y_scroll = y
            h_scroll = h
            w_scroll = w
        elif key == 2:
            y_ship_final = y
            #print("Y ship final: ", y_ship_final)    

    yellow_bars = positions(env.images_space['yellow-bar-short'], threshold=0.9)
    #print('Yellow bars detected', len(yellow_bars))

    buttomFigt = positions(env.images_space['fight'], threshold=0.9)
    not_working_green_bars = []
    #for bar in green_bars:
    #    not_working_green_bars.append(bar)
    #for bar in yellow_bars:
    #    not_working_green_bars.append(bar)

        
    for bar in buttomFigt:
        not_working_green_bars.append(bar)

        
    if len(not_working_green_bars) > 0:
        print('buttons with green bar detected', len(not_working_green_bars))
        print('Naves disponiveis', len(not_working_green_bars))

    ship_clicks_cnt = 0
    for (x, y, w, h) in not_working_green_bars:
        #print("Entrou for x y w h. Y:", y)
        #moveToWithRandomness(x+offset_x+(w/2),y+(h/2),1)
        if len(not_working_green_bars) > 0 :
            if ships_15_15():
                return len(not_working_green_bars)

            for i in range(len(not_working_green_bars)):
                #pyautogui.click()
                clickBtn(env.images_space['fight'])
                global ship_clicks
                ship_clicks = ship_clicks + 1
                ship_clicks_cnt = ship_clicks_cnt + 1
                if ship_clicks > 15:
                    return            
            print("Qtd ship enviadas: " + str(ship_clicks_cnt) + ". " + "Qtd ship total enviadas: " + str(ship_clicks))   
            #print("Qtd ship total enviadas", ship_clicks) 
            click_fight_ship_new()
        else:
            return len(not_working_green_bars)
    return len(not_working_green_bars)

       
def ship_to_fight():    
    global ship_clicks
    go_to_continue()
    verify_error()

    finish_boss()

    #if time_is_zero():
    if go_to_ship():
        ship_clicks = 0
        buttonsClicked = 1
        empty_scrolls_attempts = 8
        while(empty_scrolls_attempts >0):
            buttonsClicked = click_fight_ship_new()
            if ships_15_15():
                break 
            if buttonsClicked == 0:
                empty_scrolls_attempts = empty_scrolls_attempts - 1
                       
            if ship_clicks > 15:
                break    
            scroll_ships()
            time.sleep(1)
        go_to_fight()
    else:
        return
    #else:
    #    return

def go_to_ship_tela_boss():
    if clickBtn(env.images_space['ship-boss']):
        print('Volta para naves, tela boss')
        return True
    else:   
        return False

def ship_tela_boss():
    if ships_15_15_boss():
        return
    elif ships_15_15_boss() == False:        
        if go_to_ship_tela_boss():
            time.sleep(5)
            buttonsClicked = 1
            empty_scrolls_attempts = 3

            while(empty_scrolls_attempts >0):
                buttonsClicked = click_fight_ship_new()
                if buttonsClicked == 0:
                    empty_scrolls_attempts = empty_scrolls_attempts - 1
                if ships_15_15():
                    break
                scroll_ships()
                time.sleep(2)
            go_to_fight()


def login():
    
    print("Verificando se o jogo foi desconectado")
    go_to_continue()
    verify_error()

    if clickBtn(env.images_space['connect-wallet'], timeout = 10):
        print('Connect wallet encontrado')
        verify_error()

    if clickBtn(env.images_space['sign'], timeout=8):
        print('Sign button encontrado')
        
        if clickBtn(env.images_space['play'], timeout = 15):
            print('Botao play encontrado')
            print('''Jogo iniciado com sucesso!!

            ''')
            login_attempts = 0
        return



def verify_error():
    if clickBtn(env.images_space['error'], timeout = 8):
        print('Erro Login')
        pyautogui.hotkey('ctrl','f5')
        time.sleep(0.6)
        login()
        return

def go_to_continue():
    if clickBtn(env.images_space['confirm']):
        print('Encontrou confirm')
        time.sleep(0.6)
        return True
    else:
        return False