from kivy.garden.facelock import FaceLock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
Builder.load_string('''

<LockScreen>:

    index: 0
    cascade: 'haarcascade_frontalface_default.xml'
    on_match: root.change_scr()
    BoxLayout:
        id: bl
        Label:
            text: "You have a nice face !!!"
            font_size: 40

''')


class StartScreen(Screen):
    pass


class LockScreen(FaceLock, Screen):
    def change_scr(self):
        print("You have unlocked the Application")
        print("Secret Code: 15UCS164")
        print("You can not access this code unless you unlock it")
        print("You can do whatever that you want but it would need your face")

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LockScreen(name="lock_screen"))


class CameraApp(App):

    def build(self):
        return sm


CameraApp().run()