from collections import defaultdict

import PySide6
from PySide6.QtCharts import QPieSeries, QChart, QChartView
from PySide6.QtCore import QDate
from PySide6.QtGui import Qt, QPainter, QFont
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from qfluentwidgets import PrimaryPushButton, SimpleCardWidget, SingleDirectionScrollArea, CaptionLabel, \
    TransparentToolButton, FluentIcon, TitleLabel, ImageLabel, ComboBox, PushButton, MessageBoxBase, SubtitleLabel, \
    LineEdit, TimePicker, CompactTimeEdit, TimeEdit, InfoBar, InfoBarPosition

from PullUp import PullUpVideoPlayer
from main_window.PlanManageDB import PlanManageDatabaseFactory
from main_window.RecordManageDB import RecordManageDatabaseFactory
from pushup import PushUpVideoPlayer
from walk import VideoPlayer


class AddTaskMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('New Task', self)
        self.caloriesLineEdit = LineEdit()

        self.caloriesLineEdit.setPlaceholderText('Planned calorie intake')
        self.caloriesLineEdit.setClearButtonEnabled(True)
        self.timeLabel = CaptionLabel("Duration:", self)

        self.timePicker = TimeEdit(self)
        # self.timePicker.setColumnVisible(0, False)  # 隐藏小时
        # self.timePicker.setColumnVisible(1, True)  # 隐藏分钟
        # self.timePicker.setColumnVisible(2, True)  # 显示秒

        self.exerciseType = ComboBox(self)
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


class Task(SimpleCardWidget):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.task = task
        self.dateLabel = CaptionLabel(self)
        self.kcalLabel = CaptionLabel(self)
        self.exerciseTypeLabel = CaptionLabel(self)

        self.dateLabel.setStyleSheet("QLabel{background: transparent;color: gray;font-size: 10pt;}")
        self.kcalLabel.setStyleSheet("QLabel{background: transparent;color: gray;font-size: 10pt;}")
        self.completeLabel = CaptionLabel("incomplete", self)
        if task[6] == 1:
            self.completeLabel.setText("finished")
        self.completeLabel.setStyleSheet("background: transparent;color: gray;font-size: 8pt;")
        self.exerciseTypeLabel.setStyleSheet("QLabel{background: transparent;}")

        self.deleteButton = TransparentToolButton(FluentIcon.DELETE)
        self.deleteButton.hide()
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
        self.hBoxLayout.addWidget(self.completeLabel, 1, Qt.AlignTop)
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


class TaskArea(SingleDirectionScrollArea):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)

        self.userid = userid

        self.view = QWidget(self)

        # self.post1 = Task(self)

        self.vBoxLayout = QVBoxLayout(self.view)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("taskarea22")

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
                self.vBoxLayout.addWidget(Task(self.view, task), 1, Qt.AlignTop)

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


class PlanCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.w = None
        self.titleLabel = TitleLabel("Select exercise-type", self)
        self.titleLabel.setStyleSheet("background-color : rgba(0, 0, 0, 0);")
        # self.exerciseTypeSVG = ImageLabel("resource/icons/gym-workout-treadmill-icon.svg", self)
        self.exerciseTypeSVG = QSvgWidget("resource/icons/gym-workout-treadmill-icon.svg")
        self.exerciseTypeSVG.setFixedSize(260, 260)
        self.comboBox = ComboBox()

        items = ['Running', 'PushUp', 'PullUp']

        for item in items:
            self.comboBox.addItem(item)
        self.comboBox.setFixedSize(180, 30)
        self.goBtn = PrimaryPushButton("go", self)
        self.goBtn.setFixedSize(180, 80)
        font = QFont()
        font.setPointSize(20)  # Set the desired font size
        self.goBtn.setFont(font)

        self.goBtn.clicked.connect(self.justDoIt)

        self.comboBox.currentIndexChanged.connect(self.onComboBoxChanged)

        self.vBoxLayout = QVBoxLayout(self)

        self.initLayout()

    def initLayout(self):
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.exerciseTypeSVG, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.comboBox, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.goBtn, 0, Qt.AlignCenter)

    def justDoIt(self):
        if self.comboBox.text() == 'Running':
            self.w = VideoPlayer(self)
            self.w.show()
        elif self.comboBox.text() == 'PushUp':
            self.w = PushUpVideoPlayer(self)
            self.w.show()
        elif self.comboBox.text() == 'PullUp':
            self.w = PullUpVideoPlayer(self)
            self.w.show()

    def onComboBoxChanged(self, index):
        # Define the paths to the SVG files
        svg_paths = {
            'Running': "resource/icons/gym-workout-treadmill-icon.svg",
            'PushUp': "resource\icons\pushups-man-svgrepo-com.svg",
            'PullUp': "resource/icons/pulling-up-training-silhouette-svgrepo-com.svg"
        }

        # Get the selected item text
        selected_item = self.comboBox.currentText()

        # Update the SVG widget with the new file
        if selected_item in svg_paths:
            self.exerciseTypeSVG.load(svg_paths[selected_item])

    def show_and_add_record(self, userid, exercise_type, action_count, calories_burned, total_seconds):
        rm = RecordManageDatabaseFactory()
        rm.add_record(userid, exercise_type, action_count, calories_burned, total_seconds)
        InfoBar.success(
            title='Success',
            content="Upload successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=5000,
            parent=self.window()
        )
        self.window().recordInterface.update_widget()
        self.parent().update_widget()


class PieCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.pieRecord = QPieSeries()
        self.pieRecord.setHoleSize(0.4)
        self.chart = QChart()
        self.chart.addSeries(self.pieRecord)
        self.chart.setTitle("Today's record")
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("background-color : rgba(0, 0, 0, 0);")

        self.taskArea = TaskArea(self, self.parent().userid)
        self.taskLabel = TitleLabel("Today's tasks", self)
        self.taskLabel.setStyleSheet("background-color : rgba(0, 0, 0, 0);")
        self.addTaskBtn = PushButton('Go to plan widget', self)
        self.addTaskBtn.clicked.connect(lambda: self.window().switchTo(self.window().planInterface))

        self.vBoxlayout = QVBoxLayout(self)
        self.hBoxlayout = QHBoxLayout()
        self.vBoxlayout1 = QVBoxLayout()

        self.initPieRecord()

        self.setLayout(self.vBoxlayout)

    def initPieRecord(self):
        rm = RecordManageDatabaseFactory()
        records = rm.query_record_by_user_id_and_date(
            self.parent().userid,
            QDate.currentDate().toString(format=Qt.ISODate)
        )

        # 使用 defaultdict 来存储每种类型的总卡路里
        record_summary = defaultdict(float)

        # 清除之前的饼图数据
        self.pieRecord.clear()

        if records:
            for record in records:
                record_summary[record[10]] += record[5]

            for record_type, total_calories in record_summary.items():
                self.pieRecord.append(f"{record_type}  {total_calories:.2f}kcal", total_calories)
        else:
            self.pieRecord.append("There has no record today.", 1)

        self.vBoxlayout.addWidget(self.chart_view)
        self.vBoxlayout.addWidget(self.taskLabel, 0, Qt.AlignCenter)
        self.vBoxlayout.addLayout(self.hBoxlayout)
        self.hBoxlayout.addStretch(1)
        self.hBoxlayout.addLayout(self.vBoxlayout1, 5)
        self.vBoxlayout1.addWidget(self.taskArea)
        self.vBoxlayout1.addWidget(self.addTaskBtn)
        self.hBoxlayout.addStretch(1)

    def clear_layout(self, layout):
        """清空布局中的所有组件"""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def update_widget(self):
        """重新组织窗口"""
        # 清空当前布局
        self.clear_layout(self.vBoxlayout)
        # self.clear_layout(self.hBoxlayout)
        # self.clear_layout(self.vBoxlayout1)

        # 重新初始化布局和组件
        self.initUI()
        self.update()

    def showMessage(self):
        w = AddTaskMessageBox(self.window())
        if w.exec():
            print(w.caloriesLineEdit.text())


class ExerciseWidget(QWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.setObjectName("exerciseWidget")
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
        self.setup_layout()

        self.setLayout(self.Hlayout)

    def setup_layout(self):
        """设置布局和添加组件"""
        self.pieCard = PieCard(self)
        self.planCard = PlanCard(self)
        self.planCard.setMaximumWidth(310)
        self.pieCard.setMaximumWidth(400)

        self.Hlayout.addStretch(1)
        self.Hlayout.addWidget(self.pieCard, 5)
        self.Hlayout.addWidget(self.planCard, 5)
        self.Hlayout.addStretch(1)

    def clear_layout(self):
        """清空布局中的所有组件"""
        while self.Hlayout.count():
            item = self.Hlayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def update_widget(self):
        """重新组织窗口"""
        # 清空当前布局
        self.clear_layout()
        # 重新设置布局和添加组件
        self.setup_layout()
        # 强制更新窗口
        self.update()
