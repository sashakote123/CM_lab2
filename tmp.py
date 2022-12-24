class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self, function_index):
        functions = {
            1: func()
        }

        x = functions[function_index][0]
        y = functions[function_index][1]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')
        ax.set_ylim([0, self.y_lim])
        ax.set_xlim([0, self.x_lim])

        ax.plot(x, y, linestyle='-', color='#008000')
        self.canvas.draw()


def returnFunc(funcindex):
    functions = {
        1: func()
    }
    return functions[funcindex]
