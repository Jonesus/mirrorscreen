import pygame
from pygame.locals import *
import math
from time import gmtime, strftime
from weatherclass import weatherobj
from textclass import textobj
from imgclass import imgobj
import time

def main():
    print("Starting...")
    
    
    def fetch_eventlist(oldevents):
        tries = 3
        while tries:
            print("Getting events...")
            try:
                eventlist = weather.get_events()
                print("got events.")
                tries = 0
            except:
                tries -= 1
                print("failed to get events, retrying...")
                
        return eventlist if (len(eventlist) > 0) else oldevents
            
    
    
    
    # Initialize pygame
    
    pygame.display.init()
    dispw = pygame.display.Info().current_w
    disph = pygame.display.Info().current_h
    size = (dispw, disph)
    display = pygame.display.set_mode(size)
    pygame.display.set_caption('Jee')
    clock = pygame.time.Clock()
    FPS = 10
    pygame.mouse.set_visible(False)
    pygame.init()
    
    print("Pygame set up.")
    
    
    
    # Initialize weather class and special dates
    
    weather = weatherobj()
    weather.get_rise_set()
    bigfont = pygame.font.Font("fonts/Roboto-Light.ttf", 58)
    smallfont = pygame.font.Font("fonts/Roboto-Light.ttf", 28)
    minifont = pygame.font.Font("fonts/Roboto-Light.ttf", 16)
    minibold = pygame.font.Font("fonts/Roboto-Medium.ttf", 16)
    dates = {"06.12." : "Hyvää Itsenäisyyspäivää!"}
    
    
    # Print something on screen so user knows the program is working
    
    starttext = textobj(100, 100, minifont, "Starting...", display, dispw, disph, 255)
    for i in range(52):
        starttext.fade_in()
    starttext.draw()
    pygame.display.update()
    
    
    
    # Get text for weather objects
    
    tries = 10
    while tries:
        print("Getting data...")
        try:
            currenttemp = weather.get_current()[1]
            wind = weather.get_current()[2] + " m/s"
            forecast = weather.get_forecast()
            hournow = strftime("%H:")
            minutenow = strftime("%M")
            datenow = strftime("%d.%m.%Y")
            bigpic = weather.get_current()[0]
            tries = 0
            print("got data.")
            
        except:
            time.sleep(2)
            tries -= 1
            print("Failed to get data, retrying...")
        
    
    
    # Get events in Helsinki from minnenyt.fi
    
    tries = 3
    while tries:
        eventlist = fetch_eventlist(None)
        if eventlist == None:
            time.sleep(10)
            tries -= 1
            eventlist = fetch_eventlist(None)
        else:
            tries = 0
    
    eventrunner = 0  # Running variable to determine which event from eventlist is being displayed
    
    # Create text objects for time and weather
    
    print("Initializing objects...")
    
    timehour   = textobj(68         , 0          , bigfont  , hournow    , display, dispw, disph)
    timeminute = textobj(145        , 0          , bigfont  , minutenow  , display, dispw, disph)
    date       = textobj(100        , 110        , smallfont, datenow    , display, dispw, disph, 200)
    bigtemp    = textobj(dispw - 200, 0          , bigfont  , currenttemp, display, dispw, disph)
    windspd    = textobj(dispw - 200, 60         , smallfont, wind       , display, dispw, disph, 200)
    dailytext  = textobj(0          , disph - 200, bigfont  , ""         , display, dispw, disph)
    
    smalltemp_y = 160
    
    smalltemp0 = textobj(dispw, smalltemp_y,       smallfont, forecast[0][1], display, dispw, disph, 225)
    smalltemp1 = textobj(dispw, smalltemp_y + 35,  smallfont, forecast[1][1], display, dispw, disph, 205)
    smalltemp2 = textobj(dispw, smalltemp_y + 70,  smallfont, forecast[2][1], display, dispw, disph, 185)
    smalltemp3 = textobj(dispw, smalltemp_y + 105, smallfont, forecast[3][1], display, dispw, disph, 165)
    smalltemp4 = textobj(dispw, smalltemp_y + 140, smallfont, forecast[4][1], display, dispw, disph, 145)
    
    
    # Create text objects for event info
    
    # Coordinates on screen
    event_x = 70
    event_y = 700
    spacing = 18
    
    eventline0  = textobj(event_x, event_y + spacing * 0 , minibold, eventlist[0][0] , display, dispw, disph, 255)
    eventline1  = textobj(event_x, event_y + spacing * 1 , minibold, eventlist[0][1] , display, dispw, disph, 255)
    eventline2  = textobj(event_x, event_y + spacing * 2 , minifont, eventlist[0][2] , display, dispw, disph, 255)
    eventline3  = textobj(event_x, event_y + spacing * 3 , minifont, eventlist[0][3] , display, dispw, disph, 255)
    eventline4  = textobj(event_x, event_y + spacing * 4 , minifont, eventlist[0][4] , display, dispw, disph, 255)
    eventline5  = textobj(event_x, event_y + spacing * 5 , minifont, eventlist[0][5] , display, dispw, disph, 255)
    eventline6  = textobj(event_x, event_y + spacing * 6 , minifont, eventlist[0][6] , display, dispw, disph, 255)
    eventline7  = textobj(event_x, event_y + spacing * 7 , minifont, eventlist[0][7] , display, dispw, disph, 255)
    eventline8  = textobj(event_x, event_y + spacing * 8 , minifont, eventlist[0][8] , display, dispw, disph, 255)
    eventline9  = textobj(event_x, event_y + spacing * 9 , minifont, eventlist[0][9] , display, dispw, disph, 255)
    eventline10 = textobj(event_x, event_y + spacing * 10, minifont, eventlist[0][10], display, dispw, disph, 255)
    eventline11 = textobj(event_x, event_y + spacing * 11, minifont, eventlist[0][11], display, dispw, disph, 255)
    eventline12 = textobj(event_x, event_y + spacing * 12, minifont, eventlist[0][12], display, dispw, disph, 255)
    eventline13 = textobj(event_x, event_y + spacing * 13, minifont, eventlist[0][13], display, dispw, disph, 255)
    eventline14 = textobj(event_x, event_y + spacing * 14, minifont, eventlist[0][14], display, dispw, disph, 255)
    
    
    eventobjlist = [eventline0, eventline1, eventline2, eventline3, eventline4, eventline5, eventline6, \
                    eventline7, eventline8, eventline9, eventline10, eventline11, eventline12, eventline13, \
                    eventline14]
    
    # Load picture files for image objects
    
    bigpic    = pygame.image.load("icons/" + bigpic)
    smallpic0 = pygame.image.load("icons/" + forecast[0][0])
    smallpic1 = pygame.image.load("icons/" + forecast[1][0])
    smallpic2 = pygame.image.load("icons/" + forecast[2][0])
    smallpic3 = pygame.image.load("icons/" + forecast[3][0])
    smallpic4 = pygame.image.load("icons/" + forecast[4][0])
    
    
    
    # Scale pictures
    
    bigpic    = pygame.transform.smoothscale(bigpic,    (70, 70))
    smallpic0 = pygame.transform.smoothscale(smallpic0, (32, 32))
    smallpic1 = pygame.transform.smoothscale(smallpic1, (32, 32))
    smallpic2 = pygame.transform.smoothscale(smallpic2, (32, 32))
    smallpic3 = pygame.transform.smoothscale(smallpic3, (32, 32))
    smallpic4 = pygame.transform.smoothscale(smallpic4, (32, 32))
    
    
    
    # Create appropriate objects for pictures
    
    smallpic_y = 160
    
    bigimg =    imgobj(dispw - 290, 60              , bigpic   , display, 70)
    smallimg0 = imgobj(dispw - 250, smallpic_y      , smallpic0, display, 32, 225)
    smallimg1 = imgobj(dispw - 250, smallpic_y + 35 , smallpic1, display, 32, 205)
    smallimg2 = imgobj(dispw - 250, smallpic_y + 70 , smallpic2, display, 32, 185)
    smallimg3 = imgobj(dispw - 250, smallpic_y + 105, smallpic3, display, 32, 165)
    smallimg4 = imgobj(dispw - 250, smallpic_y + 140, smallpic4, display, 32, 145)
    
    
    # Create a list for all objects
    
    objlist = [bigtemp, smalltemp0, smalltemp1, smalltemp2, smalltemp3, \
               smalltemp4, date, timehour, timeminute, windspd,\
               bigimg, smallimg0, smallimg1, smallimg2, smallimg3, smallimg4, \
               eventline0, eventline1, eventline2, eventline3, eventline4, eventline5, eventline6, \
               eventline7, eventline8, eventline9, eventline10, eventline11, eventline12, eventline13, \
               eventline14, dailytext]
        
    
    
    
    print("initialized.")
    
    
    # Variables for main loop
    
    lastminute = None

    print("Fading in...")
                
    ms = clock.tick(FPS)
    passed = 0

    time.sleep(2)


            
    # Fade in weathertext and time/date for the first time

                
    while True:

        clock.tick(60)
                    
        display.fill((0,0,0))
        for obj in objlist:
            obj.draw()
                    
        passed = clock.tick(FPS) / 20
        
        
        # Move stuff super smooth
                    
        if smalltemp4.get_x() <= dispw - 200:
            for obj in objlist:
                obj.zero_time()
            break
                    
        if bigtemp.get_y() <= 100:
                        
            bigtemp.move_down(passed)
            bigtemp.fade_in()
            bigimg.fade_in()
            timehour.move_down(passed)
            timehour.fade_in()
            timeminute.move_down(passed)
            timeminute.fade_in()
            dailytext.fade_in()
                    
        if smalltemp0.get_x() >= dispw - 200:
            smalltemp0.move_left(passed)
            smalltemp0.fade_in()
            smallimg0.fade_in()
                    
        if smalltemp1.get_x() >= dispw - 200 and smalltemp0.get_x() <= dispw - 100:
            smalltemp1.move_left(passed)
            smalltemp1.fade_in()
            smallimg1.fade_in()
            windspd.move_down(passed)
            windspd.fade_in()
                        
        if smalltemp2.get_x() >= dispw - 200 and smalltemp1.get_x() <= dispw - 100:
            smalltemp2.move_left(passed)
            smalltemp2.fade_in()
            smallimg2.fade_in()
            date.move_right(passed)
            date.fade_in()
                        
        if smalltemp3.get_x() >= dispw - 200 and smalltemp2.get_x() <= dispw - 100:
            smalltemp3.move_left(passed)
            smalltemp3.fade_in()
            smallimg3.fade_in()
                        
        if smalltemp4.get_x() >= dispw - 200 and smalltemp3.get_x() <= dispw - 100:
            smalltemp4.move_left(passed)
            smalltemp4.fade_in()
            smallimg4.fade_in()
                        
        pygame.display.update()
    print("done.\n")
    
    
    # Draw first event
    
    print("Drawing event...")
    
    for i in range(52):
                    
        display.fill((0,0,0))
        for obj in objlist:
            obj.draw()
        
        passed = clock.tick(FPS) / 20
        
        for obj in eventobjlist:
            obj.fade_in()
        pygame.display.update()
        
    print("done.\n")



    
    
    
    
    print()
    print()
    print("------------------")
    print("Main loop started.")
    print("------------------")
    print()
    print()
    print()
    
    
    # Start main loop
    
    while True:
        ms = clock.tick(FPS) 
        
        
        # Check if info on screen needs to be updated
        
        currentminute = strftime("%M")[-1]
        if currentminute != lastminute:
            
            # Fetch new info
            
            tries = 10
            while tries:
                print("Getting data...")
                try:
                    lastminute = currentminute
                    currenttemp = weather.get_current()[1]
                    wind = weather.get_current()[2] + " m/s"
                    forecast = weather.get_forecast()
                    hournow = strftime("%H:")
                    minutenow = strftime("%M")
                    datenow = strftime("%d.%m.%Y")
                    bigpic = weather.get_current()[0]
                    tries = 0
                    print("fresh data.\n")
                except:
                    time.sleep(2)
                    tries -= 1
                    print("Failed to update info, trying again...")
            
            
                
            # Update the classes    
            
            bigtemp.update_text(currenttemp)
            smalltemp0.update_text(forecast[0][1])
            smalltemp1.update_text(forecast[1][1])
            smalltemp2.update_text(forecast[2][1])
            smalltemp3.update_text(forecast[3][1])
            smalltemp4.update_text(forecast[4][1])
            date.update_text(datenow)
            timehour.update_text(hournow)
            timeminute.update_text(minutenow)
            windspd.update_text(wind)
            bigimg.update_img("icons/" + bigpic)
            smallimg0.update_img("icons/" + forecast[0][0])
            smallimg1.update_img("icons/" + forecast[1][0])
            smallimg2.update_img("icons/" + forecast[2][0])
            smallimg3.update_img("icons/" + forecast[3][0])
            smallimg4.update_img("icons/" + forecast[4][0])
            
            
            
            # Find out if its a day for a special message, fade in and out if necessary
            
            day = "%d.%m."
            if strftime(day) in dates.keys():
                if dates[strftime(day)] != dailytext.inputtext:
                    print("Fading out old text...")
                    for i in range(52):
                        clock.tick(FPS)
                        dailytext.fade_out()
                        dailytext.draw()
                        pygame.display.update()
                    print("Fading in daily text...")
                    dailytext.hue = 0
                    dailytext.update_text(dates[strftime(day)])
                    center = (dispw // 2) - (dailytext.text.get_rect().width // 2)
                    dailytext.x = center
                    dailytext.startx = center
                    for i in range(52):
                        clock.tick(FPS)
                        dailytext.fade_in()
                        dailytext.draw()
                        pygame.display.update()
                    print("done.\n")
                        
            else:
                if dailytext.inputtext != "":
                    print("Fading out daily text...")
                    for i in range(52):
                        clock.tick(FPS)
                        dailytext.fade_out()
                        dailytext.draw()
                        pygame.display.update()
                    dailytext.update_text("")
                    print("done.\n")
            
            display.fill((0,0,0))
            for obj in objlist:
                obj.draw()
            pygame.display.update()
            
            
            
            # Handle event text
            
            if eventrunner == len(eventlist) - 2:
                eventlist = fetch_eventlist(eventlist)
                eventrunner = 0
            
            print("Changing event text...")
            
            # Fade out old event
            for i in range(52):
                display.fill((0,0,0))
                for obj in objlist:
                    obj.draw()
                
                passed = clock.tick(FPS) / 20
                
                for obj in eventobjlist:
                    obj.fade_out()
                pygame.display.update()
        
            eventrunner += 1
            
            # Update each line with new event's text
            i = 0
            for obj in eventobjlist:
                obj.update_text( eventlist[eventrunner][i] )
                i += 1
            
            # Fade in new event
            for i in range(52):
                display.fill((0,0,0))
                for obj in objlist:
                    obj.draw()
                
                passed = clock.tick(FPS) / 20
                
                for obj in eventobjlist:
                    obj.fade_in()
                pygame.display.update()
        
            
            print("done.\n")
                
        # Make the ":" in the clock tick every second
        
        currentsecond = strftime("%S")[-1]
        if int(currentsecond) % 2 == 0:
            hournow = strftime("%H:")
            timehour.update_text(hournow)
            display.fill((0,0,0))
            for obj in objlist:
                obj.draw()
                
        else:
            hournow = strftime("%H")
            timehour.update_text(hournow)
            display.fill((0,0,0))
            for obj in objlist:
                obj.draw()
        
        
        
        # Check for quitting keystrokes, pressing "k" toggles the text on, "l" off
        
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                break
            
            # Fade text in
            elif event.key == K_k:
                
                print("Fading in...")
                
                ms = clock.tick(FPS)
                passed = 0
                
                while True:
                    
                    display.fill((0,0,0))
                    for obj in objlist:
                        obj.draw()
                    
                    passed = clock.tick(FPS) / 20
                    
                    # Move shit super smooth
                    
                    if smalltemp4.get_x() <= dispw - 200:
                        for obj in objlist:
                            obj.zero_time()
                        break
                    
                    if bigtemp.get_y() <= 100:
                        
                        bigtemp.move_down(passed)
                        bigtemp.fade_in()
                        bigimg.fade_in()
                        timehour.move_down(passed)
                        timehour.fade_in()
                        timeminute.move_down(passed)
                        timeminute.fade_in()
                        dailytext.fade_in()
                    
                    if smalltemp0.get_x() >= dispw - 200:
                        smalltemp0.move_left(passed)
                        smalltemp0.fade_in()
                        smallimg0.fade_in()
                    
                    if smalltemp1.get_x() >= dispw - 200 and smalltemp0.get_x() <= dispw - 100:
                        smalltemp1.move_left(passed)
                        smalltemp1.fade_in()
                        smallimg1.fade_in()
                        windspd.move_down(passed)
                        windspd.fade_in()
                        
                    if smalltemp2.get_x() >= dispw - 200 and smalltemp1.get_x() <= dispw - 100:
                        smalltemp2.move_left(passed)
                        smalltemp2.fade_in()
                        smallimg2.fade_in()
                        date.move_right(passed)
                        date.fade_in()
                        
                    if smalltemp3.get_x() >= dispw - 200 and smalltemp2.get_x() <= dispw - 100:
                        smalltemp3.move_left(passed)
                        smalltemp3.fade_in()
                        smallimg3.fade_in()
                        
                    if smalltemp4.get_x() >= dispw - 200 and smalltemp3.get_x() <= dispw - 100:
                        smalltemp4.move_left(passed)
                        smalltemp4.fade_in()
                        smallimg4.fade_in()
                        
                    pygame.display.update()
                print("done.\n")
            
            # Fade text out
            
            elif event.key == K_l:
                
                print("Fading out...")
                
                for i in range(52):
                    
                    display.fill((0,0,0))
                    for obj in objlist:
                        obj.draw()
                    
                    passed = clock.tick(FPS) / 20
                    
                    for obj in objlist[:-1]:
                        obj.fade_out()
                    pygame.display.update()
                    
                for obj in objlist:
                    obj.reset_pos()
                print("done.\n")
                    
        pygame.display.update()
    
        
    print()
    print()
    print("-------------------")
    print("Main loop finished.")
    print("-------------------")
    print()
    print()



if __name__ == "__main__":
    main()



