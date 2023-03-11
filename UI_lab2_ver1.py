from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

import main_program
from test_program import *
from main_program import *
class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс
    N = 100

    def set_N(self, N):
        self.N = N
        print(N)
    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self, function_index):

        functions = {
            1: get_data1(self.N),
            2: get_data2(self.N),
        }

        x = functions[function_index][0]
        y = functions[function_index][1]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        ax.plot(x, y, linestyle='-', color='#008000')
        self.canvas.draw()

def returnFunc(funcindex):

    functions = {
        1: info(PlotWidget.N),
        2: get_data2(PlotWidget.N)
    }
    return functions[funcindex]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget()
        #self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(820, 10, 661, 451))
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(315, 10, 501, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 380, 291, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_N = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_N.setObjectName("line_N")
        self.line_N.setText('100')
        self.gridLayout.addWidget(self.line_N, 0, 1, 1, 1)
        self.N_line_PB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.N_line_PB.setObjectName("N_line_PB")
        self.gridLayout.addWidget(self.N_line_PB, 0, 2, 1, 1)
        self.plot_test_PB = QtWidgets.QPushButton(self.centralwidget)
        self.plot_test_PB.setGeometry(QtCore.QRect(160, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_test_PB.setFont(font)
        self.plot_test_PB.setObjectName("plot_test_PB")
        self.plot_main_PB = QtWidgets.QPushButton(self.centralwidget)
        self.plot_main_PB.setGeometry(QtCore.QRect(10, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_main_PB.setFont(font)
        self.plot_main_PB.setObjectName("plot_main_PB")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 480, 531, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.N_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.N_label.setObjectName("N_label")
        self.horizontalLayout.addWidget(self.N_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(610, 480, 521, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.NMain_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.NMain_label.setObjectName("NMain_label")
        self.horizontalLayout_2.addWidget(self.NMain_label)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 510, 400, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.S_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.S_label.setFont(font)
        self.S_label.setObjectName("S_label")
        self.horizontalLayout_3.addWidget(self.S_label)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(610, 510, 521, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.SMain_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SMain_label.setFont(font)
        self.SMain_label.setObjectName("SMain_label")
        self.horizontalLayout_4.addWidget(self.SMain_label)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 540, 531, 21))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.x_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x_label.setFont(font)
        self.x_label.setObjectName("x_label")
        self.horizontalLayout_5.addWidget(self.x_label)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(610, 540, 190, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.horizontalLayoutWidget_6.setFont(font)
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.xMain_label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.xMain_label.setFont(font)
        self.xMain_label.setObjectName("xMain_label")
        self.horizontalLayout_6.addWidget(self.xMain_label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 291, 361))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("numeros.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.l = QVBoxLayout(self.centralwidget)
        self.bl = QHBoxLayout(self.centralwidget)

        self.l2 = QVBoxLayout(self.widget)
        self.l.addWidget(self.widget)
        self.l2.addWidget(self.widget)

        self.message = QMessageBox()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№ Узла"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "x"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "u(x)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "v(x)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "|u(x)-v(x)|"))
        self.label.setText(_translate("MainWindow", "Число разбиений: "))
        self.N_line_PB.setText(_translate("MainWindow", "Подтвердить"))
        self.plot_test_PB.setText(_translate("MainWindow", "Решить тестовую \n"
" задачу"))
        self.plot_main_PB.setText(_translate("MainWindow", "Решить основную \n"
" задачу"))
        self.label_5.setText(_translate("MainWindow", "Для решения тестовой задачи использована сетка с числом разбиений по x:"))
        self.N_label.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Для решения основной задачи использована сетка с числом разбиений по x:"))
        self.NMain_label.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Тестовая задача решена с точностью:"))
        self.S_label.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "При пересчете задачи с половинным шагом, максимальная разность приближений:"))
        self.SMain_label.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Максимальное отклонение точного и приближенного решения наблюдается в точке: "))
        self.x_label.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "И соответствует узлу х = "))
        self.xMain_label.setText(_translate("MainWindow", "0"))
        self.N_line_PB.clicked.connect(lambda: PlotWidget.set_N(PlotWidget, int(self.line_N.text())))
        self.plot_test_PB.clicked.connect(lambda: self.widget.plot(1))
        self.plot_test_PB.clicked.connect(lambda: self.tableWidget.setRowCount(PlotWidget.N+1))
        self.plot_test_PB.clicked.connect(lambda: self.setTable(1))
        self.plot_test_PB.clicked.connect(lambda: self.setInfo(1))
        self.plot_test_PB.clicked.connect(lambda: (print("clicked")))

        self.plot_main_PB.clicked.connect(lambda: self.widget.plot(2))
        self.plot_main_PB.clicked.connect(lambda: self.tableWidget.setRowCount(PlotWidget.N+1))
        self.plot_main_PB.clicked.connect(lambda: self.setTable(2))
        self.plot_main_PB.clicked.connect(lambda: self.setInfo(2))
        self.plot_main_PB.clicked.connect(lambda: (print("clicked")))

    def setInfo(self, funcindex):
        self.N_label.setText('0')
        self.S_label.setText('0')
        self.x_label.setText('0')
        self.NMain_label.setText('0')
        self.SMain_label.setText('0')
        self.xMain_label.setText('0')

        if funcindex == 1:
            List = returnFunc(funcindex)
            element = max(List[3])
            index = List[3].index(element)
            self.N_label.setText(str(PlotWidget.N))
            self.S_label.setText(str(max(List[3])))
            self.x_label.setText(str(List[0][index]))
            self.NMain_label.setText('0')
            self.SMain_label.setText('0')
            self.xMain_label.setText('0')

        if funcindex == 2:
            List = returnFunc(funcindex)
            element = max(List[4])
            index = List[4].index(element)
            self.N_label.setText('0')
            self.S_label.setText('0')
            self.x_label.setText('0')
            self.NMain_label.setText(str(PlotWidget.N))
            self.SMain_label.setText(str(max(List[4])))
            self.xMain_label.setText(str(List[2][index]))


    def setTable(self, funcindex):
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(123)))
        self.tableWidget.clearContents()
        List = returnFunc(funcindex)
        for i in range(PlotWidget.N+1):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(List[1][i])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(List[2][i])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(List[3][i])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
