import sys

from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QHBoxLayout
from qfluentwidgets import SimpleCardWidget, PushButton, CaptionLabel, TitleLabel


class RecordButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.titleLabel = CaptionLabel("Record", self)
        # self.titleLabel.setStyleSheet("font-weight: bold;")
        self.logoSVGWidget = QSvgWidget("resource/icons/record-svgrepo-com.svg", self)
        self.logoSVGWidget.setFixedSize(20, 20)
        self.textLabel = CaptionLabel("Track your progress and milestones to stay motivated and on course.", self)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("color:gray;")
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.logoSVGWidget)
        self.hBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.textLabel)
        self.setFixedSize(200, 100)

class ChatButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.titleLabel = CaptionLabel("Chat", self)
        # self.titleLabel.setStyleSheet("font-weight: bold;")
        self.logoSVGWidget = QSvgWidget("resource/icons/chat-svgrepo-com.svg", self)
        self.logoSVGWidget.setFixedSize(20, 20)
        self.textLabel = CaptionLabel("Connect with trainers and fitness enthusiasts for support and motivation.", self)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("color:gray;")
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.logoSVGWidget)
        self.hBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.textLabel)
        self.setFixedSize(200, 100)

class PlanButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.titleLabel = CaptionLabel("Plan", self)
        # self.titleLabel.setStyleSheet("font-weight: bold;")
        self.logoSVGWidget = QSvgWidget("resource/icons/plan-svgrepo-com.svg", self)
        self.logoSVGWidget.setFixedSize(20, 20)
        self.textLabel = CaptionLabel("Create and manage tailored fitness plans to achieve your goals.", self)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("color:gray;")
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.logoSVGWidget)
        self.hBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.textLabel)
        self.setFixedSize(200, 100)

class ExerciseButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.titleLabel = CaptionLabel("Exercise", self)
        # self.titleLabel.setStyleSheet("font-weight: bold;")
        self.logoSVGWidget = QSvgWidget("resource/icons/exercise-ball-svgrepo-com.svg", self)
        self.logoSVGWidget.setFixedSize(20, 20)
        self.textLabel = CaptionLabel("Discover personalized workouts to challenge and transform your body.", self)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("color: gray;")
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.logoSVGWidget)
        self.hBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.textLabel)
        self.setFixedSize(200, 100)


# class RecordByMonth(SimpleCardWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)


class HomeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HomeWidget")

        self.logoSVG = QSvgWidget("resource/icons/dumbbell-svgrepo-com.svg", self)
        self.logoSVG.setFixedSize(150, 150)
        self.titleLabel = TitleLabel("Transform Your Body, Elevate Your Life.", self)
        self.card1 = ExerciseButton(self)
        self.card2 = PlanButton(self)
        self.card3 = ChatButton(self)
        self.card4 = RecordButton(self)

        self.card1.clicked.connect(lambda: self.window().switchTo(self.window().appInterface))
        self.card2.clicked.connect(lambda: self.window().switchTo(self.window().planInterface))
        self.card3.clicked.connect(lambda: self.window().switchTo(self.window().chatInterface))
        self.card4.clicked.connect(lambda: self.window().switchTo(self.window().recordInterface))
        # self.vBoxLayout = QVBoxLayout(self)

        # self.vBoxLayout.addWidget(self.logoSVG, 0, Qt.AlignCenter)
        # self.vBoxLayout.addWidget(self.card1)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.vBoxLayout.addStretch(3)
        self.vBoxLayout.addWidget(self.logoSVG, 1, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.titleLabel, 1, Qt.AlignCenter)
        self.vBoxLayout.addLayout(self.hBoxLayout1, 1)
        self.hBoxLayout1.addWidget(self.card1)
        self.hBoxLayout1.addWidget(self.card2)
        self.vBoxLayout.addLayout(self.hBoxLayout2, 1)
        self.hBoxLayout2.addWidget(self.card3)
        self.hBoxLayout2.addWidget(self.card4)
        self.vBoxLayout.addStretch(3)

        self.hBoxLayout.addStretch(1)


