# coding:utf-8
import os
import shutil
import sys
import uuid

from PySide6.QtCore import Qt, Signal, QEasingCurve, QUrl, QRect
from PySide6.QtGui import QIcon, QDesktopServices, QFont, QBrush, QColor, QPainter, QImage, QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QApplication, QFrame, QWidget, QPushButton, QFileDialog

from qfluentwidgets import (NavigationBar, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, SearchLineEdit,
                            PopUpAniStackedWidget, getFont, FlowLayout, SplitFluentWindow, InfoBar, InfoBarPosition)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.date_time.calendar_view import CalendarView
from qframelesswindow import FramelessWindow, TitleBar

from main_window.ManageCommentWidget import ManageCommentWidget
from main_window.ManagePostWidget import ManagePostWidget
from main_window.ManageUserWidget import ManageUserWidget
from main_window.ChatWidget import ChatWidget
from main_window.ExerciseWidget import ExerciseWidget
from main_window.HomeWidget import HomeWidget
from main_window.PlanWidget import PlanWidget
from main_window.RecordWidget import RecordWidget
from main_window.SettingWidget import SettingInterface
from main_window.UserManageDB import UserManageDatabaseFactory
from main_window.UserWidget import UserWidget


class Widget(QWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class StackedWidget(QFrame):
    """ Stacked widget """

    currentChanged = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.view = PopUpAniStackedWidget(self)

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.view)

        self.view.currentChanged.connect(self.currentChanged)

    def addWidget(self, widget):
        """ add widget to view """
        self.view.addWidget(widget)

    def widget(self, index: int):
        return self.view.widget(index)

    def setCurrentWidget(self, widget, popOut=False):
        if not popOut:
            self.view.setCurrentWidget(widget, duration=300)
        else:
            self.view.setCurrentWidget(
                widget, True, False, 200, QEasingCurve.InQuad)

    def setCurrentIndex(self, index, popOut=False):
        self.setCurrentWidget(self.view.widget(index), popOut)


class AvatarWidget(NavigationWidget):
    """ Avatar widget """

    def __init__(self, parent=None):
        super().__init__(isSelectable=False, parent=parent)
        self.avatar = QImage('../resource/shoko.png').scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)

        if self.isPressed:
            painter.setOpacity(0.7)

        # draw background
        if self.isEnter:
            c = 255 if isDarkTheme() else 0
            painter.setBrush(QColor(c, c, c, 10))
            painter.drawRoundedRect(self.rect(), 5, 5)

        # draw avatar
        painter.setBrush(QBrush(self.avatar))
        painter.translate(8, 6)
        painter.drawEllipse(0, 0, 24, 24)
        painter.translate(-8, -6)

        if not self.isCompacted:
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
            font = QFont('Segoe UI')
            font.setPixelSize(14)
            painter.setFont(font)
            painter.drawText(QRect(44, 0, 255, 36), Qt.AlignVCenter, 'zhiyiYo')


class CustomTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(48)
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 20)
        self.hBoxLayout.insertWidget(
            1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(
            2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        self.avatar = AvatarWidget()
        # add search line edit
        # self.searchLineEdit = SearchLineEdit(self)
        # self.searchLineEdit.setPlaceholderText('搜索应用、游戏、电影、设备等')
        # self.searchLineEdit.setFixedWidth(400)
        # self.searchLineEdit.setClearButtonEnabled(True)

        self.vBoxLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignTop)
        self.buttonLayout.addWidget(self.avatar)
        self.buttonLayout.addWidget(self.minBtn)
        self.buttonLayout.addWidget(self.maxBtn)
        self.buttonLayout.addWidget(self.closeBtn)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.vBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout, 0)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))

    # def resizeEvent(self, e):
    #     self.avatar.move((self.width() - self.avatar.width()) // 1.18, 3)


class BWidget(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.initUI()

    def initUI(self):
        # 设置布局
        layout = QVBoxLayout(self)

        # 添加标签
        label = QLabel("Record Interface", self)
        layout.addWidget(label)

        # 添加按钮
        btn1 = QPushButton('Button 1', self)
        btn1.clicked.connect(lambda: self.on_button_clicked(btn1))

        btn2 = QPushButton('Button 2', self)
        btn2.clicked.connect(lambda: self.on_button_clicked(btn2))

        btn3 = QPushButton('Button 3', self)
        btn3.clicked.connect(lambda: self.on_button_clicked(btn3))

        # 将按钮添加到布局中
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)

    def on_button_clicked(self, btn):
        # 按钮点击事件处理函数
        print(f"{btn.text()} was clicked")


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        layout = FlowLayout(self, needAni=True)  # 启用动画

        # 自定义动画参数
        layout.setAnimation(250, QEasingCurve.OutQuad)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(10)

        layout.addWidget(QPushButton('aiko'))
        layout.addWidget(QPushButton('刘静爱'))
        layout.addWidget(QPushButton('柳井爱子'))
        layout.addWidget(QPushButton('aiko 赛高'))
        layout.addWidget(QPushButton('aiko 太爱啦😘'))

        self.resize(250, 300)


class Window(FramelessWindow):

    def __init__(self, user):
        super().__init__()

        self.user = None

        self.ctitleBar = CustomTitleBar(self)
        self.setTitleBar(self.ctitleBar)

        # use dark theme mode
        setTheme(Theme.LIGHT)

        # change the theme color
        # setThemeColor('#0078d4')

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationBar = NavigationBar(self)
        self.stackWidget = StackedWidget(self)

        # create sub interface


        self.chatInterface = ChatWidget(self, user[0])
        self.homeInterface = HomeWidget(self)
        self.settingInterface = SettingInterface(self)
        self.planInterface = PlanWidget(self, user[0])
        self.appInterface = ExerciseWidget(self, user[0])
        self.recordInterface = RecordWidget(self, user[0])
        if user[7] == 1:
            self.manageUserInterface = ManageUserWidget(self)
            self.managePostInterface = ManagePostWidget(self)
            self.manageCommentInterface = ManageCommentWidget(self)
        self.userInterface = UserWidget(self)
        self.userInterface.setObjectName("userwidget")
        self.user = user
        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()
        self.initWindow()
        self.initUser()
        self.userInterface.userCard.uploadAvatar.clicked.connect(lambda: self.uploadAvatar(userid=self.user[0]))


    def initUser(self):
        um = UserManageDatabaseFactory()
        self.user = um.query_user_by_id(self.user[0])
        self.userInterface.userCard.userNameEdit.setText(self.user[1])
        self.userInterface.userid = self.user[0]
        self.userInterface.userCard.emailEdit.setText(self.user[4])
        self.userInterface.userCard.selectAge.setValue(self.user[3])
        self.userInterface.avatar.setImage(self.user[6])
        self.userInterface.avatar.setRadius(64)
        if self.user[2] == 'M':
            self.userInterface.userCard.selectGender.setCurrentIndex(0)
        else:
            self.userInterface.userCard.selectGender.setCurrentIndex(1)
        image = QPixmap(self.user[6])
        size = min(image.width(), image.height())
        cropped_image = image.copy(
            (image.width() - size) // 2,
            (image.height() - size) // 2,
            size, size
        )
        self.ctitleBar.avatar.avatar = cropped_image.scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.chatInterface.myPostArea.userid = self.user[0]


    def uploadAvatar(self, userid):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Avatar", "", "Image files (*.jpg *.png *.jpeg)")
        if file_path:
            # 生成新的文件名和路径
            basename = uuid.uuid4().hex
            new_path = os.path.join("resource/avatars", basename)

            # 复制文件到新位置
            shutil.copy(file_path, new_path)

            # 显示新头像并更新数据库
            # self.avatarPath = new_path
            um = UserManageDatabaseFactory()
            um.upload_avatar(new_path, userid)
            self.userInterface.avatar.setImage(new_path)
            self.userInterface.avatar.setRadius(64)
            image = QPixmap(new_path)
            # 确保图像是正方形
            size = min(image.width(), image.height())
            cropped_image = image.copy(
                (image.width() - size) // 2,
                (image.height() - size) // 2,
                size, size
            )
            self.ctitleBar.avatar.avatar = cropped_image.scaled(
            24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            del um
            InfoBar.success(
                title='Success',
                content="Avatar uploaded successfully.",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000,
                parent=self
            )

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 48, 0, 0)
        self.hBoxLayout.addWidget(self.navigationBar)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home', selectedIcon=FIF.HOME_FILL)
        self.addSubInterface(self.appInterface, FIF.SEND, 'Exercise', selectedIcon=FIF.SEND_FILL)
        self.addSubInterface(self.chatInterface, FIF.CHAT, 'Chat')
        self.addSubInterface(self.planInterface, FIF.DATE_TIME, 'Plan')
        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Setting', NavigationItemPosition.BOTTOM, )
        self.addSubInterface(self.recordInterface, FIF.PIE_SINGLE, 'Record', )
        self.addSubInterface(self.userInterface, FIF.PEOPLE, 'User')
        if self.user[7] == 1:
            self.addSubInterface(self.manageUserInterface, FIF.FILTER, 'Admin_user')
            self.addSubInterface(self.managePostInterface, FIF.ROBOT, 'Admin_Post')
            self.addSubInterface(self.manageCommentInterface, FIF.CHAT, 'Admin_comment')
        self.navigationBar.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='Help',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.navigationBar.setCurrentItem(self.homeInterface.objectName())
        self.ctitleBar.avatar.clicked.connect(lambda: self.switchTo(self.userInterface))
        # add custom widget to bottom
        # self.navigationBar.addItem(
        #     routeKey='avatar',
        #     # widget=AvatarWidget(),
        #     onClick=self.showMessageBox,
        #     position=NavigationItemPosition.BOTTOM
        # )
        # hide the text of button when selected
        # self.navigationBar.setSelectedTextVisible(False)

        # adjust the font size of button
        # self.navigationBar.setFont(getFont(12))

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('AI GYM')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, selectedIcon=None):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationBar.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            selectedIcon=selectedIcon,
            position=position,
        )

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'resource/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)
        self.appInterface.update_widget()
        self.planInterface.calendarCard.taskArea.initTasks()
        self.initUser()

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationBar.setCurrentItem(widget.objectName())

    def showMessageBox(self):
        w = MessageBox(
            '支持作者',
            '开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('Yes')
        w.cancelButton.setText('Cancel')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/FuzGuo"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    w.ctitleBar.avatar.avatar = QImage('../resource/avatar1.jpg').scaled(
        24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    app.exec()
