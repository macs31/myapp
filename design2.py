KV = '''
ScreenManager:
    Login:
    Registration:
    Menu:
    
<Login>
    id: login
    name: 'login'
    MDCard:
        size_hint: None, None
        size: 430, 500
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 10
        padding: 20
        spacing: 30
        orientation: 'vertical'
        MDLabel:
            text: 'Login'
            font_style: 'Button'
            font_size: 45
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 1
        MDTextFieldRound:
            id: user
            hint_text: 'username'
            icon_right: 'account'       
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {'center_x':.5}
            color_active: [1,1,1,1]
        MDTextFieldRound:
            id: password
            hint_text: 'password'
            icon_right: 'eye-off'
            size_hint_x: None
            width: 220
            pos_hint: {'center_x':.5}
            color_active: [1,1,1,1]
            password: True
        MDRoundFlatButton:
            text: 'Войти'
            pos_hint: {'center_x':0.5}
            font_size: 15
            on_press: app.get_data()
            on_press: root.manager.current = 'menu'
        MDFlatButton:
            text: "Зарегистрироваться"
            theme_text_color: "Custom"
            text_color: "lightblue"
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'registration'
        Widget:
            size_hint_y: None
            height: 10

<Registration>:
    name: 'registration'
    id: registration
    MDCard:
        size_hint: None, None
        size: 430, 500
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 10
        padding: 20
        spacing: 30
        orientation: 'vertical'
        MDLabel:
            text: 'Login'
            font_style: 'Button'
            font_size: 45
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 1
        MDTextFieldRound:
            id: user_r
            hint_text: 'username'
            icon_right: 'account'       
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {'center_x':.5}
            color_active: [1,1,1,1]
        MDTextFieldRound:
            id: password_r
            hint_text: 'password'
            icon_right: 'eye-off'
            size_hint_x: None
            width: 220
            pos_hint: {'center_x':.5}
            color_active: [1,1,1,1]
            password: True
        MDRoundFlatButton:
            text: 'Зарегистрироваться'
            pos_hint: {'center_x':0.5}
            font_size: 15
            on_press: app.get_data_registration()
            on_press: root.manager.current = 'menu'
        MDFlatButton:
            text: "Назад"
            theme_text_color: "Custom"
            text_color: "lightblue"
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'login'
        Widget:
            size_hint_y: None
            height: 10
            
<Menu>
    id: menu
    name: 'menu'
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "green"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Обучение'
            icon: 'sprout'
            MDRectangleFlatIconButton:
                icon: "book"
                text: "Изучайте новые слова, вместе с нами"
            MDRectangleFlatIconButton:
                icon: "music-box"
                text: "Тексты ваших любимых английских песен на русском"
            MDRectangleFlatIconButton:
                icon: "android"
                text: "MDRectangleFlatIconButton"

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Статистика'
            icon: 'crown'


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Профиль'
            icon: 'account'
            MDLabel:
                text: 'hello'
'''