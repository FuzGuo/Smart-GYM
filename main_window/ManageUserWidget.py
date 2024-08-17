import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem
from numpy import Inf
from qfluentwidgets import SimpleCardWidget, TableWidget, MessageBoxBase, SubtitleLabel, LineEdit, PrimaryPushButton, \
    InfoBar, InfoBarPosition

from main_window.UserManageDB import UserManageDatabaseFactory


class DelMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('删除用户', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入要删除用户的uid')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 设置只能输入整数的限制
        int_validator = QIntValidator()  # 设置一个合理的范围
        self.urlLineEdit.setValidator(int_validator)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)
        # 重新指向
        self.yesButton.clicked.disconnect()
        self.yesButton.clicked.connect(lambda: self.__onYesButtonClicked())

    def __onYesButtonClicked(self):
        um = UserManageDatabaseFactory()
        if not um.query_user_by_id(self.urlLineEdit.text()):
            InfoBar.warning(
                title='Error',
                content="Invalid Userid.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0
        um.delete_user_by_id(self.urlLineEdit.text())

        self.accept()
        self.accepted.emit()


def is_valid_email(email):
    # 定义一个电子邮件的正则表达式
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # 使用re.match来检查是否匹配
    if re.match(pattern, email):
        return True
    else:
        return False


class AddMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('增加用户', self)
        self.urlLineEdit = LineEdit()
        self.passwordLineEdit = LineEdit()
        self.emailLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入要增加用户的用户名')
        self.urlLineEdit.setClearButtonEnabled(True)

        self.emailLineEdit.setPlaceholderText('输入要增加用户的邮箱')
        self.emailLineEdit.setClearButtonEnabled(True)

        self.passwordLineEdit.setPlaceholderText('输入要增加用户的密码')
        self.passwordLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)
        self.viewLayout.addWidget(self.emailLineEdit)
        self.viewLayout.addWidget(self.passwordLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)
        # 重新指向
        self.yesButton.clicked.disconnect()
        self.yesButton.clicked.connect(lambda: self.__onYesButtonClicked())

    def __onYesButtonClicked(self):
        um = UserManageDatabaseFactory()
        if not is_valid_email(self.emailLineEdit.text()):
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
        elif um.query_user_by_name(self.urlLineEdit.text()):
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
        elif self.passwordLineEdit.text() == '':
            InfoBar.warning(
                title='Error',
                content="Invalid Password.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0
        elif self.urlLineEdit.text().strip() == '':
            InfoBar.warning(
                title='Error',
                content="Invalid Username.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0

        um.add_user(self.urlLineEdit.text(), self.passwordLineEdit.text(), self.emailLineEdit.text())
        InfoBar.success(
            title='Success',
            content="Add successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.parent()
        )

        self.accept()
        self.accepted.emit()


class EditMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('编辑用户', self)
        self.urlLineEdit = LineEdit()
        self.userNameEdit = LineEdit()
        self.passwordLineEdit = LineEdit()
        self.emailLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入要编辑用户的用户uid')
        self.urlLineEdit.setClearButtonEnabled(True)

        self.userNameEdit.setPlaceholderText('输入要编辑用户的用户名')
        self.userNameEdit.setClearButtonEnabled(True)

        self.emailLineEdit.setPlaceholderText('输入要编辑用户的邮箱')
        self.emailLineEdit.setClearButtonEnabled(True)

        self.passwordLineEdit.setPlaceholderText('输入要增加用户的密码')
        self.passwordLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)
        self.viewLayout.addWidget(self.userNameEdit)
        self.viewLayout.addWidget(self.emailLineEdit)
        self.viewLayout.addWidget(self.passwordLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)
        # 重新指向
        self.yesButton.clicked.disconnect()
        self.yesButton.clicked.connect(lambda: self.__onYesButtonClicked())

    def __onYesButtonClicked(self):
        um = UserManageDatabaseFactory()
        if not is_valid_email(self.emailLineEdit.text()):
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
        elif um.query_user_by_name(self.userNameEdit.text()):
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
        elif self.passwordLineEdit.text() == '':
            InfoBar.warning(
                title='Error',
                content="Invalid Password.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0

        um.edit_user_info(self.userNameEdit.text(), self.passwordLineEdit.text(), self.emailLineEdit.text(),
                          self.urlLineEdit.text())
        InfoBar.success(
            title='Success',
            content="Edit successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.parent()
        )

        self.accept()
        self.accepted.emit()


class UserTableCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.userTable = TableWidget(self)

        self.delBtn = PrimaryPushButton('Delete User', self)
        self.addBtn = PrimaryPushButton('Add User', self)
        self.editBtn = PrimaryPushButton('Edit User', self)

        self.delBtn.clicked.connect(lambda: self.showDelMessage())
        self.addBtn.clicked.connect(lambda: self.showAddMessage())
        self.editBtn.clicked.connect(lambda: self.showEditMessage())

        self.initUserTable()

        # 布局

        self.layout = QVBoxLayout(self)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.delBtn)
        self.btnLayout.addWidget(self.addBtn)
        self.btnLayout.addWidget(self.editBtn)
        self.layout.addLayout(self.btnLayout)
        self.layout.addWidget(self.userTable)
        # self.setLayout(layout)

    def initUserTable(self):
        um = UserManageDatabaseFactory()
        results = um.query_all()

        # 设置行数和列数
        self.userTable.setRowCount(len(results))  # 行数为数据的行数
        self.userTable.setColumnCount(6)  # 只显示前六个字段

        # 设置表头标签
        self.userTable.setHorizontalHeaderLabels(['UserID', 'Name', 'Gender', 'Age', 'Email', 'Password'])

        # 填充表格数据，只取每行的前六个字段
        for row_index, user in enumerate(results):
            for column_index in range(6):  # 只处理前六个字段
                self.userTable.setItem(row_index, column_index, QTableWidgetItem(str(user[column_index])))

    def showDelMessage(self):
        w = DelMessageBox(self.window())
        if w.exec():
            self.initUserTable()

    def showAddMessage(self):
        w = AddMessageBox(self.window())
        if w.exec():
            self.initUserTable()

    def showEditMessage(self):
        w = EditMessageBox(self.window())
        if w.exec():
            self.initUserTable()


class ManageUserWidget(QWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.setObjectName("ManageUserWidget")
        self.userid = userid

        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
                    Demo{background: white}
                    QLabel{
                        font: 20px 'Segoe UI';
                        background: rgb(242,242,242);
                        border-radius: 8px;
                        color: black
                    }
                """)
        self.Hlayout = QHBoxLayout(self)
        self.userTableCard = UserTableCard(self)

        self.Hlayout.addStretch(1)
        self.Hlayout.addWidget(self.userTableCard, 6)

        self.Hlayout.addStretch(1)

        self.setLayout(self.Hlayout)
