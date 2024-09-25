from PySide6.QtWidgets import QApplication, QDialog, QStackedWidget, QWidget
import sys

# Import the widget classes from your module
from GUI.loginPage import Login_Widget
from GUI.signUp import SignUp_Widget

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Login_Widget()
        self.ui.setupUi(self)
        # Make sure to connect after setupUi, where the button is presumably instantiated
        self.ui.newSignUpButton.clicked.connect(self.goToSignUp)

    def goToSignUp(self):
        global widget  # Use global to refer to the widget defined in main
        widget.setCurrentIndex(1)  # Assumes that SignUpWidget is at index 1

class SignUpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = SignUp_Widget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()  # Define widget globally if used in other parts of the code

    mainWindow = LoginWidget()
    screen2 = SignUpWidget()

    widget.addWidget(mainWindow)
    widget.addWidget(screen2)

    widget.setMinimumHeight(600)
    widget.setMinimumWidth(800)
    widget.show()

    sys.exit(app.exec())
