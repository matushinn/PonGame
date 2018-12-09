# -*- coding: utf-8 -*

from kivy.app import App
from kivy.factory import Factory
# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# 日本語フォント表示対応
# resource_add_path('{}\\{}'.format(os.environ['SYSTEMROOT'], 'Fonts'))
# LabelBase.register(DEFAULT_FONT, 'MSGOTHIC.ttc')

Builder.load_file('window1.kv')
Builder.load_file('window2.kv')
Builder.load_file('window3.kv')


class MainRoot(BoxLayout):
    window1 = None
    window2 = None
    window3 = None

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.window1 = Factory.Window1()
        self.window2 = Factory.window2()
        self.window3 = Factory.Window3()

        super(MainRoot, self).__init__(**kwargs)

    # 一番目の画面遷移
    def change_disp(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    # 二番目の画面遷移
    def change_disp1(self):
         self.clear_widgets()
         self.add_widget(self.window2)

    # 三番目の画面遷移
    def change_disp2(self):
         self.clear_widgets()
         self.add_widget(self.window3)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'PongPongPong Game'


if __name__ == "__main__":
    MainApp().run()
