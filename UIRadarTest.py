from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import sys
import pyqtgraph as pg


class RadarTestMain(QMainWindow):
    def __init__(self):
        super(RadarTestMain, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle("毫米波雷达测试系统")
        self.setFont(QFont('Menlo', 12))
        self.menu_init()
        # self.tool_menu_init()
        self.tab_menu()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def menu_init(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件")
        mission_menu = menubar.addMenu("任务")
        view_menu = menubar.addMenu("视图")
        config_menu = menubar.addMenu("配置")
        analysis_menu = menubar.addMenu("分析")
        self_test_menu = menubar.addMenu("自检")
        tool_menu = menubar.addMenu("工具")
        help_menu = menubar.addMenu("帮助")
        # 文件菜单
        open_act = QAction("打开", self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.open_file)
        file_menu.addAction(open_act)
        save_act = QAction("保存", self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.save_file)
        file_menu.addAction(save_act)
        exit_act = QAction("退出", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)
        # 任务菜单
        new_mission_act = QAction('新建', self)
        mission_menu.addAction(new_mission_act)
        edit_mission_act = QAction('修改', self)
        mission_menu.addAction(edit_mission_act)
        # 工具菜单
        com_act = QAction("串口调试", self)
        # com_act.triggered.connect()
        tool_menu.addAction(com_act)
        net_act = QAction("网口调试", self)
        # net_act.triggered.connect()
        tool_menu.addAction(net_act)

    def open_file(self):
        QFileDialog.getOpenFileName(self, '打开文件', '/home')

    def save_file(self):
        QFileDialog.getSaveFileName(self, '保存文件', '/home')

    def tool_menu_init(self):
        exit_act = QAction("退出", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(qApp.quit)
        exit_act.setToolTip("退出应用")

        self.toolbar = self.addToolBar("exit")
        self.toolbar.addAction(exit_act)

    def tab_menu(self):
        self.central_widget = QWidget(self)
        self.tabWidget = QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(0, 0, self.width(), self.height()-50)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab1, "射频性能测试")
        self.tabWidget.addTab(self.tab2, "探测性能测试")
        self.tabWidget.addTab(self.tab3, "天线性能测试")
        self.setCentralWidget(self.central_widget)
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

    def tab1_ui(self):
        self.off_button = QRadioButton('off', self)
        self.on_button = QRadioButton('on', self)
        self.pic_label = QLabel(self)

        self.name_label = QLabel('姓名')
        self.department_label = QLabel('部门')
        self.post_label = QLabel('岗位')
        self.name_edit = QLineEdit()
        self.department_edit = QLineEdit()
        self.post_edit = QLineEdit()

        self.time_label = QLabel('时间')
        self.job_classify_label = QLabel('工作分类')
        self.man_hour_label = QLabel('工时')
        self.nature_label = QLabel('性质')
        self.important_urgency_label = QLabel('重要/紧急')
        self.status_label = QLabel('状态')
        self.work_cop_label = QLabel('工作配合')
        self.time_data_edit = QDateEdit()
        self.time_data_edit.setCalendarPopup(True)
        self.time_data_edit.setDate(QtCore.QDate(2020, 1, 1))
        self.job_classify_combo = QComboBox()
        self.man_hour_combo = QComboBox()
        self.nature_combo = QComboBox()
        self.important_urgency_combo = QComboBox()
        self.status_combo = QComboBox()
        self.work_cop_combo = QComboBox()

        self.content_label = QLabel('工作配合')
        self.question_label = QLabel('问题及意见')
        self.content_edit = QTextEdit()
        self.question_edit = QTextEdit()

        self.save_button = QPushButton('保存', self)
        self.change_button = QPushButton('修改', self)
        self.delete_button = QPushButton('删除', self)
        self.submit_button = QPushButton('提交', self)
        self.query_button = QPushButton('查询', self)
        self.config_button = QPushButton('配置', self)

        self.message_table = QTableWidget()
        self.message_table.setHorizontalHeaderLabels(['时间', '工作分类', '事项内容', '工时', '性质', '重要/紧急', '状态', '工作配合', '问题和困难', 'ID'])

        self.tab1_layout_init()
        self.radiobutton_init()
        self.label_init()

    def tab1_layout_init(self):
        self.up_h_layout = QHBoxLayout()
        self.up_h_layout.addWidget(self.name_label)
        self.up_h_layout.addWidget(self.name_edit)
        self.up_h_layout.addWidget(self.department_label)
        self.up_h_layout.addWidget(self.department_edit)
        self.up_h_layout.addWidget(self.post_label)
        self.up_h_layout.addWidget(self.post_edit)
        self.up_h_layout.addStretch(3)
        self.up_h_layout.setStretch(3, 1)

        self.l_grid_layout = QGridLayout()
        self.l_grid_layout.addWidget(self.time_label, 0, 0, 1, 1)
        self.l_grid_layout.addWidget(self.time_data_edit, 0, 1, 1, 1)
        self.l_grid_layout.addWidget(self.job_classify_label, 1, 0, 1, 1)
        self.l_grid_layout.addWidget(self.job_classify_combo, 1, 1, 1, 1)
        self.l_grid_layout.addWidget(self.man_hour_label, 2, 0, 1, 1)
        self.l_grid_layout.addWidget(self.man_hour_combo, 2, 1, 1, 1)
        self.l_grid_layout.addWidget(self.nature_label, 3, 0, 1, 1)
        self.l_grid_layout.addWidget(self.nature_combo, 3, 1, 1, 1)
        self.l_grid_layout.addWidget(self.important_urgency_label, 4, 0, 1, 1)
        self.l_grid_layout.addWidget(self.important_urgency_combo, 4, 1, 1, 1)
        self.l_grid_layout.addWidget(self.status_label, 5, 0, 1, 1)
        self.l_grid_layout.addWidget(self.status_combo, 5, 1, 1, 1)
        self.l_grid_layout.addWidget(self.work_cop_label, 6, 0, 1, 1)
        self.l_grid_layout.addWidget(self.work_cop_combo, 6, 1, 1, 1)
        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.pic_h_layout.addStretch(2)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.l_grid_layout.addLayout(self.pic_h_layout, 7, 0, 1, 2)
        self.l_grid_layout.addLayout(self.button_h_layout, 8, 0, 1, 2)

        self.m_grid_layout = QGridLayout()
        self.m_grid_layout.addWidget(self.content_label, 0, 0, 1, 1)
        self.m_grid_layout.addWidget(self.content_edit, 0, 1, 5, 50)
        self.m_grid_layout.addWidget(self.question_label, 5, 0, 1, 1)
        self.m_grid_layout.addWidget(self.question_edit, 5, 1, 5, 50)

        self.r_v_layout = QVBoxLayout()
        self.r_v_layout.addWidget(self.save_button)
        self.r_v_layout.addWidget(self.change_button)
        self.r_v_layout.addWidget(self.delete_button)
        self.r_v_layout.addWidget(self.submit_button)
        self.r_v_layout.addWidget(self.query_button)
        self.r_v_layout.addWidget(self.config_button)

        self.m_h_layout = QHBoxLayout()
        self.m_h_layout.addLayout(self.l_grid_layout)
        self.m_h_layout.addLayout(self.m_grid_layout)
        self.m_h_layout.addLayout(self.r_v_layout)
        self.all_v_layout = QVBoxLayout()
        self.all_v_layout.addLayout(self.up_h_layout)
        self.all_v_layout.addLayout(self.m_h_layout)
        self.all_v_layout.addWidget(self.message_table)
        self.tab1.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap((QPixmap('./image/light_off.png')))
        self.pic_label.setScaledContents(True)

    def on_off_bulb_func(self):
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap('./image/light_off.png'))
            self.pic_label.setScaledContents(True)
        else:
            self.pic_label.setPixmap(QPixmap('./image/light_on.png'))
            self.pic_label.setScaledContents(True)

    def tab2_ui(self):
        # 基本信息
        self.tab2_sample_number_label = QLabel('样品编号:')
        self.tab2_sample_number_browser = QTextBrowser()
        self.tab2_sample_number_browser.setText('00001')
        self.tab2_sample_number_browser.setMinimumSize(80, 20)
        self.tab2_sample_number_browser.setMaximumSize(100, 20)
        self.tab2_tester_name_label = QLabel('测试人员:')
        self.tab2_tester_name_browser = QTextBrowser()
        self.tab2_tester_name_browser.setText('薛岩')
        self.tab2_tester_name_browser.setMinimumSize(80, 20)
        self.tab2_tester_name_browser.setMaximumSize(100, 20)
        self.tab2_supervisor_name_label = QLabel('复核/监督人员:')
        self.tab2_supervisor_name_combo = QComboBox()
        self.tab2_supervisor_name_combo.setMaximumSize(80, 20)
        self.tab2_supervisor_name_combo.addItem('刘力')
        self.tab2_supervisor_name_combo.addItem('申亚飞')
        self.tab2_supervisor_name_combo.addItem('裴毓')
        self.tab2_supervisor_name_combo.addItem('张晓蕾')
        self.tab2_supervisor_name_combo.addItem('薛岩')
        self.tab2_test_data_label = QLabel('试验日期')
        self.tab2_test_data_edit = QDateEdit()
        self.tab2_test_data_edit.setMaximumSize(200, 20)
        self.tab2_test_data_edit.setCalendarPopup(True)
        self.tab2_test_data_edit.setDate(QtCore.QDate(2020, 1, 1))
        # 测试内容
        self.tab2_horizontal_power_box = QCheckBox('水平探测威力')
        self.tab2_vertical_power_box = QCheckBox('垂直探测威力')
        self.tab2_distance_resolution_box = QCheckBox('距离分辨率')
        self.tab2_distance_distinction_box = QCheckBox('距离区分度')
        self.tab2_horizontal_angular_range_box = QCheckBox('水平角度范围')
        self.tab2_vertical_angular_range_box = QCheckBox('垂直角度范围')
        self.tab2_angular_resolution_box = QCheckBox('角度分辨率')
        self.tab2_horizontal_distinction_box = QCheckBox('角度区分度')
        self.tab2_speed_range_box = QCheckBox('速度范围')
        self.tab2_speed_resolution_box = QCheckBox('速度分辨率')
        self.tab2_speed_distinction_box = QCheckBox('速度区分度')
        self.tab2_test_start_button = QPushButton('开始测试')
        self.tab2_horizontal_power_config_button = QPushButton('设置')
        self.tab2_horizontal_power_config_button.setEnabled(False)
        self.horizontal_power_config_menu_window = HorizontalPowerMenu()
        self.tab2_horizontal_power_config_button.clicked.connect(self.horizontal_power_config_menu_window.show)
        self.tab2_horizontal_power_box.stateChanged.connect(self.tab2_horizontal_power_button_status)
        self.tab2_vertical_power_config_button = QPushButton('设置')
        self.tab2_vertical_power_config_button.setEnabled(False)
        self.tab2_vertical_power_box.stateChanged.connect(self.tab2_vertical_power_button_status)
        self.tab2_distance_resolution_config_button = QPushButton('设置')
        self.tab2_distance_resolution_config_button.setEnabled(False)
        self.tab2_distance_resolution_box.stateChanged.connect(self.tab2_distance_resolution_button_status)
        self.tab2_distance_distinction_config_button = QPushButton('设置')
        self.tab2_distance_distinction_config_button.setEnabled(False)
        self.tab2_distance_distinction_box.stateChanged.connect(self.tab2_distance_distinction_button_status)
        self.tab2_horizontal_angular_range_config_button = QPushButton('设置')
        self.tab2_horizontal_angular_range_config_button.setEnabled(False)
        self.tab2_horizontal_angular_range_box.stateChanged.connect(self.tab2_horizontal_angular_range_button_status)
        self.tab2_vertical_angular_range_config_button = QPushButton('设置')
        self.tab2_vertical_angular_range_config_button.setEnabled(False)
        self.tab2_vertical_angular_range_box.stateChanged.connect(self.tab2_vertical_angular_range_button_status)
        self.tab2_angular_resolution_config_button = QPushButton('设置')
        self.tab2_angular_resolution_config_button.setEnabled(False)
        self.tab2_angular_resolution_box.stateChanged.connect(self.tab2_angular_resolution_button_status)
        self.tab2_horizontal_distinction_config_button = QPushButton('设置')
        self.tab2_horizontal_distinction_config_button.setEnabled(False)
        self.tab2_horizontal_distinction_box.stateChanged.connect(self.tab2_horizontal_distinction_button_status)
        self.tab2_speed_range_config_button = QPushButton('设置')
        self.tab2_speed_range_config_button.setEnabled(False)
        self.tab2_speed_range_box.stateChanged.connect(self.tab2_speed_range_button_status)
        self.tab2_speed_resolution_config_button = QPushButton('设置')
        self.tab2_speed_resolution_config_button.setEnabled(False)
        self.tab2_speed_resolution_box.stateChanged.connect(self.tab2_speed_resolution_button_status)
        self.tab2_speed_distinction_config_button = QPushButton('设置')
        self.tab2_speed_distinction_config_button.setEnabled(False)
        self.tab2_speed_distinction_box.stateChanged.connect(self.tab2_speed_distinction_button_status)
        # 状态信息
        self.tab2_status_test_label = QLabel('测试状态')
        self.tab2_status_test_edit = QTextEdit()
        self.tab2_result_test_label = QLabel('试验结果')
        self.tab2_result_test_edit = QTextEdit()
        # 雷达目标信息
        self.tab2_realtime_plot = pg.PlotWidget()
        self.tab2_realtime_plot.showGrid(x=True, y=True)
        self.tab2_realtime_plot.setRange(xRange=[-10, 10], yRange=[0, 300])
        self.tab2_realtime_table = QTableWidget()
        self.tab2_realtime_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tab2_realtime_table.setColumnCount(6)
        self.tab2_realtime_table.setRowCount(10)
        self.tab2_realtime_table.setHorizontalHeaderLabels(['ID', '垂直距离', '水平距离', '方位角度', '相对速度', '目标RCS'])
        # 位置初始化
        self.tab2_layout_init()

    def tab2_layout_init(self):
        # ---底层界面布局---
        # 左侧顶层布局
        self.tab2_lu_h_layout = QHBoxLayout()
        self.tab2_lu_h_layout.addWidget(self.tab2_sample_number_label)
        self.tab2_lu_h_layout.addWidget(self.tab2_sample_number_browser)
        self.tab2_lu_h_layout.addWidget(self.tab2_tester_name_label)
        self.tab2_lu_h_layout.addWidget(self.tab2_tester_name_browser)
        self.tab2_lu_h_layout.addWidget(self.tab2_supervisor_name_label)
        self.tab2_lu_h_layout.addWidget(self.tab2_supervisor_name_combo)
        self.tab2_lu_h_layout.addWidget(self.tab2_test_data_label)
        self.tab2_lu_h_layout.addWidget(self.tab2_test_data_edit)
        # 左侧底部L布局
        self.tab2_ldl_grid_layout = QGridLayout()
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_power_box, 0, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_power_config_button, 0, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_power_box, 1, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_power_config_button, 1, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_resolution_box, 2, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_resolution_config_button, 2, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_distinction_box, 3, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_distinction_config_button, 3, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_angular_range_box, 4, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_angular_range_config_button, 4, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_angular_range_box, 5, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_angular_range_config_button, 5, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_distinction_box, 6, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_distinction_config_button, 6, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_range_box, 7, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_range_config_button, 7, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_resolution_box, 8, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_resolution_config_button, 8, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_distinction_box, 9, 0, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_distinction_config_button, 9, 2, 1, 1)
        self.tab2_ldl_grid_layout.addWidget(self.tab2_test_start_button, 10, 0, 1, 3)
        # 左侧底部R布局
        self.tab2_ldr_v_layout = QVBoxLayout()
        self.tab2_ldr_v_layout.addWidget(self.tab2_status_test_label)
        self.tab2_ldr_v_layout.addWidget(self.tab2_status_test_edit)
        self.tab2_ldr_v_layout.addWidget(self.tab2_result_test_label)
        self.tab2_ldr_v_layout.addWidget(self.tab2_result_test_edit)
        self.tab2_ldr_v_layout.addWidget(self.tab2_realtime_table)
        # 左侧底部布局
        self.tab2_ld_h_layout = QHBoxLayout()
        self.tab2_ld_h_layout.addLayout(self.tab2_ldl_grid_layout)
        self.tab2_ld_h_layout.addLayout(self.tab2_ldr_v_layout)
        # 右侧布局
        self.tab2_right_v_layout = QVBoxLayout()
        self.tab2_right_v_layout.addWidget(self.tab2_realtime_plot)
        # 左侧布局
        self.tab2_left_v_layout = QVBoxLayout()
        self.tab2_left_v_layout.addLayout(self.tab2_lu_h_layout)
        self.tab2_left_v_layout.addLayout(self.tab2_ld_h_layout)
        # 完整布局
        self.all_h_layout = QHBoxLayout()
        self.all_h_layout.addLayout(self.tab2_left_v_layout)
        self.all_h_layout.addLayout(self.tab2_right_v_layout)
        self.tab2.setLayout(self.all_h_layout)

    def tab2_horizontal_power_button_status(self):
        if self.tab2_horizontal_power_box.checkState() == 2:
            self.tab2_horizontal_power_config_button.setEnabled(True)
        else:
            self.tab2_horizontal_power_config_button.setEnabled(False)

    def tab2_vertical_power_button_status(self):
        if self.tab2_vertical_power_box.checkState() == 2:
            self.tab2_vertical_power_config_button.setEnabled(True)
        else:
            self.tab2_vertical_power_config_button.setEnabled(False)

    def tab2_distance_resolution_button_status(self):
        if self.tab2_distance_resolution_box.checkState() == 2:
            self.tab2_distance_resolution_config_button.setEnabled(True)
        else:
            self.tab2_distance_resolution_config_button.setEnabled(False)

    def tab2_distance_distinction_button_status(self):
        if self.tab2_distance_distinction_box.checkState() == 2:
            self.tab2_distance_distinction_config_button.setEnabled(True)
        else:
            self.tab2_distance_distinction_config_button.setEnabled(False)

    def tab2_horizontal_angular_range_button_status(self):
        if self.tab2_horizontal_angular_range_box.checkState() == 2:
            self.tab2_horizontal_angular_range_config_button.setEnabled(True)
        else:
            self.tab2_horizontal_angular_range_config_button.setEnabled(False)

    def tab2_vertical_angular_range_button_status(self):
        if self.tab2_vertical_angular_range_box.checkState() == 2:
            self.tab2_vertical_angular_range_config_button.setEnabled(True)
        else:
            self.tab2_vertical_angular_range_config_button.setEnabled(False)

    def tab2_angular_resolution_button_status(self):
        if self.tab2_angular_resolution_box.checkState() == 2:
            self.tab2_angular_resolution_config_button.setEnabled(True)
        else:
            self.tab2_angular_resolution_config_button.setEnabled(False)

    def tab2_horizontal_distinction_button_status(self):
        if self.tab2_horizontal_distinction_box.checkState() == 2:
            self.tab2_horizontal_distinction_config_button.setEnabled(True)
        else:
            self.tab2_horizontal_distinction_config_button.setEnabled(False)

    def tab2_speed_range_button_status(self):
        if self.tab2_speed_range_box.checkState() == 2:
            self.tab2_speed_range_config_button.setEnabled(True)
        else:
            self.tab2_speed_range_config_button.setEnabled(False)

    def tab2_speed_resolution_button_status(self):
        if self.tab2_speed_resolution_box.checkState() == 2:
            self.tab2_speed_resolution_config_button.setEnabled(True)
        else:
            self.tab2_speed_resolution_config_button.setEnabled(False)

    def tab2_speed_distinction_button_status(self):
        if self.tab2_speed_distinction_box.checkState() == 2:
            self.tab2_speed_distinction_config_button.setEnabled(True)
        else:
            self.tab2_speed_distinction_config_button.setEnabled(False)

    def tab3_ui(self):
        pass


class HorizontalPowerMenu(QWidget):
    def __init__(self):
        super(HorizontalPowerMenu, self).__init__()
        self.resize(200, 200)
        self.setWindowTitle('水平威力范围设置')
        self.min_range_label = QLabel('最小测试距离')
        self.min_range_edit = QTextEdit('30')
        self.min_range_edit.setMaximumSize(50, 25)
        self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_range_unit_label = QLabel('m')
        self.max_range_label = QLabel('最大测试距离')
        self.max_range_edit = QTextEdit('200')
        self.max_range_edit.setMaximumSize(50, 25)
        self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.max_range_unit_label = QLabel('m')
        self.min_angle_label = QLabel('最小测试角度')
        self.min_angle_edit = QTextEdit('-60')
        self.min_angle_edit.setMaximumSize(50, 25)
        self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_angle_unit_label = QLabel('°')
        self.max_angle_label = QLabel('最大测试角度')
        self.max_angle_edit = QTextEdit('60')
        self.max_angle_edit.setMaximumSize(50, 25)
        self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.max_angle_unit_label = QLabel('°')
        self.step_range_label = QLabel('距离步进')
        self.step_range_edit = QTextEdit('1')
        self.step_range_edit.setMaximumSize(50, 25)
        self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.step_range_unit_label = QLabel('m')
        self.step_angle_label = QLabel('角度步进')
        self.step_angle_edit = QTextEdit('1')
        self.step_angle_edit.setMaximumSize(50, 25)
        self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.step_angle_unit_label = QLabel('°')
        self.motor_pattern_one_way_button = QRadioButton('单向运动')
        self.motor_pattern_round_trip_button = QRadioButton('往返运动')
        self.motor_pattern_round_trip_button.setChecked(True)
        self.motor_pattern_round_trip_button.toggled.connect(self.radiobutton_select)
        self.motor_pattern_one_way_combo = QComboBox()
        self.motor_pattern_one_way_combo.addItems(('远离', '靠近'))
        self.motor_pattern_one_way_combo.setEnabled(False)
        self.test_mode_combo = QComboBox()
        self.test_mode_combo.addItems(('先距离后角度', '先角度后距离'))
        self.confirm_button = QPushButton('确认')
        self.confirm_button.clicked.connect(self.set_result__output)
        self.layout_init()

    def layout_init(self):
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.grid_layout.addWidget(self.min_range_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.min_range_edit, 0, 1, 1, 2)
        self.grid_layout.addWidget(self.min_range_unit_label, 0, 3, 1, 1)
        self.grid_layout.addWidget(self.max_range_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.max_range_edit, 1, 1, 1, 2)
        self.grid_layout.addWidget(self.max_range_unit_label, 1, 3, 1, 1)
        self.grid_layout.addWidget(self.min_angle_label, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.min_angle_edit, 2, 1, 1, 2)
        self.grid_layout.addWidget(self.min_angle_unit_label, 2, 3, 1, 1)
        self.grid_layout.addWidget(self.max_angle_label, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.max_angle_edit, 3, 1, 1, 2)
        self.grid_layout.addWidget(self.max_angle_unit_label, 3, 3, 1, 1)
        self.grid_layout.addWidget(self.step_range_label, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.step_range_edit, 4, 1, 1, 2)
        self.grid_layout.addWidget(self.step_range_unit_label, 4, 3, 1, 1)
        self.grid_layout.addWidget(self.step_angle_label, 5, 0, 1, 1)
        self.grid_layout.addWidget(self.step_angle_edit, 5, 1, 1, 2)
        self.grid_layout.addWidget(self.step_angle_unit_label, 5, 3, 1, 1)
        self.v_layout.addWidget(self.motor_pattern_round_trip_button)
        self.v_layout.addWidget(self.motor_pattern_one_way_button)
        self.v_layout.addWidget(self.motor_pattern_one_way_combo)
        self.v_layout.addWidget(self.test_mode_combo)
        self.v_layout.addWidget(self.confirm_button)
        self.h_layout.addLayout(self.grid_layout)
        self.h_layout.addLayout(self.v_layout)
        self.setLayout(self.h_layout)

    def radiobutton_select(self):
        if self.motor_pattern_round_trip_button.isChecked():
            self.motor_pattern_one_way_combo.setEnabled(False)
        else:
            self.motor_pattern_one_way_combo.setEnabled(True)

    def set_result__output(self):
        if self.motor_pattern_round_trip_button.isChecked():
            motor_pattern = '往返运动'
            motor_pattern_one_way = ''
        else:
            motor_pattern = '单向运动'
            motor_pattern_one_way = self.motor_pattern_one_way_combo.currentText()
        print('最小测试距离设置为：%sm\n'
              '最大测试距离设置为：%sm\n'
              '最小测试角度设置为：%s°\n'
              '最大测试角度设置为：%s°\n'
              '步进距离设置为：%sm\n'
              '步进角度设置为：%sm\n'
              '运动模式设置为：%s\n'
              '单向运动模式设置为：%s\n'
              '测试模式设置为：%s\n' % (
                self.min_range_edit.toPlainText(),
                self.max_range_edit.toPlainText(),
                self.min_angle_edit.toPlainText(),
                self.max_angle_edit.toPlainText(),
                self.step_range_edit.toPlainText(),
                self.step_angle_edit.toPlainText(),
                motor_pattern,
                motor_pattern_one_way,
                self.test_mode_combo.currentText()))
        file = open('./config/HorizontalPowerTest.txt', 'w+')
        file.write('最小测试距离设置为：%sm\n'
                   '最大测试距离设置为：%sm\n'
                   '最小测试角度设置为：%s°\n'
                   '最大测试角度设置为：%s°\n'
                   '步进距离设置为：%sm\n'
                   '步进角度设置为：%sm\n'
                   '运动模式设置为：%s\n'
                   '单向运动模式设置为：%s\n'
                   '测试模式设置为：%s\n' % (
                    self.min_range_edit.toPlainText(),
                    self.max_range_edit.toPlainText(),
                    self.min_angle_edit.toPlainText(),
                    self.max_angle_edit.toPlainText(),
                    self.step_range_edit.toPlainText(),
                    self.step_angle_edit.toPlainText(),
                    motor_pattern,
                    motor_pattern_one_way,
                    self.test_mode_combo.currentText()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radar_test = RadarTestMain()
    radar_test.show()
    sys.exit(app.exec())
