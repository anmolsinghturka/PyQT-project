import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox, QComboBox, QSpinBox, QSlider, QDial, QProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQT App by Anmol Singh")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layout for central widget
        vbox = QVBoxLayout()

        # Add label to layout
        label = QLabel("Hello From Anmol Singh", self)
        vbox.addWidget(label)

        # Add button to layout
        button = QPushButton("Click me!", self)
        button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(button)

        # Add line edit to layout
        line_edit = QLineEdit(self)
        vbox.addWidget(line_edit)

        # Add text edit to layout
        text_edit = QTextEdit(self)
        vbox.addWidget(text_edit)

        # Add checkbox to layout
        checkbox = QCheckBox("Check me!", self)
        vbox.addWidget(checkbox)

        # Add combo box to layout
        combo_box = QComboBox(self)
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        vbox.addWidget(combo_box)

        # Add spin box to layout
        spin_box = QSpinBox(self)
        vbox.addWidget(spin_box)

        # Add slider to layout
        slider = QSlider(self)
        slider.setOrientation(1)
        vbox.addWidget(slider)

        # Add dial to layout
        dial = QDial(self)
        vbox.addWidget(dial)

        # Add progress bar to layout
        progress_bar = QProgressBar(self)
        vbox.addWidget(progress_bar)

        # Set layout for central widget
        central_widget.setLayout(vbox)

    def on_button_clicked(self):
        print("Button clicked! for Sony Pictures")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
