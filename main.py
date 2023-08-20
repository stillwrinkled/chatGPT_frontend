from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from backend import Chatbot
import sys
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 60, 40)
        # self.button.setStyleSheet("QPushButton { border: 2px solid #D3D3D3; border-radius: 5px; }")
        self.button.setStyleSheet("""
            QPushButton {
                border: 2px solid #D3D3D3;
                border-radius: 5px;
            }
            QPushButton:pressed {
                background-color: #007AFF;
            }
        """)  # from ChatGPT
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()  # v imp. captures user input
        self.chat_area.append(f"<p style='color: #333333'> me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color: #333333; background-color: #E9E9E9'> chatGPT: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
