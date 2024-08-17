from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, \
    QHBoxLayout, QFrame
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QFont
from qfluentwidgets import FluentWindow, SimpleCardWidget, TitleLabel, CaptionLabel, BodyLabel
from ultralytics import YOLO
import cv2
import sys
import time

from main_window.PlanManageDB import PlanManageDatabaseFactory
from main_window.the_gym import TheGym


class StyledSeparator(QFrame):
    def __init__(self, color="gray", height=0.1, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet(f"background-color: {color}; height: {height}px;")


class PanelCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("微软雅黑", 16)
        self.titleLabel = BodyLabel("Workout Details", self)
        self.titleLabel.setFont(font)
        self.countLabel = BodyLabel("Count: 0", self)
        self.countLabel.setFont(font)
        self.BurnedCLabel = BodyLabel("Calories Burned: 0", self)
        self.BurnedCLabel.setFont(font)
        self.timeLabel = BodyLabel("Time: 0m,0s", self)
        self.timeLabel.setFont(font)
        self.vBoxLayout = QVBoxLayout(self)

        self.separator = StyledSeparator()
        self.separator1 = StyledSeparator()
        self.separator2 = StyledSeparator()
        self.separator3 = StyledSeparator()
        self.separator4 = StyledSeparator()

        self.initLayout()

    def initLayout(self):
        # self.vBoxLayout.addWidget(self.separator)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.separator1)
        self.vBoxLayout.addWidget(self.countLabel)
        self.vBoxLayout.addWidget(self.separator2)
        self.vBoxLayout.addWidget(self.BurnedCLabel)
        self.vBoxLayout.addWidget(self.separator3)
        self.vBoxLayout.addWidget(self.timeLabel)
        # self.vBoxLayout.addWidget(self.separator4)


class PullUpVideoPlayer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QMainWindow{background: Gray}")
        self.gym_object = TheGym()
        self.setWindowTitle("Video Player with YOLO and AI Gym")
        self.setGeometry(100, 100, 800, 600)

        # Create UI elements
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumSize(400, 590)
        self.play_button = QPushButton("Play", self)
        self.pause_button = QPushButton("Pause", self)
        self.fps_label = QLabel("FPS: 0", self)
        self.fps_label.hide()
        self.open_button = QPushButton("Open Video", self)
        self.open_camera_button = QPushButton("Open Camera", self)
        self.exit_button = QPushButton("Exit", self)
        self.plan_card = PanelCard(self)

        # Set up layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.video_label)

        panel_layout = QVBoxLayout()

        button_layout1 = QHBoxLayout()
        button_layout2 = QHBoxLayout()

        main_layout.addLayout(panel_layout)
        panel_layout.addWidget(self.plan_card)

        panel_layout.addLayout(button_layout1)
        button_layout1.addWidget(self.open_button)
        button_layout1.addWidget(self.open_camera_button)

        panel_layout.addLayout(button_layout2)
        button_layout2.addWidget(self.play_button)
        button_layout2.addWidget(self.pause_button)

        panel_layout.addWidget(self.exit_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Connect buttons to functions
        self.play_button.clicked.connect(self.play_video)
        self.pause_button.clicked.connect(self.pause_video)
        self.open_button.clicked.connect(self.open_video)
        self.open_camera_button.clicked.connect(self.open_camera)
        self.exit_button.clicked.connect(self.close)

        # Initialize variables
        self.cap = None
        self.model = None
        self.timer = QTimer(self)
        self.frame_count = 0
        self.is_paused = False
        self.start_time = time.time()

        # Set up timer for video playback
        self.timer.timeout.connect(self.update_frame)
        self.timer.setInterval(int(1000 / 20))  # 30 FPS

        self.timer2 = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_timer)
        self.elapsed_time = 0  # Time in seconds

    def update_timer(self):
        self.elapsed_time += 1
        minutes = self.elapsed_time // 60
        seconds = self.elapsed_time % 60
        self.plan_card.timeLabel.setText(f"Time: {minutes}m,{seconds}s")

    def open_camera(self):
        del self.model
        del self.cap
        self.frame_count = 0
        if not self.is_paused:
            self.timer.stop()
        self.cap = cv2.VideoCapture(0)
        assert self.cap.isOpened(), "Error reading camera feed"
        self.model = YOLO("yolov8n-pose.pt")
        self.gym_object = TheGym()
        self.gym_object.set_args(line_thickness=2, view_img=False, pose_type="pullup", kpts_to_check=[6, 8, 10],
                                 pose_down_angle=117)
        self.frame_count = 0
        self.is_paused = False
        self.start_time = time.time()
        self.update_frame()
        self.timer.start()

    def open_video(self):
        # Open file dialog to select video file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        del self.model
        del self.cap
        self.frame_count = 0
        if file_name:
            self.cap = cv2.VideoCapture(file_name)
            assert self.cap.isOpened(), "Error reading video file"
            self.model = YOLO("yolov8n-pose.pt")
            self.gym_object = TheGym()
            self.gym_object.set_args(line_thickness=2, view_img=False, pose_type="pullup", kpts_to_check=[6, 8, 10],
                                     pose_down_angle=117)
            self.frame_count = 0
            self.is_paused = False
            self.start_time = time.time()
            self.update_frame()
            self.is_paused = True

    def play_video(self):
        self.is_paused = False
        self.timer.start()
        self.timer2.start(1000)  # Update every 1000 milliseconds (1 second)

    def pause_video(self):
        self.is_paused = True
        self.timer.stop()
        self.timer2.stop()

    def update_frame(self):
        if not self.is_paused and self.cap is not None and self.cap.isOpened():
            success, im0 = self.cap.read()
            if not success:
                self.pause_video()
                return

            self.frame_count += 1
            results = self.model.track(im0, verbose=False)
            im0 = self.gym_object.start_counting(im0, results, self.frame_count)
            im0 = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)

            height, width, channel = im0.shape
            bytes_per_line = 3 * width
            q_img = QImage(im0.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            pixmap = pixmap.scaled(400, 590, Qt.KeepAspectRatio)  # 按比例缩放到合适的大小
            self.video_label.setPixmap(pixmap)

            # Calculate and display FPS
            elapsed_time = time.time() - self.start_time
            fps = self.frame_count / elapsed_time
            self.fps_label.setText(f"FPS: {fps:.2f}")

            self.plan_card.countLabel.setText("Count: " + str(self.gym_object.count[0]))
            self.plan_card.BurnedCLabel.setText(
                "Calories Burned: {:.1f}".format(self.gym_object.count[0] * 1.04) + " kcal")
        else:
            self.pause_video()

    def closeEvent(self, event):
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()
        super().closeEvent(event)
        if self.elapsed_time != 0:
            self.parent().show_and_add_record(self.parent().parent().userid, 3, self.gym_object.count[0], self.gym_object.count[0] * 1.04, self.elapsed_time)
        pm = PlanManageDatabaseFactory()
        pm.complete_task(self.parent().parent().userid, 3)
        # self.window().appInterface.update_widget()


