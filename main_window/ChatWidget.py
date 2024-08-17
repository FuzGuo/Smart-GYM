from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QIntValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QScrollArea, QFrame
from qfluentwidgets import SingleDirectionScrollArea, Pivot, setTheme, Theme, SimpleCardWidget, PushButton, LineEdit, \
    ComboBox, SpinBox, PrimaryPushButton, CaptionLabel, ProgressRing, IndeterminateProgressRing, AvatarWidget, \
    TitleLabel, TransparentToolButton, InfoBadge, InfoBadgePosition, TransparentPushButton, RoundMenu, Action, \
    ToolButton, TextEdit, DropDownPushButton, MessageBoxBase, SmoothScrollArea, NavigationSeparator, InfoBar, \
    InfoBarPosition, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF

from main_window.PostManageDB import PostManageDatabaseFactory
from main_window.SensitiveWordChecker import SensitiveWordChecker
from main_window.UserManageDB import UserManageDatabaseFactory


class CommentArea(SmoothScrollArea):
    def __init__(self, parent=None, postId=None):
        super().__init__(parent)

        self.postId = postId
        self.comments = self.initComments()

        self.view = QWidget(self)

        self.vBoxLayout = QVBoxLayout(self.view)

        self.setWidget(self.view)
        self.setWidgetResizable(True)

        # self.commentCard = Comment(parent=None, comment=self.comments[0])
        # self.vBoxLayout.setSpacing(10)
        # self.vBoxLayout.setContentsMargins(0, 0, 10, 30)

        self.setStyleSheet("QScrollArea { background:rgb(242,242,242);border-radius: 8px;")
        self.view.setStyleSheet('QWidget {background:rgb(242,242,242)};border-radius: 8px;')

        self.initLayout()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.commentCard, 0, Qt.AlignTop)
        pass

    def initComments(self):
        pm = PostManageDatabaseFactory()
        comments = pm.query_comment_by_post_id(self.postId)
        if comments:
            return comments
        pass

    def creatComment(self):
        pass


class Comment(QWidget):
    def __init__(self, parent=None, comment=None):
        super().__init__(parent)
        # self.progressRing = IndeterminateProgressRing(self)
        # self.progressRing.setVisible(True)
        self.messageNum = None
        self.likeNum = None
        self.comment = comment
        self.avatar = AvatarWidget(self)
        self.userNameLabel = CaptionLabel(self)
        self.contextLabel = CaptionLabel(self)
        self.userNameLabel.setStyleSheet("QLabel{background-color : rgba(0, 0, 0, 0);} ")
        self.contextLabel.setStyleSheet("QLabel{background-color : rgba(0, 0, 0, 0);} ")
        # self.likeButton = TransparentPushButton(FIF.HEART, "2000w", self)
        # self.messageButton = TransparentPushButton(FIF.MESSAGE, "2000w", self)
        self.moreButton = DropDownPushButton(FIF.MORE, 'More')
        if comment[2] != self.parent().parent().parent().parent().userid:
            self.moreButton.hide()

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        self.initComment(comment)
        self.initLayout()

    def initComment(self, comment):
        if not comment:
            self.close()
            return 0

        self.avatar.setImage(comment[6])
        self.avatar.setRadius(20)
        self.userNameLabel.setText(comment[7])
        self.contextLabel.setText(comment[3])

    def initLayout(self):
        self.vBoxLayout.addWidget(self.separator)
        self.vBoxLayout.addLayout(self.hBoxLayout1)
        self.hBoxLayout1.addWidget(self.avatar)
        self.hBoxLayout1.addWidget(self.userNameLabel)
        self.hBoxLayout1.addWidget(self.moreButton, 0, Qt.AlignRight)
        self.vBoxLayout.addWidget(self.contextLabel, 0, Qt.AlignLeft)
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        # self.hBoxLayout2.addWidget(self.messageButton, 10, Qt.AlignRight)
        # self.hBoxLayout2.addWidget(self.likeButton, 1, Qt.AlignRight)

        self.menu = RoundMenu(parent=self.moreButton)
        del_action = Action(FIF.DELETE, 'Delete')
        del_action.triggered.connect(lambda: self.delete_self())
        self.menu.addActions([
            del_action
        ])

        self.moreButton.setMenu(self.menu)
        # self.vBoxLayout.addWidget(self.avatar)
        # self.vBoxLayout.addWidget(self.progressRing, 0, Qt.AlignCenter)
        pass

    def delete_self(self):
        self.parent().messageButton.setText(str(int(self.parent().messageButton.text()) - 1))
        pm = PostManageDatabaseFactory()
        pm.delete_comment(self.comment[0], self.comment[1])
        self.setParent(None)
        self.deleteLater()


class CommentBox(MessageBoxBase):
    def __init__(self, parent=None, post=None):
        super().__init__(parent)
        self.post = post
        self.postWidget = Post(self, post)
        self.postWidget.moreButton.close()
        self.postWidget.messageButton.close()
        self.commentArea = CommentArea(self, post[0])
        self.viewLayout.addWidget(self.postWidget)
        self.viewLayout.addWidget(self.commentArea, 0, Qt.AlignTop)
        self.widget.setMinimumWidth(500)
        # self.widget.setWidgetResizable(True)


class LoadingPost(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.progressRing = IndeterminateProgressRing(self)
        self.progressRing.setVisible(True)
        self.vBoxLayout = QVBoxLayout(self)
        # self.delButton = PrimaryPushButton("Delete", self)
        # self.delButton.clicked.connect(lambda: self.close())
        self.initLayout()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.avatar)
        self.vBoxLayout.addWidget(self.progressRing, 0, Qt.AlignCenter)
        # self.vBoxLayout.addWidget(self.delButton)
        pass


class AddComment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.postEdit = TextEdit()
        # self.addPostButton = ToolButton(FIF.ADD, self)
        # self.addPostButton.setMinimumSize(500, 50)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()
        self.avatar = AvatarWidget()
        self.publishButton = PrimaryPushButton("Publish", self)
        self.publishButton.clicked.connect(lambda: self.addComment())
        self.userid = self.parent().parent().parent().parent().userid
        self.post_id = self.parent().post[0]
        # self.uploadImageButton = TransparentToolButton(FIF.PHOTO, self)
        self.initAddComment()
        self.initLayout()

    def initAddComment(self):
        pm = PostManageDatabaseFactory()

        user = pm.query_user_by_id(self.parent().parent().parent().parent().userid)
        self.avatar.setImage(user[6])
        self.avatar.setRadius(20)

    def initLayout(self):
        self.vBoxLayout.addLayout(self.hBoxLayout, 5)
        self.hBoxLayout.addWidget(self.avatar, 0, Qt.AlignTop)
        self.hBoxLayout.addWidget(self.postEdit)
        self.vBoxLayout.addLayout(self.hBoxLayout2, 1)
        spacer = QSpacerItem(35, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.hBoxLayout2.addItem(spacer)
        # self.hBoxLayout2.addWidget(self.uploadImageButton, 0, Qt.AlignLeft)

        self.hBoxLayout2.addWidget(self.publishButton, 0, Qt.AlignRight)

    def addComment(self):
        wc = SensitiveWordChecker()
        pm = PostManageDatabaseFactory()
        pm.add_comment(self.postEdit.toPlainText(), self.userid, self.post_id)
        new_comment = pm.query_comment_by_post_id(self.post_id)[-1]

        new_comment = Comment(self.parent(), new_comment)

        # 移除最后一个 stretch
        # self.vBoxLayout.takeAt(self.vBoxLayout.count() - 1)

        self.parent().vBoxLayout1.insertWidget(1, new_comment)
        self.parent().messageButton.setText(str(int(self.parent().messageButton.text()) + 1))

        InfoBar.success(
            title='Success',
            content="Publish successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.window()
        )
        self.postEdit.setText('')

        result, found_words = wc.check_text(self.postEdit.toPlainText())
        if result:
            InfoBar.warning(
                title='Error',
                content="有敏感词，请修改你的文本.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0



class PublishPostMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('设置一个标题', self)
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('为你的帖子设置一个标题')
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
        self.accept()
        self.accepted.emit()


class EditPostMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None, title='', context='', post_id=None):
        super().__init__(parent)
        self.post_id = post_id
        self.titleLabel = SubtitleLabel('编辑帖子', self)
        self.urlLineEdit = LineEdit()
        self.postEdit = TextEdit()

        self.urlLineEdit.setPlaceholderText('为你的帖子设置一个标题')
        self.urlLineEdit.setClearButtonEnabled(True)

        self.postEdit.setText(context)

        self.urlLineEdit.setText(title)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)
        self.viewLayout.addWidget(self.postEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)
        # 重新指向
        self.yesButton.clicked.disconnect()
        self.yesButton.clicked.connect(lambda: self.__onYesButtonClicked())

    def __onYesButtonClicked(self):
        wc = SensitiveWordChecker()
        result, found_words = wc.check_text(self.urlLineEdit.text())
        result2, found_words = wc.check_text(self.postEdit.toPlainText())
        if result or result2:
            InfoBar.warning(
                title='Error',
                content="有敏感词，请修改你的文本.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0
        pm = PostManageDatabaseFactory()
        pm.edit_post(self.urlLineEdit.text(), self.postEdit.toPlainText(), self.post_id)
        self.accept()
        self.accepted.emit()


class AddPost(SimpleCardWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.postEdit = TextEdit()
        self.userid = userid
        # self.addPostButton = ToolButton(FIF.ADD, self)
        # self.addPostButton.setMinimumSize(500, 50)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()
        self.avatar = AvatarWidget()
        self.publishButton = PrimaryPushButton("Publish", self)
        # self.uploadImageButton = TransparentToolButton(FIF.PHOTO, self)
        self.publishButton.clicked.connect(lambda: self.publishPost())
        self.initAddPost()
        self.initLayout()

    def initAddPost(self):
        pm = PostManageDatabaseFactory()

        user = pm.query_user_by_id(self.userid)
        self.avatar.setImage(user[6])
        self.avatar.setRadius(20)

    def initLayout(self):
        self.vBoxLayout.addLayout(self.hBoxLayout, 5)
        self.hBoxLayout.addWidget(self.avatar, 0, Qt.AlignTop)
        self.hBoxLayout.addWidget(self.postEdit)
        self.vBoxLayout.addLayout(self.hBoxLayout2, 1)
        spacer = QSpacerItem(35, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.hBoxLayout2.addItem(spacer)
        # self.hBoxLayout2.addWidget(self.uploadImageButton, 0, Qt.AlignLeft)

        self.hBoxLayout2.addWidget(self.publishButton, 0, Qt.AlignRight)

    def publishPost(self):
        title = None
        swc = SensitiveWordChecker()
        result, found_words = swc.check_text(self.postEdit.toPlainText())
        if result:
            InfoBar.warning(
                title='Error',
                content="有敏感词，请修改你的文本.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0
        elif self.postEdit.toPlainText() == '':
            InfoBar.warning(
                title='Error',
                content="文本不能为空",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0
        w = PublishPostMessageBox(self.window())
        if w.exec():
            title = w.urlLineEdit.text()
        pm = PostManageDatabaseFactory()
        pm.add_new_post(self.userid, title, self.postEdit.toPlainText())
        InfoBar.success(
            title='Success',
            content="Publish successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.window()
        )
        self.window().chatInterface.allPostArea.myPostArea.showNewPost()
        self.window().chatInterface.myPostArea.myPostArea.showNewPost()


class Post(SimpleCardWidget):
    def __init__(self, parent=None, post=None):
        super().__init__(parent)
        # self.progressRing = IndeterminateProgressRing(self)
        # self.progressRing.setVisible(True)
        self.m = None
        self.isMessageShow = False
        self.messageNum = None
        self.likeNum = None
        self.post = post
        self.avatar = AvatarWidget(self)
        self.userNameLabel = CaptionLabel(self)
        self.contextLabel = CaptionLabel(self)
        self.titleLabel = TitleLabel(self)
        self.userNameLabel.setStyleSheet(
            "background-color : rgba(0, 0, 0, 0); font: 24px 'Segoe UI', 'Microsoft YaHei'; ")
        self.contextLabel.setStyleSheet("background-color : rgba(0, 0, 0, 0); ")
        self.titleLabel.setStyleSheet("background-color : rgba(0, 0, 0, 0); ")
        self.likeButton = TransparentPushButton(FIF.HEART, "2000w", self)
        self.likeButton.hide()
        self.messageButton = TransparentPushButton(FIF.MESSAGE, "2000w", self)
        self.moreButton = DropDownPushButton(FIF.MORE, 'More')

        if self.post[1] != self.parent().userid:
            self.moreButton.hide()

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.messageButton.clicked.connect(lambda: self.showMessage())

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout1 = QVBoxLayout()
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        self.initPost(post)
        self.initLayout()

    def initPost(self, post):
        if not post:
            self.close()
            return 0
        pm = PostManageDatabaseFactory()

        user = pm.query_user_by_id(post[1])
        self.avatar.setImage(user[6])
        self.avatar.setRadius(20)
        self.userNameLabel.setText(user[1])
        self.titleLabel.setText(post[2])
        self.contextLabel.setText(post[3])
        self.likeButton.setText(str(post[6]))
        self.messageButton.setText(str(post[7]))

    def initLayout(self):
        self.vBoxLayout.addLayout(self.hBoxLayout1)
        self.hBoxLayout1.addWidget(self.avatar)
        self.hBoxLayout1.addWidget(self.userNameLabel)
        self.hBoxLayout1.addWidget(self.moreButton, 0, Qt.AlignRight)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.contextLabel, 0, Qt.AlignLeft)
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        self.hBoxLayout2.addWidget(self.messageButton, 10, Qt.AlignRight)
        self.hBoxLayout2.addWidget(self.likeButton, 1, Qt.AlignRight)

        self.vBoxLayout.addWidget(self.separator, 0, Qt.AlignTop)
        self.vBoxLayout.addLayout(self.vBoxLayout1)
        self.menu = RoundMenu(parent=self.moreButton)

        del_action = Action(FIF.DELETE, 'Delete')
        del_action.triggered.connect(lambda: self.deletePost())
        edit_action = Action(FIF.EDIT, 'Edit')
        edit_action.triggered.connect(lambda: self.editPost())
        self.menu.addActions([
            del_action,
            edit_action
        ])

        self.moreButton.setMenu(self.menu)
        # self.vBoxLayout.addWidget(self.avatar)
        # self.vBoxLayout.addWidget(self.progressRing, 0, Qt.AlignCenter)
        pass

    def deletePost(self):
        pm = PostManageDatabaseFactory()
        pm.delete_post(self.post[0])
        self.setParent(None)
        self.deleteLater()
        InfoBar.success(
            title='Success',
            content="Delete successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self.window()
        )

    def editPost(self):
        m = EditPostMessageBox(self.window(), self.titleLabel.text(), self.contextLabel.text(), self.post[0])
        if m.exec():
            self.titleLabel.setText(m.urlLineEdit.text())
            self.contextLabel.setText(m.postEdit.toPlainText())

    def showMessage(self):
        pm = PostManageDatabaseFactory()
        comments = pm.query_comment_by_post_id(self.post[0])

        if self.isMessageShow:
            while self.vBoxLayout1.count():
                item = self.vBoxLayout1.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()  # 清空组件
            self.isMessageShow = False
        else:
            self.vBoxLayout1.addWidget(AddComment(self))
            if comments is not None:
                for comment in comments:
                    self.vBoxLayout1.addWidget(Comment(self, comment))
            self.isMessageShow = True
        pass


class PostArea(SingleDirectionScrollArea):
    def __init__(self, parent=None, userid=None, allPost=None):
        super().__init__(parent)
        self.allPost = allPost
        self.userid = userid
        self.posts = None

        self.view = QWidget(self)

        self.vBoxLayout = QVBoxLayout(self.view)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("appInterface")

        self.vBoxLayout.setSpacing(10)
        # self.vBoxLayout.setContentsMargins(0, 0, 10, 30)

        self.setStyleSheet("QScrollArea { background:rgb(242,242,242);border-radius: 8px;")
        self.view.setStyleSheet('QWidget {background:rgb(242,242,242)};border-radius: 8px;')

        self.initLayout()
        self.initPosts()

    def initLayout(self):
        pass

    def initPosts(self):
        pm = PostManageDatabaseFactory()
        if not self.allPost:
            self.posts = pm.query_post_by_id(self.userid)
        else:
            self.posts = pm.query_all_posts()
        self.post1 = AddPost(self, self.userid)
        self.vBoxLayout.addWidget(self.post1, 0, Qt.AlignTop)
        self.post1.setMaximumHeight(200)

        if self.posts is not None:
            for post in self.posts:
                self.vBoxLayout.addWidget(Post(self, post), 0, Qt.AlignTop)
            self.vBoxLayout.addStretch(1)

    def showNewPost(self):
        pm = PostManageDatabaseFactory()
        post = pm.query_all_posts()[-1]
        # 移除最后一个 stretch
        self.vBoxLayout.takeAt(self.vBoxLayout.count() - 1)

        # 插入新帖子到 post1 之后
        new_post_widget = Post(self, post)
        self.vBoxLayout.insertWidget(1, new_post_widget, 0, Qt.AlignTop)

        # 重新添加 stretch
        self.vBoxLayout.addStretch(1)


class PostWidget(QWidget):
    def __init__(self, parent=None, userid=None, allPost=None):
        super().__init__(parent=parent)
        self.myPostArea = PostArea(self, userid, allPost)
        # self.myPostArea.setMinimumHeight(400)
        self.myPostArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.HBoxLayer = QHBoxLayout(self)
        self.HBoxLayer.addStretch(1)
        self.HBoxLayer.addWidget(self.myPostArea, 5)
        self.HBoxLayer.addStretch(1)
        self.myPostArea.setMaximumWidth(600)


class ChatWidget(QWidget):

    def __init__(self, parent=None, userid=None):
        super().__init__(parent=parent)
        setTheme(Theme.LIGHT)
        self.setObjectName("ChatWidget")
        self.setStyleSheet("""
            Demo{background: white}
            QLabel{
                font: 20px 'Segoe UI';
                background: rgb(242,242,242);
                border-radius: 8px;
                color: black
            }
        """)
        self.resize(400, 400)

        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.allPostArea = PostWidget(self, userid, True)
        self.myPostArea = PostWidget(self, userid, False)

        # self.myPostArea.setMinimumHeight(1000)

        # add items to pivot
        self.addSubInterface(self.allPostArea, 'allPostInterface', 'All')
        self.addSubInterface(self.myPostArea, 'albumInterface', 'My Posts')

        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 0, 30, 30)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.allPostArea)
        self.pivot.setCurrentItem(self.allPostArea.objectName())

    def addSubInterface(self, widget, objectName, text):
        widget.setObjectName(objectName)
        # widget.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
