import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem
from numpy import Inf
from qfluentwidgets import SimpleCardWidget, TableWidget, MessageBoxBase, SubtitleLabel, LineEdit, PrimaryPushButton, \
    InfoBar, InfoBarPosition

from main_window.PostManageDB import PostManageDatabaseFactory
from main_window.UserManageDB import UserManageDatabaseFactory


class DelMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('删除评论', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入要删除评论的id')
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
        um = PostManageDatabaseFactory()
        if not um.query_comment_by_comment_id(self.urlLineEdit.text()):
            InfoBar.warning(
                title='Error',
                content="Invalid commentid.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
            return 0
        comment = um.query_comment_by_comment_id(self.urlLineEdit.text())
        um.delete_comment(str(comment[0]), str(comment[1]))

        self.accept()
        self.accepted.emit()


class CommentTableCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.userTable = TableWidget(self)

        self.delBtn = PrimaryPushButton('Delete Comment', self)

        self.delBtn.clicked.connect(lambda: self.showDelMessage())

        self.initCommentTable()

        # 布局

        self.layout = QVBoxLayout(self)
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.delBtn)

        self.layout.addLayout(self.btnLayout)
        self.layout.addWidget(self.userTable)
        # self.setLayout(layout)

    def initCommentTable(self):
        um = PostManageDatabaseFactory()
        results = um.query_all_comments()

        # 设置行数和列数
        self.userTable.setRowCount(len(results))  # 行数为数据的行数
        self.userTable.setColumnCount(4)  # 只显示前4个字段

        # 设置表头标签
        self.userTable.setHorizontalHeaderLabels(['CommentID', 'PostID', 'UserID', 'Content'])

        # 填充表格数据，只取每行的前六个字段
        for row_index, user in enumerate(results):
            for column_index in range(4):  # 只处理前4个字段
                self.userTable.setItem(row_index, column_index, QTableWidgetItem(str(user[column_index])))

    def showDelMessage(self):
        w = DelMessageBox(self.window())
        if w.exec():
            self.initCommentTable()


class ManageCommentWidget(QWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.setObjectName("ManageCommentWidget")
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
        self.commentTableCard = CommentTableCard(self)

        self.Hlayout.addStretch(2)
        self.Hlayout.addWidget(self.commentTableCard, 6)

        self.Hlayout.addStretch(2)

        self.setLayout(self.Hlayout)
