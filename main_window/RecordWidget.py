from collections import defaultdict

import PySide6
from PySide6.QtCharts import QChartView, QChart, QPieSeries
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QPainter
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame
from qfluentwidgets import SimpleCardWidget, SingleDirectionScrollArea, CaptionLabel, ToolButton, FluentIcon, \
    TransparentToolButton, InfoBarPosition, InfoBar, MessageBoxBase, SubtitleLabel, LineEdit, TextEdit

from main_window.PostManageDB import PostManageDatabaseFactory
from main_window.RecordManageDB import RecordManageDatabaseFactory
from main_window.SensitiveWordChecker import SensitiveWordChecker
from main_window.UserManageDB import UserManageDatabaseFactory


class shareMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None, record = None):
        super().__init__(parent)
        self.record = record
        self.titleLabel = SubtitleLabel('分享记录', self)
        self.urlLineEdit = LineEdit()
        self.postEdit = TextEdit()

        self.urlLineEdit.setPlaceholderText('输入标题')
        self.urlLineEdit.setClearButtonEnabled(True)

        calories_burned = record[5]
        total_seconds = record[7]
        total_minutes = total_seconds//60
        share_message = f"""Today, I completed an amazing workout!\n- Calories Burned: {calories_burned} kcal\n- Exercise Time: {total_seconds} seconds ({total_minutes} minutes)\nFeeling great and staying motivated! 💪
        """
        self.postEdit.setText(share_message)


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
        pm = PostManageDatabaseFactory()
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
        pm.add_new_post(self.record[1],self.urlLineEdit.text(),self.postEdit.toPlainText())
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
        self.accept()
        self.accepted.emit()

class SingleRecord(QWidget):
    def __init__(self, parent=None, userid=None, record=None):
        super().__init__(parent)
        self.userid = userid
        self.record = record

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.exerciseTypeSVG = QSvgWidget(self)
        self.exerciseTypeSVG.setFixedSize(40, 40)
        self.exerciseTypeLabel = CaptionLabel(self)
        self.datetimeLabel = CaptionLabel(self)
        self.kcalLabel = CaptionLabel(self)
        self.durationLabel = CaptionLabel(self)
        self.countLabel = CaptionLabel(self)
        self.delBtn = TransparentToolButton(FluentIcon.DELETE, self)
        self.shareBtn = TransparentToolButton(FluentIcon.SHARE, self)
        self.vBoxLayout = QVBoxLayout(self)
        self.cardBoxLayout = QHBoxLayout()
        self.vBoxLayout2 = QVBoxLayout()
        self.typeTimeLayout = QHBoxLayout()
        self.btnLayout = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        self.shareBtn.clicked.connect(lambda : self.share())

        self.initDetail()
        self.initLayout()
        self.delBtn.hide()

    def initLayout(self):
        self.vBoxLayout.addWidget(self.separator)
        self.vBoxLayout.addLayout(self.cardBoxLayout)
        self.cardBoxLayout.addLayout(self.cardBoxLayout)
        self.cardBoxLayout.addWidget(self.exerciseTypeSVG)
        self.cardBoxLayout.addLayout(self.vBoxLayout2)
        self.vBoxLayout2.addLayout(self.typeTimeLayout)
        self.typeTimeLayout.addWidget(self.exerciseTypeLabel)
        self.typeTimeLayout.addWidget(self.datetimeLabel)
        self.vBoxLayout2.addLayout(self.btnLayout)
        # self.btnLayout.addStretch(50)
        # self.btnLayout.addWidget(self.delBtn, 1, Qt.AlignRight)
        self.typeTimeLayout.addWidget(self.shareBtn, 1, Qt.AlignRight)
        self.vBoxLayout2.addLayout(self.hBoxLayout2)
        self.hBoxLayout2.addWidget(self.kcalLabel)
        self.hBoxLayout2.addWidget(self.durationLabel)
        self.hBoxLayout2.addWidget(self.countLabel)

    def initDetail(self):
        if self.record[2] == 1:
            self.exerciseTypeSVG.load("resource/icons/pushups-man-svgrepo-com.svg")
            self.exerciseTypeLabel.setText("Push-Up")
        elif self.record[2] == 2:
            self.exerciseTypeSVG.load("resource/icons/gym-workout-treadmill-icon.svg")
            self.exerciseTypeLabel.setText("Running")
        elif self.record[2] == 3:
            self.exerciseTypeSVG.load("resource/icons/pulling-up-training-silhouette-svgrepo-com.svg")
            self.exerciseTypeLabel.setText("Pull-up")
        self.datetimeLabel.setText(str(self.record[3]))
        self.kcalLabel.setText(str(self.record[5]) + ' kcal')
        self.kcalLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.countLabel.setText(str(self.record[4]) + ' times')
        self.countLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.durationLabel.setText(str(self.record[7]) + ' seconds')
        self.durationLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.exerciseTypeLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.datetimeLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        pass

    def share(self):
        m = shareMessageBox(self.window(),self.record)
        if m.exec():
            pass
        pass


class RecordByMonth(SimpleCardWidget):
    def __init__(self, parent=None, userid=None, month_record=None):
        super().__init__(parent)
        self.monthRecord = month_record
        self.userid = userid
        self.isShowDetail = False
        self.dateLabel = CaptionLabel(self)
        self.detailLabel = CaptionLabel(self)
        self.dateLabel.setStyleSheet("background: transparent;color: black;font-size: 13pt;")
        self.detailLabel.setStyleSheet("background: transparent;color: gray;font-size: 10pt;")
        self.showDetailBtn = ToolButton(FluentIcon.CARE_DOWN_SOLID, self)
        self.showDetailBtn.clicked.connect(self.showDetail)
        self.vBox0 = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout1 = QVBoxLayout()

        self.initLayout()
        self.initDetail()

    def initLayout(self):
        self.vBox0.addLayout(self.hBoxLayout)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.vBoxLayout.addWidget(self.dateLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.detailLabel, 0, Qt.AlignTop)
        self.hBoxLayout.addWidget(self.showDetailBtn, 0, Qt.AlignTop)
        self.vBox0.addLayout(self.vBoxLayout1)
        pass

    def initDetail(self):
        self.dateLabel.setText(self.monthRecord[0])
        self.detailLabel.setText("Count: " + str(self.monthRecord[3]) + " Time: " +
                                 self.secondsTohms(self.monthRecord[1]) + " Kcal: " + str(self.monthRecord[2]))
        self.detailLabel.setText(
            f"Count: {self.monthRecord[3]} Time: {self.secondsTohms(self.monthRecord[1])} Kcal: {self.monthRecord[2]:.2f}"
        )

        pass

    def secondsTohms(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m {seconds}s"

    def showDetail(self):
        if self.isShowDetail:
            self.isShowDetail = False
            self.showDetailBtn.setIcon(FluentIcon.CARE_DOWN_SOLID)
            while self.vBoxLayout1.count():
                item = self.vBoxLayout1.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
        else:
            self.isShowDetail = True
            self.showDetailBtn.setIcon(FluentIcon.CARE_UP_SOLID)
            rm = RecordManageDatabaseFactory()
            records = rm.query_record_by_user_id_and_month(self.userid, self.monthRecord[0])
            for record in records:
                self.vBoxLayout1.addWidget(SingleRecord(self, self.userid, record), 1, Qt.AlignTop)
            self.vBoxLayout1.addStretch(100)


class RecordArea(SingleDirectionScrollArea):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.userid = userid

        self.view = QWidget(self)

        self.vBoxLayout = QVBoxLayout(self.view)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("RecordArea")

        self.setStyleSheet("QScrollArea { background:rgb(242,242,242);border-radius: 8px;")
        self.view.setStyleSheet('QWidget {background:rgb(242,242,242)};border-radius: 8px;')

        self.initLayout()

    def initLayout(self):
        rm = RecordManageDatabaseFactory()
        records = rm.query_month_record_by_user(self.userid)
        if records:
            for record in records:
                self.vBoxLayout.addWidget(RecordByMonth(self, self.userid, record), 1, Qt.AlignTop)
            self.vBoxLayout.addStretch(10)
        pass


class RecordCard(SimpleCardWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.recordArea = RecordArea(self, userid)
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.recordArea)


class PieCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pieRecord = QPieSeries()
        self.pieRecord.setHoleSize(0.4)
        self.chart = QChart()
        self.chart.addSeries(self.pieRecord)
        self.chart.setTitle("Today's record")
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("background-color : rgba(0, 0, 0, 0);")

        self.suggestLabel = CaptionLabel(self)
        self.suggestLabel.setWordWrap(True)
        self.suggestLabel.setStyleSheet("background: transparent;")

        self.vBoxlayout = QVBoxLayout(self)
        self.hBoxlayout = QHBoxLayout()
        self.vBoxlayout1 = QVBoxLayout()

        self.initPieRecord()

    def initPieRecord(self):
        rm = RecordManageDatabaseFactory()
        records = rm.query_record_by_user_id_and_date(self.parent().userid, QDate.currentDate().toString(
            format=PySide6.QtCore.Qt.DateFormat.ISODate))
        # 使用defaultdict来存储每种类型的总卡路里
        record_summary = defaultdict(float)

        if records:
            for record in records:
                record_summary[record[10]] += record[5]

            for record_type, total_calories in record_summary.items():
                self.pieRecord.append(f"{record_type}  {total_calories:.2f}kcal", total_calories)
        else:
            self.pieRecord.append("There has no record today.", 1)

        self.vBoxlayout.addWidget(self.chart_view,5)
        self.vBoxlayout.addWidget(self.suggestLabel,4)

        rm = RecordManageDatabaseFactory()
        records = rm.query_month_record_by_user(self.parent().userid)
        if records:
            latest_record = records[0]
            month = latest_record[0]
            total_seconds = latest_record[1]
            total_calories_burned = latest_record[2]
            count = latest_record[3]

            # Provide suggestions based on the record (this is a simple example, adjust as needed)
            if total_seconds < 3600:
                suggestion = f"  Recently, you only exercised for {total_seconds // 60} minutes. It is recommended to increase your exercise time."
            elif total_seconds > 18000:  # Example threshold: 5 hours
                suggestion = f"  Recently, you exercised for {total_seconds // 3600:.1f} hours. It's important to balance exercise with rest to avoid overtraining."
            elif total_calories_burned < 2000:
                suggestion = f"  Recently, you burned {total_calories_burned} calories. It is recommended to increase your exercise intensity."
            else:
                suggestion = f"  Recently, you exercised for {total_seconds // 60} minutes and burned {total_calories_burned} calories. Keep up the good work!"

            self.suggestLabel.setText(suggestion)
        else:
            self.suggestLabel.setText(
                "No exercise records found for the last month. It's a good time to start exercising!")




class RecordWidget(QWidget):
    def __init__(self, parent=None, userid=None):
        super().__init__(parent)
        self.setObjectName("RecordWidget")
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
        self.pieCard.setMaximumWidth(400)

        self.recordCard = RecordCard(self, self.userid)

        self.Hlayout.addStretch(1)
        self.Hlayout.addWidget(self.pieCard, 5)
        self.Hlayout.addWidget(self.recordCard, 5)
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

