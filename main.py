import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QStatusBar, QMenuBar, QBoxLayout, QButtonGroup, QPushButton, QFrame
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("PyQt6 Window Layout")

        # Create widgets
        self.window_title_label = QLabel("Window Title")
        self.menu_bar_label = QLabel("Menu Bar")
        self.tool_bar_label = QLabel("Toolbar Areas")
        self.dock_label = QLabel("Dock Window Areas")
        self.central_widget_label = QLabel("Central Widget")
        self.status_bar_label = QLabel("Status Bar")

        # Set layout
        self.main_layout = QVBoxLayout()
        self.title_layout = QHBoxLayout()
        self.content_layout = QVBoxLayout()
        self.dock_layout = QVBoxLayout()
        self.central_layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()

        # Add widgets to layouts
        self.title_layout.addWidget(self.window_title_label)
        self.content_layout.addWidget(self.menu_bar_label)
        self.content_layout.addWidget(self.tool_bar_label)
        self.dock_layout.addWidget(self.dock_label)
        self.central_layout.addWidget(self.central_widget_label)
        self.dock_layout.addLayout(self.central_layout)
        self.content_layout.addLayout(self.dock_layout)
        self.bottom_layout.addWidget(self.status_bar_label)

        # Add layouts to main layout
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.content_layout)
        self.main_layout.addLayout(self.bottom_layout)

        # Set main layout
        self.setLayout(self.main_layout)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    pass
