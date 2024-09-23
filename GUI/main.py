import sys
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout
from GUI.loginPage import Login_Widget  # Import your login page class
from GUI.signUp import SignUp_Widget    # Import your signup page class

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()

        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Setup the login page
        self.login_page = QWidget()
        self.login_ui = Login_Widget()
        self.login_ui.setupUi(self.login_page)

        # Setup the signup page
        self.signup_page = QWidget()
        self.signup_ui = SignUp_Widget()
        self.signup_ui.setupUi(self.signup_page)

        # Add the login and signup pages to the stacked widget
        self.stacked_widget.addWidget(self.login_page)  # Index 0: Login page
        self.stacked_widget.addWidget(self.signup_page)  # Index 1: Signup page

        # Set the login page to show by default
        self.stacked_widget.setCurrentIndex(0)

        # Set the layout for the main widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Connect the "Sign Up" button to show the signup page
        self.login_ui.newSignUpButton.clicked.connect(self.show_signup)

        # Assuming there is a "Back to Login" button in the signup page
        self.signup_ui.signUpButton.clicked.connect(self.show_login)

    def show_signup(self):
        # Show the signup page
        self.stacked_widget.setCurrentIndex(1)

    def show_login(self):
        # Show the login page
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")  # Try a different style for clarity
    window = MainApplication()
    window.resize(800, 600)  # Explicitly set the size
    window.show()
    sys.exit(app.exec())
