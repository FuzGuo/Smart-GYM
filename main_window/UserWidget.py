import os
import re
import shutil

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QIcon, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QFileDialog
from qfluentwidgets import LineEdit, SimpleCardWidget, ComboBox, SpinBox, PrimaryPushButton, SingleDirectionScrollArea, \
    TransparentToolButton, AvatarWidget, PushButton, CaptionLabel, InfoBar, InfoBarPosition

from main_window.UserManageDB import UserManageDatabaseFactory


class UserInfoCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.avatar = QImage('resource/avatar1.jpg').scaled(
        # 24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.uploadAvatar = PushButton('Upload New Avatar')
        self.userNameEdit = LineEdit()
        self.emailEdit = LineEdit()
        self.selectGender = ComboBox()
        items = ['Male', 'Female']
        for item in items:
            self.selectGender.addItem(item)
        self.selectAge = SpinBox()
        self.saveButton = PrimaryPushButton('Save')

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.vBoxLayout2 = QVBoxLayout()
        self.vBoxLayout3 = QVBoxLayout()
        self.userLabel = CaptionLabel("User Name:")
        self.emailLabel = CaptionLabel("Email:")
        self.genderLabel = CaptionLabel("Gender:")
        self.ageLabel = CaptionLabel("Age:")
        self.remindLabel = CaptionLabel("")
        self.remindLabel.setTextColor(QColor(139, 0, 0))
        self.initLayout()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.avatar)
        self.vBoxLayout.addWidget(self.uploadAvatar)
        self.vBoxLayout.addSpacing(5)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addLayout(self.vBoxLayout2)
        self.hBoxLayout.addLayout(self.vBoxLayout3)

        self.vBoxLayout2.addWidget(self.userLabel)
        self.vBoxLayout2.addSpacing(5)
        self.vBoxLayout2.addWidget(self.emailLabel)
        self.vBoxLayout2.addSpacing(5)
        self.vBoxLayout2.addWidget(self.genderLabel)
        self.vBoxLayout2.addSpacing(5)
        self.vBoxLayout2.addWidget(self.ageLabel)

        self.vBoxLayout3.addWidget(self.userNameEdit)
        self.vBoxLayout3.addSpacing(5)
        self.vBoxLayout3.addWidget(self.emailEdit)
        self.vBoxLayout3.addSpacing(5)
        self.vBoxLayout3.addWidget(self.selectGender)
        self.vBoxLayout3.addSpacing(5)
        self.vBoxLayout3.addWidget(self.selectAge)

        self.vBoxLayout.addSpacing(5)
        self.vBoxLayout.addWidget(self.saveButton)
        self.vBoxLayout.addWidget(self.remindLabel,0,Qt.AlignCenter)


class UserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.userid = None
        # self.setWindowTitle(title)
        self.initUI()
        # self.initButton()

    def initUI(self):
        # 设置布局
        # self.view = QWidget(self)
        self.Vlayout = QVBoxLayout(self)
        self.userCard = UserInfoCard(self)
        self.userCard.setMinimumWidth(400)  # 设置最小宽度
        self.userCard.setMaximumWidth(400)  # 设置最大宽度，与最小宽度相同，固定宽度为200像素

        self.avatar = AvatarWidget('resource/avatar1.jpg')
        self.avatar.setRadius(64)

        # self.avatar.setAlignment(Qt.AlignCenter)

        # self.avatar.setMinimumHeight(64)  # 设置最小宽度
        # self.avatar.setMaximumHeight(64)  # 设置最大宽度，与最小宽度相同，固定宽度为200像素
        self.Vlayout.addWidget(self.avatar, 2, alignment=Qt.AlignCenter)
        # self.Vlayout.setSpacing(5)
        # self.Vlayout.setContentsMargins(0, 0, 10, 30)
        # self.Vlayout.addWidget(self.avatar, 0,alignment = Qt.AlignTop)
        self.Hlayout = QHBoxLayout()
        self.Vlayout.addWidget(self.userCard, 5, alignment=Qt.AlignCenter)
        spacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.Vlayout.addItem(spacer)

        self.setLayout(self.Vlayout)

        self.userCard.saveButton.clicked.connect(self.saveUserInfo)

    def is_valid_email(self, email):
        # 定义一个电子邮件的正则表达式
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # 使用re.match来检查是否匹配
        if re.match(pattern, email):
            return True
        else:
            return False

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Lesson 4',
            content="With respect, let's advance towards a new stage of the spin.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )
    def saveUserInfo(self):
        um = UserManageDatabaseFactory()
        result = um.query_user_by_id(self.userid)
        if self.userCard.userNameEdit.text() == result[1]:
            pass
        elif um.query_user_by_name(self.userCard.userNameEdit.text()):
            # self.userCard.remindLabel.setText("Username is already existed.")
            InfoBar.warning(
                title='Error',
                content="Username is already existed.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0
        if not self.is_valid_email(self.userCard.emailEdit.text()):
            # self.userCard.remindLabel.setText("Email is not valid.")
            InfoBar.warning(
                title='Error',
                content="Invalid Email.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0
        gender = self.userCard.selectGender.text()[0]
        age = self.userCard.selectAge.value()
        um.save_user_info(self.userCard.userNameEdit.text(), gender, age, self.userCard.emailEdit.text(), self.userid)
        InfoBar.success(
            title='Success',
            content="Save successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )
        pass


