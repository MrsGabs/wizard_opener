import pyautogui as pg
import time

pg.press("win")

pg.write("edge")

time.sleep(1)

pg.press("enter")

time.sleep(1)

pg.write("https://pearson.lti.elos.vc/rooms/671020747fc006267bec249795592dcfd7518737/scheduled_meetings/RplctsnYca1m/external")

pg.press("enter")

time.sleep(1.5)

pg.write("Gabriel")

pg.press("enter")

pg.write("Althoff Monteiro")

pg.press("enter")

time.sleep(0.5)

pg.hotkey("ctrl", "t")

time.sleep(0.5)

pg.write("https://me.wizard.com.br/catchup/#/catchup/")

pg.press("enter")

time.sleep(1.5)

pg.click(550, 550) # Click the mouse at the x, y coordinates 550, 550.

time.sleep(0.5)

pg.hotkey("ctrl", "t")

pg.write("translate")

pg.press("enter")

time.sleep(0.5)

pg.hotkey("ctrl", "tab")