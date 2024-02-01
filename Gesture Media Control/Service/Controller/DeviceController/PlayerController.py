import os
import time
import pyautogui as pag
from Service.Controller.ConfigController.AppConfig import config


class PlayerController:

    def __init__(self):
        self.active = False
        self.path_parser(config.PLAYER)
    

    def path_parser(self, path):
        self.player_path = fr'{path}'
        self.player_name = path.split('/')[-1]


    def set_player(self, path):
        self.path_parser(path)
        config.set_param('PLAYER', path)


    def set_main_player(self):
        self.path_parser(config.DEFAULT_PLAYER)
        config.set_param('PLAYER', config.DEFAULT_PLAYER)


    def play_pause(self): pag.press('playpause') # two


    def stop(self): pag.press('stop') # fist


    def next_track(self): pag.press('nexttrack') # right


    def previous_track(self): pag.press('prevtrack') # left


    def increase_volume(self):
        for _ in range(5):
            pag.press('volumeup') # up


    def decrease_volume(self):
        for _ in range(5):
            pag.press('volumedown') # down


    def mute_volume(self): pag.press('volumemute') # okay


    def open_close_player(self):
        if self.active:
            os.system(f'taskkill /F /IM {self.player_name}')
        else:
            os.startfile(self.player_path)
            time.sleep(1)
            pag.press('tab')
            pag.press('enter')
        self.active = not self.active




player = PlayerController()

commandCollection = {
    "OPEN/CLOSE": player.open_close_player,
    "PLAY/PAUSE": player.play_pause,
    "MUTE/UNMUTE": player.mute_volume,
    "STOP": player.stop,
    "PREV": player.previous_track,
    "NEXT": player.next_track,
    "VOL_UP": player.increase_volume,
    "VOL_DOWN": player.decrease_volume
}