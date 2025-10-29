from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
import random

class LeilaAI:
    def __init__(self):
        self.name = "Лейла"
        self.jokes = [
            "Почему программисты путают Хэллоуин и Рождество? Oct 31 == Dec 25!",
            "Что говорит математик без туалетной бумаги? 'Сейчас посчитаю...'",
            "Почему курица перешла дорогу? Чтобы доказать, что она не индюк!",
            "Как русские часы? Секунда-секунда-секунда...",
            "Кот программист делает только Ctrl+C, Ctrl+V!",
            "Почему 6 боится 7? Потому что 7 8 9!",
            "Стакан воды сидел потому что был стаканом!",
            "Программист любит Java!",
            "Кот программист ловит mouse!",
            "Зачем AI шутит? Чтобы byte-сь! 🤖"
        ]
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if any(word in user_input for word in ['привет', 'хай']):
            return f"Привет! Я {self.name} - твой шутник! 😄"
        elif any(word in user_input for word in ['шутка', 'пошути']):
            return random.choice(self.jokes)
        elif any(word in user_input for word in ['как дела']):
            return "Отлично! Готова шутить! 🎭"
        elif any(word in user_input for word in ['имя']):
            return f"Я {self.name}! AI с юмором! 🤡"
        elif any(word in user_input for word in ['пока']):
            return "Пока! Возвращайся за шутками! 👋"
        else:
            return f"{random.choice(['Хм...', 'Окей,', 'Интересно!'])} {random.choice(self.jokes)}"

class LeilaApp(App):
    def build(self):
        self.leila = LeilaAI()
        self.title = "Лейла AI Шутник"
        
        # Главный layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок
        title = Label(
            text="🎭 Лейла - AI Шутник 🎭",
            size_hint_y=0.1,
            color=(0.9, 0.1, 0.5, 1),
            font_size='20sp',
            bold=True
        )
        layout.add_widget(title)
        
        # Чат
        self.chat_area = ScrollView(size_hint_y=0.7)
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.chat_area.add_widget(self.chat_layout)
        layout.add_widget(self.chat_area)
        
        # Ввод
        input_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        self.input = TextInput(
            hint_text="Напишите Лейле...",
            size_hint_x=0.7,
            multiline=False
        )
        self.input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text="Отправить",
            size_hint_x=0.3,
            background_color=(0.9, 0.1, 0.5, 1)
        )
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.input)
        input_layout.add_widget(send_btn)
        layout.add_widget(input_layout)
        
        # Быстрые кнопки
        btn_layout = BoxLayout(size_hint_y=0.05, spacing=5)
        joke_btn = Button(text="🎭 Шутка", background_color=(0, 0.5, 1, 1))
        clear_btn = Button(text="🗑️ Очистить", background_color=(1, 0.3, 0.3, 1))
        
        joke_btn.bind(on_press=self.quick_joke)
        clear_btn.bind(on_press=self.clear_chat)
        
        btn_layout.add_widget(joke_btn)
        btn_layout.add_widget(clear_btn)
        layout.add_widget(btn_layout)
        
        self.add_message("Привет! Я Лейла! Напиши мне или нажми 'Шутка'! 😊", False)
        return layout
    
    def add_message(self, text, is_user):
        msg_color = (0, 0.5, 1, 1) if is_user else (0.9, 0.1, 0.5, 1)
        prefix = "Вы: " if is_user else "Лейла: "
        
        msg = Label(
            text=f"{prefix}{text}",
            text_size=(Window.width * 0.9, None),
            halign='left',
            valign='middle',
            color=msg_color,
            size_hint_y=None,
            height=80
        )
        self.chat_layout.add_widget(msg)
        Clock.schedule_once(lambda dt: setattr(self.chat_area, 'scroll_y', 0))
    
    def send_message(self, instance):
        text = self.input.text.strip()
        if text:
            self.add_message(text, True)
            self.input.text = ""
            Clock.schedule_once(lambda dt: self.get_response(text), 0.3)
    
    def get_response(self, text):
        response = self.leila.get_response(text)
        self.add_message(response, False)
    
    def quick_joke(self, instance):
        self.add_message("Шутка!", True)
        Clock.schedule_once(lambda dt: self.get_response("шутка"), 0.3)
    
    def clear_chat(self, instance):
        self.chat_layout.clear_widgets()
        self.add_message("Чат очищен! Привет! 😊", False)

if __name__ == "__main__":
    LeilaApp().run()