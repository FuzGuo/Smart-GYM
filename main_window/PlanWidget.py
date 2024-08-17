import PySide6
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QColor, QIntValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QGridLayout
from qfluentwidgets import AvatarWidget, SimpleCardWidget, PushButton, LineEdit, ComboBox, SpinBox, PrimaryPushButton, \
    CaptionLabel, CalendarPicker, SingleDirectionScrollArea, FluentIcon, TransparentToolButton, MessageBoxBase, \
    SubtitleLabel, TimeEdit, InfoBar, InfoBarPosition
from qfluentwidgets.components.date_time.calendar_view import CalendarView

from main_window.PlanManageDB import PlanManageDatabaseFactory


class MyC(CalendarView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def __initWidget(self):
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint |
                            Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.stackedWidget.addWidget(self.dayView)
        self.stackedWidget.addWidget(self.monthView)
        self.stackedWidget.addWidget(self.yearView)

        self.hBoxLayout.setContentsMargins(12, 8, 12, 20)
        self.hBoxLayout.addWidget(self.stackedWidget)
        self.setShadowEffect()

        self.dayView.setDate(QDate.currentDate())

        self.aniGroup.addAnimation(self.opacityAni)
        self.aniGroup.addAnimation(self.slideAni)

        self.dayView.titleClicked.connect(self._onDayViewTitleClicked)
        self.monthView.titleClicked.connect(self._onMonthTitleClicked)

        self.monthView.itemClicked.connect(self._onMonthItemClicked)
        self.yearView.itemClicked.connect(self._onYearItemClicked)
        self.dayView.itemClicked.connect(self._onDayItemClicked)

    def _onDayItemClicked(self, date: QDate):
        # self.close()
        if date != self.date:
            self.date = date
            self.dateChanged.emit(date)
            self.dayView.setDate(date)
            self.parent().taskArea.clear_layout()
            self.parent().taskArea.initTasks(date)


class Task(SimpleCardWidget):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.task = task
        self.dateLabel = CaptionLabel(self)
        self.kcalLabel = CaptionLabel(self)
        self.exerciseTypeLabel = CaptionLabel(self)
        self.completeLabel = CaptionLabel("incomplete", self)
        if task[6] == 1:
            self.completeLabel.setText("finished")
        self.completeLabel.setStyleSheet("background: transparent;color: gray;font-size: 8pt;")

        self.dateLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.kcalLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.exerciseTypeLabel.setStyleSheet("background: transparent;")

        self.deleteButton = TransparentToolButton(FluentIcon.DELETE)
        self.deleteButton.clicked.connect(lambda: self.delete_task())
        self.vBoxLayout = QVBoxLayout(self)

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout1 = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        self.initLayout()
        self.initTask()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.dateLabel)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.dateLabel, 1, Qt.AlignTop)
        self.hBoxLayout.addWidget(self.completeLabel,1, Qt.AlignTop)
        self.hBoxLayout.addWidget(self.deleteButton, 10, Qt.AlignTop)

        self.vBoxLayout.addLayout(self.hBoxLayout1)
        self.hBoxLayout1.addWidget(self.exerciseTypeLabel, 1, Qt.AlignTop)
        self.hBoxLayout1.addWidget(self.kcalLabel, 1, Qt.AlignRight)
        pass
        # self.vBoxLayout.addWidget(self.calendar)

    def initTask(self):
        if self.task is not None:
            self.dateLabel.setText(self.task[5].strftime("%Y-%m-%d"))
            self.exerciseTypeLabel.setText(self.task[9])
            self.kcalLabel.setText(str(self.task[3]) + "kcal")
        pass

    def delete_task(self):
        # self.window().appInterface.update_widget()
        pm = PlanManageDatabaseFactory()
        pm.del_tasks(self.task[0])
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
        self.setParent(None)
        self.deleteLater()


class TaskArea(SingleDirectionScrollArea):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.date = None
        self.userid = userid

        self.view = QWidget(self)

        # self.post1 = Task(self)

        self.vBoxLayout = QVBoxLayout(self.view)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("taskarea")

        # self.vBoxLayout.setSpacing(10)
        # self.vBoxLayout.setContentsMargins(0, 0, 10, 30)

        self.setStyleSheet("QScrollArea { background:rgb(242,242,242);border-radius: 8px;")
        self.view.setStyleSheet('QWidget {background:rgb(242,242,242)};border-radius: 8px;')

        self.initLayout()
        self.initTasks()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.post1, 0, Qt.AlignTop)
        pass

    def initTasks(self, date=QDate.currentDate()):
        self.date = date
        while self.vBoxLayout.count():
            item = self.vBoxLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()
        pm = PlanManageDatabaseFactory()
        self.tasks = pm.query_tasks_by_user_id_and_date(self.userid,
                                                        date.toString(format=PySide6.QtCore.Qt.DateFormat.ISODate))
        if self.tasks is not None:
            for task in self.tasks:
                self.vBoxLayout.addWidget(Task(self, task), 1, Qt.AlignTop)

            self.vBoxLayout.addStretch(100)

        else:
            pass
        pass

    def clear_layout(self):
        while self.vBoxLayout.count():
            item = self.vBoxLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

    def add_task(self):
        pm = PlanManageDatabaseFactory()
        if pm.query_plan_by_user_id(self.userid) is None:
            pm.add_new_plan(self.userid)
        plan = pm.query_plan_by_user_id(self.userid)[0]
        m = AddTaskMessageBox(self.window(), self.userid, plan[0], self.date)
        if m.exec():
            self.initTasks(self.date)
            self.window().appInterface.update_widget()


def hhmm_to_seconds(time_str):
    """将 hh:mm 格式的字符串转换为总秒数"""
    # 拆分字符串，提取小时和分钟
    hh, mm = map(int, time_str.split(':'))

    # 计算总秒数
    total_seconds = hh * 3600 + mm * 60

    return total_seconds


class AddTaskMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None, userid=None, plan_id=None, date=None):
        super().__init__(parent)
        self.userid = userid
        self.plan_id = plan_id
        self.date = date
        self.titleLabel = SubtitleLabel('New Task', self)
        self.caloriesLineEdit = LineEdit()
        int_validator = QIntValidator(1, 10000)  # 设置一个合理的范围
        self.caloriesLineEdit.setValidator(int_validator)

        self.caloriesLineEdit.setPlaceholderText('Planned calorie intake')
        self.caloriesLineEdit.setClearButtonEnabled(True)
        self.timeLabel = CaptionLabel("Duration:", self)

        self.timePicker = TimeEdit(self)
        # self.timePicker.setColumnVisible(0, False)  # 隐藏小时
        # self.timePicker.setColumnVisible(1, True)  # 隐藏分钟
        # self.timePicker.setColumnVisible(2, True)  # 显示秒

        self.exerciseType = ComboBox(self)
        items = ['Running', 'PushUp', 'PullUp']
        for item in items:
            self.exerciseType.addItem(item)
        self.hBoxLayout = QHBoxLayout()

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.caloriesLineEdit)
        self.viewLayout.addLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.timeLabel, 3)
        self.hBoxLayout.addWidget(self.timePicker, 5)
        self.viewLayout.addWidget(self.exerciseType)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(300)
        # 重新指向
        self.yesButton.clicked.disconnect()
        self.yesButton.clicked.connect(lambda: self.__onYesButtonClicked())

    def __onYesButtonClicked(self):
        if self.caloriesLineEdit.text() == '' or int(self.caloriesLineEdit.text()) < 1:
            InfoBar.warning(
                title='Error',
                content="Invalid Input.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0

        pm = PlanManageDatabaseFactory()
        if self.exerciseType.text() == 'Running':
            self.exercise_id = 2
        elif self.exerciseType.text() == 'PushUp':
            self.exercise_id = 1
        elif self.exerciseType.text() == 'PullUp':
            self.exercise_id = 3
        if hhmm_to_seconds(self.timePicker.text()) == 0:
            InfoBar.warning(
                title='Error',
                content="Invalid Input.",
                orient=Qt.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self.window()
            )
            return 0
        pm.add_new_task(self.userid, self.date, self.plan_id, int(self.caloriesLineEdit.text()),
                        hhmm_to_seconds(self.timePicker.text()), self.exercise_id)
        self.accept()
        self.accepted.emit()


class CalendarCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(700)
        self.calendar = MyC(self.parent())
        self.taskWidget = QWidget(self)
        self.taskLayout = QVBoxLayout(self.taskWidget)
        self.taskWidget.setFixedWidth(220)
        self.taskArea = TaskArea(self.taskWidget, self.parent().userid)

        self.taskLayout.addWidget(self.taskArea)
        # self.calendar.setEnabled(False)
        self.clearbtn = PrimaryPushButton('Add', self)
        self.reloadbtn = PrimaryPushButton("Today's task", self)

        self.clearbtn.clicked.connect(lambda: self.taskArea.add_task())
        self.reloadbtn.clicked.connect(lambda: self.taskArea.initTasks())

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout1 = QVBoxLayout()

        self.initLayout()

    def initLayout(self):
        self.hBoxLayout.addWidget(self.calendar, 5, Qt.AlignRight)
        self.hBoxLayout.addLayout(self.vBoxLayout1, 5)
        self.vBoxLayout1.addWidget(self.taskWidget)

        self.vBoxLayout1.addWidget(self.clearbtn)
        self.vBoxLayout1.addWidget(self.reloadbtn)
        self.hBoxLayout.addStretch(2)


class PlanCaptionCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.remindlabel = None
        self.vBoxLayout = QVBoxLayout(self)

        self.initLayout()
        self.initPlan()

    def initLayout(self):
        pass
        # self.vBoxLayout.addWidget(self.calendar)

    def initPlan(self):
        pm = PlanManageDatabaseFactory()
        plan = pm.query_plan_by_user_id(self.parent().userid)

        if plan is None:
            self.remindlabel = CaptionLabel("Sorry, you do not have a plan set up.", self)
            self.remindlabel.setStyleSheet("background-color : rgba(0, 0, 0, 0); ")
            self.vBoxLayout.addWidget(self.remindlabel)
            pass
        else:
            pass


class PlanWidget(QWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.setObjectName("planWidget")
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
        # 设置布局
        # self.view = QWidget(self)
        self.Hlayout = QHBoxLayout(self)
        self.Vlayout = QVBoxLayout()
        # self.Glayout = QGridLayout(self)

        self.calendarCard = CalendarCard(self)
        self.plancaption = PlanCaptionCard(self)

        # self.avatar = AvatarWidget('resource/avatar1.jpg')
        # self.avatar.setRadius(64)

        # self.avatar.setAlignment(Qt.AlignCenter)

        self.Hlayout.addStretch(1)
        self.Hlayout.addLayout(self.Vlayout, 5)
        self.Hlayout.addStretch(1)

        # self.avatar.setMinimumHeight(64)  # 设置最小宽度
        # self.avatar.setMaximumHeight(64)  # 设置最大宽度，与最小宽度相同，固定宽度为200像素
        self.Vlayout.addWidget(self.calendarCard, 2, alignment=Qt.AlignTop)
        self.Vlayout.addWidget(self.plancaption, 2, alignment=Qt.AlignTop)


        self.setLayout(self.Vlayout)
