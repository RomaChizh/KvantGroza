from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import webbrowser
from win10toast import ToastNotifier
from kivy.uix.popup import Popup

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
a = '0'
Builder.load_string("""
<Glav>:
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
                Rectangle:
                    source: 'Frame 12.png'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .6]
            Button:
                size_hint: [.1, .07]
                canvas:
                    Rectangle:
                        source: 'phon29.jpg'
                        size: self.size
                        pos: self.pos
                on_press: 
                    root.manager.current = 'sec'

        AnchorLayout:
            canvas:
                Rectangle:
                    source: 'Rectahgle 74.png'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .4]
            BoxLayout:
                size_hint: [1, .4]
                padding: [20, 0]
                orientation: 'vertical'
                Label:
                    size_hint: [.3, .14]
                    canvas:
                        Rectangle:
                            source: 'Rekomendatsii.jpg'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Button:
                            size_hint: [.95, 1]
                            on_press: root.manager.current = 'tur'
                            canvas:
                                Rectangle:
                                    source: 'Frame 7.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Button:
                            on_press: root.manager.current = 'tur'
                            size_hint: [.95, 1]
                            canvas:
                                Rectangle:
                                    source: 'Frame 6.png'
                                    size: self.size
                                    pos: self.pos
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<MenuScreen>:
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            AnchorLayout:
                canvas:
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        source: 'Frame_33.png'
                BoxLayout:
                    orientation: 'vertical'
                    Widget:
                    Label:
                        font_size: 6
                        text: 'Дениска лох'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    orientation: 'vertical'
                    canvas:
                        Rectangle:
                            source: 'white.jpg'
                            size: self.size
                            pos: self.pos
                    size_hint: [1, .9]
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phonpr4.jpg'
                                size: self.size
                                pos: self.pos
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr5.jpg'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr2.jpg'
                                    size: self.size
                                    pos: self.pos
                                        
                    AnchorLayout:
                        Button:
                            canvas:
                                Rectangle:
                                    source: 'phonpr3.jpg'
                                    size: self.size
                                    pos: self.pos
                            size_hint: [.8, .5]
                            on_press: root.sky()
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr5.jpg'
                                    size: self.size
                                    pos: self.pos
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<SettingsScreen>:
    canvas:
        Rectangle:
            source: 'img.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        Button:
            text: '==='
            size_hint: [.1, .05]
            background_color: [0, 0, 0, 1]
            background_normal: ''
            on_press: 
                root.manager.current = 'set2'
    AnchorLayout:
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<set2>:
    canvas:
        Rectangle:
            source: 'img.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .4]
            canvas:
                Rectangle:
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            AnchorLayout:
                size_hint: [.2, .4]
                Button:
                    text: '×'
                    font_size: '18'
                    on_press:
                        root.manager.current = 'settings'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Бронирование'
                    on_press:
                        root.manager.current = 'bron'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Ресторан'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Спа и фитнес'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Туры'
                    on_press:
                        root.manager.current = 'tur'
    AnchorLayout:
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<Tur>:
    AnchorLayout:
        AnchorLayout:
            size_hint: [.8, .7]
            GridLayout:
                rows: 8
                cols: 1
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon21.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur2.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon22.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur3.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon23.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur4.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon24.jpg'
                                    size: self.size
                                    pos: self.pos
    Button:
        size_hint: [.3, .05]
        text: 'Назад'
        on_press:
            root.manager.current = 'settings'
<OurMe>:
    canvas:
        Rectangle:
            source: 'phon.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'bottom'
            size_hint: [1, .1]
            Button:
                size_hint: [.8, .5]
                background_color: [.5, 0, .24, 1]
                text: 'Информация об "Отель Островский"...'
                on_press:
                    root.manager.current = 'ourme2'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button: 
                text: 'Номера'
                background_color: [.5, 0, .24, 1]
                size_hint: [.5, .05]
                on_press:
                    root.manager.current = 'num'
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<OurMe2>:
    canvas:
        Rectangle:
            source: 'phon.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'bottom'
            size_hint: [1, .1]
            Button:
                size_hint: [.8, .7]
                background_color: [.5, 0, .24, 1]
                text: 'Информация об "Отель Островский"...' 
                on_press:
                    root.manager.current = 'our me'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            BoxLayout:
                size_hint: [.9, .8]
                orientation: 'vertical'
                canvas:
                    Rectangle:
                        source: 'phon7.jpg'
                        size: self.size
                        pos: self.pos
                Label:
                    font_size: '11'
                    text: 'Отель Островский – это комплекс услуг нового поколения,'
                Label:
                    font_size: '11'
                    text: 'соединяющий отдых на высшем уровне с возможностью'
                Label:
                    font_size: '11'
                    text: 'развития бизнеса и личностным ростом. Стильные'
                Label:
                    font_size: '11'
                    text: 'современные номера в историческом центре города,'
                Label:
                    font_size: '11'
                    text: 'бесплатный Wi-Fi, ресторан современной русской кухни Гроза,'
                Label:
                    font_size: '11'
                    text: 'суперсовременное конференц-пространство Островский-Холл'
                Label:
                    font_size: '11'
                    text: 'с удобными рабочими местами и высокоскоростным'
                Label:
                    font_size: '11'
                    text: 'интернетом, парковка. Наша цель – сделать пребывание'
                Label:
                    font_size: '11'
                    text: 'гостей в нашем отеле максимально комфортным!'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button: 
                text: 'Номера'
                background_color: [.5, 0, .24, 1]
                size_hint: [.5, .1]
                on_press:
                    root.manager.current = 'num'
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glav'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menu'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settings'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our me'
<Num>:
    canvas: 
        Rectangle:
            source: 'phon2.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            Label:
                size_hint: [.5, .1]
                text: 'Номера:'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            size_hint: [1, .8]
            BoxLayout:
                orientation: 'vertical'
                AnchorLayout:
                    Button:
                        size_hint: [.8, .2]
                        text: 'Подробнее о наших номерах'
                        background_color: [.5, 0, .24, 1]
                        on_press: root.web()  
    Button:
        size_hint: [.3, .05]
        background_color: [.5, 0, .24, 1]
        text: 'Назад'
        on_press:
            root.manager.current = 'our me'
<Bron>:
    Button:
        size_hint: [.3, .05]
        text: 'Назад'
        on_press:
            root.manager.current = 'settings'
    AnchorLayout:
        anchor_x: 'center'
        anchot_y: 'center'
        AnchorLayout:
            size_hint: [.9, .5]
            anchor_x: 'left'
            anchor_y: 'center'
            GridLayout:
                cols: 2
                rows: 6
                Label:
                    text: 'Прибытие'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                Label:
                    text: 'Ночи'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                Label:
                    text: 'Отъезд'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                Label:
                    text: 'Взрослые'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle' 
                TextInput:
                Label:
                    text: 'Дети'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                Button:
                    text: 'Поиск доступных комнат'
                    font_size: 10
                    on_press:
                        root.manager.current = 'pass'
<Pass>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon11.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass5'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon12.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass4'
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon13.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass3'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon14.jpg'
                                size: self.size
                                pos: self.pos
                        on_press: 
                            root.manager.current = 'pass2'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon50.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass'
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon10.jpg'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon20.jpg'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon16.jpg'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon18.jpg'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Назад'
            on_press:
                root.manager.current = 'bron'
        Widget:

        Widget:
<Pass2>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon11.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass5'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon12.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass4'
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon13.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass3'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon49.jpg'
                                size: self.size
                                pos: self.pos
                        on_press: 
                            root.manager.current = 'pass2'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon15.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass'
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon31.png'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon34.png'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon33.png'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon32.png'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Назад'
            on_press:
                root.manager.current = 'bron'
        Widget:

        Widget:
<Pass3>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon11.jpg'
                                size: self.size
                                pos: self.pos
                        on_press: 
                            root.manager.current = 'pass5'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon12.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass4'
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon47.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass3'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon14.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass2'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon15.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass'
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon35.png'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon36.png'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon37.png'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon38.png'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Назад'
            on_press:
                root.manager.current = 'bron'
        Widget:

        Widget:
<Pass4>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon11.jpg'
                                size: self.size
                                pos: self.pos
                        on_press: 
                            root.manager.current = 'pass5'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon51.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass4'
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon13.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass3'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon14.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass2'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon15.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass'
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon39.png'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon46.png'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon40.png'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon41.png'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Назад'
            on_press:
                root.manager.current = 'bron'
        Widget:

        Widget:
<Pass5>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon48.jpg'
                                size: self.size
                                pos: self.pos
                        on_press: 
                            root.manager.current = 'pass5'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon12.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass4'
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon13.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass3'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon14.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass2'
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon15.jpg'
                                size: self.size
                                pos: self.pos
                        on_press:
                            root.manager.current = 'pass'
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon42.png'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon46.png'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon43.png'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon45.png'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Назад'
            on_press:
                root.manager.current = 'bron'
        Widget:

        Widget:
<Sec>:
    canvas:
        Rectangle:
            source: 'phon30.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        Button:
            size_hint: [.3, .05]
            text: 'RU/en'
            on_press:
                text: 'ru/EN'
                root.manager.current = 'secEN'

    Button:
        size_hint: [.2, .05]
        text: 'Назад'
        on_press:
            root.manager.current = 'glav'
<SecEN>:
    canvas:
        Rectangle:
            source: 'phon30.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        Button:
            size_hint: [.3, .05]
            text: 'ru/EN'
            on_press:
                text: 'RU/en'
                root.manager.current = 'sec'
    Button:
        size_hint: [.2, .05]
        text: 'Back'
        on_press:
            root.manager.current = 'glavEN'
<GlavEN>:
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            canvas:
                Rectangle:
                    source: 'Frame 12.png'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .6]
            Button:
                size_hint: [.1, .07]
                canvas:
                    Rectangle:
                        source: 'phon29.jpg'
                        size: self.size
                        pos: self.pos
                on_press: 
                    root.manager.current = 'secEN'

        AnchorLayout:
            canvas:
                Rectangle:
                    source: 'Rectahgle 74.png'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .4]
            BoxLayout:
                size_hint: [1, .4]
                padding: [20, 0]
                orientation: 'vertical'
                Label:
                    size_hint: [.3, .14]
                    canvas:
                        Rectangle:
                            source: 'Rekomendatsii.jpg'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Button:
                            size_hint: [.95, 1]
                            on_press: root.manager.current = 'turEN'
                            canvas:
                                Rectangle:
                                    source: 'Frame 7.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Button:
                            on_press: root.manager.current = 'turEN'
                            size_hint: [.95, 1]
                            canvas:
                                Rectangle:
                                    source: 'Frame 6.png'
                                    size: self.size
                                    pos: self.pos
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
<BronEN>:
    Button:
        size_hint: [.3, .05]
        text: 'Back'
        on_press:
            root.manager.current = 'settingsEN'
    AnchorLayout:
        anchor_x: 'center'
        anchot_y: 'center'
        AnchorLayout:
            size_hint: [.9, .5]
            anchor_x: 'left'
            anchor_y: 'center'
            GridLayout:
                cols: 2
                rows: 6
                Label:
                    text: 'Arrival'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Nights'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Departure'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Departure'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle' 
                Label:
                    text: 'Children'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Button:
                    text: 'Finding available rooms'
                    font_size: 10
                    on_press:
                        root.manager.current = 'passEN'
<PassEN>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: [1, .25]
            orientation: 'vertical'
            Label: 
                canvas: 
                    Rectangle:
                        source: 'phon8.jpg'
                        size: self.size
                        pos: self.pos
            Label:
                canvas: 
                    Rectangle:
                        source: 'phon9.jpg'
                        size: self.size
                        pos: self.pos
            AnchorLayout:
                canvas: 
                    Rectangle: 
                        source: 'white.jpg'
                        size: self.size
                        pos: self.pos
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    size_hint: [1, .6]
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon11.jpg'
                                size: self.size
                                pos: self.pos
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon12.jpg'
                                size: self.size
                                pos: self.pos
                    Button:
                        size_hint: [1, 1]      
                        canvas: 
                            Rectangle:
                                source: 'phon13.jpg'
                                size: self.size
                                pos: self.pos
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon14.jpg'
                                size: self.size
                                pos: self.pos
                    Button:
                        size_hint: [1, 1]
                        canvas: 
                            Rectangle:
                                source: 'phon15.jpg'
                                size: self.size
                                pos: self.pos
        AnchorLayout:
            canvas: 
                Rectangle: 
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [1, .7]
            BoxLayout: 
                orientation: 'vertical'
                size_hint: [.8, .7]
                AnchorLayout:
                    canvas:
                        Rectangle:
                            source: 'phon10.jpg'
                            size: self.size
                            pos: self.pos
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phon20.jpg'
                                size: self.size
                                pos: self.pos
                    BoxLayout:
                        Label:
                            canvas:
                                Rectangle: 
                                    source: 'phon16.jpg'
                                    size: self.size
                                    pos: self.pos
                        Button:
                            canvas:
                                Rectangle: 
                                    source: 'phon17.jpg'
                                    size: self.size
                                    pos: self.pos
                            on_press:
                                root.push()
                                root.Num()
                AnchorLayout:
                    canvas:
                        Rectangle: 
                            source: 'phon18.jpg'
                            size: self.size
                            pos: self.pos
                
    GridLayout:
        size_hint: [1, .05]
        cols: 3
        rows: 1
        Button:
            text: 'Back'
            on_press:
                root.manager.current = 'bronEN'
        Widget:

        Widget:
<NumEN>:
    canvas: 
        Rectangle:
            source: 'phon2.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            Label:
                size_hint: [.5, .1]
                text: 'Rooms:'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            size_hint: [1, .8]
            BoxLayout:
                orientation: 'vertical'
                AnchorLayout:
                    Button:
                        size_hint: [.8, .2]
                        text: 'More about our rooms'
                        background_color: [.5, 0, .24, 1]
                        on_press: root.web()  
    Button:
        size_hint: [.3, .05]
        text: 'Back'
        on_press:
            root.manager.current = 'our meEN'
<OurMe2EN>:
    canvas:
        Rectangle:
            source: 'phon.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'bottom'
            size_hint: [1, .1]
            Button:
                size_hint: [.8, .7]
                text: 'Information about Hotel Ostrovsky...' 
                on_press:
                    root.manager.current = 'our meEN'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            BoxLayout:
                size_hint: [.9, .8]
                orientation: 'vertical'
                canvas:
                    Rectangle:
                        source: 'phon7.jpg'
                        size: self.size
                        pos: self.pos
                Label:
                    font_size: '11'
                    text: 'Hotel Ostrovsky is a complex of services of a new generation,'
                Label:
                    font_size: '11'
                    text: 'connecting high-level relaxation with the opportunity'
                Label:
                    font_size: '11'
                    text: 'business development and personal growth. Stylish'
                Label:
                    font_size: '11'
                    text: 'modern rooms in the historical center of the city,'
                Label:
                    font_size: '11'
                    text: 'free Wi-Fi, restaurant of modern Russian cuisine Groza,'
                Label:
                    font_size: '11'
                    text: 'ultra-modern conference space Ostrovsky Hall'
                Label:
                    font_size: '11'
                    text: 'with comfortable workplaces and high-speed'
                Label:
                    font_size: '11'
                    text: 'internet, parking. Our goal is to make your stay'
                Label:
                    font_size: '11'
                    text: 'guests in our hotel as comfortable as possible!'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button: 
                text: 'Rooms'
                size_hint: [.5, .1]
                on_press:
                    root.manager.current = 'numEN'
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
<OurMeEN>:
    canvas:
        Rectangle:
            source: 'phon.jpg'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'bottom'
            size_hint: [1, .1]
            Button:
                size_hint: [.8, .5]
                text: 'Information about Hotel Ostrovsky...'
                on_press:
                    root.manager.current = 'ourme2EN'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button: 
                text: 'Rooms'
                size_hint: [.5, .05]
                on_press:
                    root.manager.current = 'numEN'
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
<TurEN>:
    AnchorLayout:
        AnchorLayout:
            size_hint: [.8, .7]
            GridLayout:
                rows: 8
                cols: 1
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon21.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur2.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon22.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur3.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon23.jpg'
                                    size: self.size
                                    pos: self.pos
                BoxLayout:
                    AnchorLayout:
                        Widget:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'tur4.png'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Label:
                            size_hint: [.9, .9]
                            canvas:
                                Rectangle:
                                    source: 'phon24.jpg'
                                    size: self.size
                                    pos: self.pos
    Button:
        size_hint: [.3, .05]
        text: 'Back'
        on_press:
            root.manager.current = 'settingsEN'
<set2EN>:
    canvas:
        Rectangle:
            source: 'img.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: [.5, .4]
            canvas:
                Rectangle:
                    source: 'white.jpg'
                    size: self.size
                    pos: self.pos
            AnchorLayout:
                size_hint: [.2, .4]
                Button:
                    text: '×'
                    font_size: '18'
                    on_press:
                        root.manager.current = 'settingsEN'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Booking'
                    on_press:
                        root.manager.current = 'bronEN'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Restaurant'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Spa & Fitness'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                padding: [20, 20]
                Button:
                    size_hint: [.8, .8]
                    font_size: '12'
                    text: 'Tours'
                    on_press:
                        root.manager.current = 'turEN'
    AnchorLayout:
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
<SettingsScreenEN>:
    canvas:
        Rectangle:
            source: 'img.jpg'
            size: self.size
            pos: self.pos
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        Button:
            text: '==='
            size_hint: [.1, .05]
            background_color: [0, 0, 0, 1]
            background_normal: ''
            on_press: 
                root.manager.current = 'set2EN'
    AnchorLayout:
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
<MenuScreenEN>:
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            AnchorLayout:
                canvas:
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        source: 'Frame_33.png'
                BoxLayout:
                    orientation: 'vertical'
                    Widget:
                    Label:
                        font_size: 6
                        text: 'Deniz LOH'
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                BoxLayout:
                    orientation: 'vertical'
                    canvas:
                        Rectangle:
                            source: 'white.jpg'
                            size: self.size
                            pos: self.pos
                    size_hint: [1, .9]
                    Label:
                        canvas:
                            Rectangle:
                                source: 'phonpr4.jpg'
                                size: self.size
                                pos: self.pos
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr5.jpg'
                                    size: self.size
                                    pos: self.pos
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr2.jpg'
                                    size: self.size
                                    pos: self.pos
                                        
                    AnchorLayout:
                        Button:
                            canvas:
                                Rectangle:
                                    source: 'phonpr3.jpg'
                                    size: self.size
                                    pos: self.pos
                            size_hint: [.8, .5]
                            on_press: root.sky()
                    AnchorLayout:
                        Button:
                            size_hint: [.8, .5]
                            canvas:
                                Rectangle:
                                    source: 'phonpr5.jpg'
                                    size: self.size
                                    pos: self.pos
    BoxLayout:
        Button:
            canvas:
                Rectangle:
                    source: 'phon25.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'glavEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon26.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'menuEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon27.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press: 
                root.manager.current = 'settingsEN'
        Button:
            canvas:
                Rectangle:
                    source: 'phon28.jpg'
                    size: self.size
                    pos: self.pos
            size_hint: [.7, .05]
            on_press:
                root.manager.current = 'our meEN'
""")
class Glav(Screen):
    pass

class GlavEN(Screen):
    pass

class MenuScreen(Screen):
    def sky(self):
        webbrowser.open_new_tab('https://www.skypixel.com/photo360s/21c5c83d-409b-40a4-a3f7-3e26691d6972')

class MenuScreenEN(Screen):
    def sky(self):
        webbrowser.open_new_tab('https://www.skypixel.com/photo360s/21c5c83d-409b-40a4-a3f7-3e26691d6972')

class SettingsScreen(Screen):
    pass

class SettingsScreenEN(Screen):
    pass

class Set2(Screen):
    pass

class Set2EN(Screen):
    pass

class Num(Screen):
    def web(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms')

class NumEN(Screen):
    def web(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms')

class Tur(Screen):
    pass

class TurEN(Screen):
    pass

class OurMe(Screen):
    pass

class OurMeEN(Screen):
    pass

class OurMe2(Screen):
    pass

class OurMe2EN(Screen):
    pass

class Bron(Screen):
    pass


class Pass(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/appartements')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Заселение", "Апартаменты заселение 15.11.2022 11:00 am", duration=5, threaded=True)

class Pass2(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/luxery')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Заселение", "Люкс заселение 15.11.2022 11:00 am", duration=5, threaded=True)

class Pass3(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/eco')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Заселение", "ЭКО заселение 15.11.2022 11:00 am", duration=5, threaded=True)

class Pass4(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/superior')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Заселение", "Супериор заселение 15.11.2022 11:00 am", duration=5, threaded=True)

class Pass5(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/standart')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Заселение", "Стандарт заселение 15.11.2022 11:00 am", duration=5, threaded=True)

class PassEN(Screen):
    def Num(self):
        webbrowser.open_new_tab('https://ostrovskiyhotel.ru/rooms/appartements')

    def push(self):
        toaster = ToastNotifier()
        toaster.show_toast("Settlement", "Lux check-in 15.11.2022 11:00 am", duration=5, threaded=True)

class Sec(Screen):
    pass

class BronEN(Screen):
    pass


class SecEN(Screen):
    pass

class MyApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Glav(name='glav'))
        sm.add_widget(GlavEN(name='glavEN'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MenuScreenEN(name='menuEN'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SettingsScreenEN(name='settingsEN'))
        sm.add_widget(Set2(name='set2'))
        sm.add_widget(Set2EN(name='set2EN'))
        sm.add_widget(OurMe(name='our me'))
        sm.add_widget(OurMe2(name='ourme2'))
        sm.add_widget(OurMeEN(name='our meEN'))
        sm.add_widget(OurMe2EN(name='ourme2EN'))
        sm.add_widget(Bron(name='bron'))
        sm.add_widget(BronEN(name='bronEN'))
        sm.add_widget(Num(name='num'))
        sm.add_widget(NumEN(name='numEN'))
        sm.add_widget(Pass(name='pass'))
        sm.add_widget(Pass2(name='pass2'))
        sm.add_widget(Pass3(name='pass3'))
        sm.add_widget(Pass4(name='pass4'))
        sm.add_widget(Pass5(name='pass5'))
        sm.add_widget(PassEN(name='passEN'))
        sm.add_widget(Tur(name='tur'))
        sm.add_widget(TurEN(name='turEN'))
        sm.add_widget(Sec(name='sec'))
        sm.add_widget(SecEN(name='secEN'))
        return sm
        return Num
        return sky
        return Num
        return push


if __name__ == '__main__':
    MyApp().run()



