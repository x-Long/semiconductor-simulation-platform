import os

from UI_BJT import Ui_Form
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5.QtCore import QCoreApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.creatFigure()
        self.i = 1  # 计数器

    # 创建绘图类，并发射信号
    def creatFigure(self):
        # self.figure = plt.figure(facecolor='#FFD7C4')
        # 控制绘图比例
        self.figure = plt.figure(figsize=(8, 8), )  # 可选参数,facecolor为背景颜色  600 * 650大小
        self.canvas = FigureCanvas(self.figure)
        # 将图放入布局
        self.verticalLayout_3.addWidget(self.canvas)

        # 发射信号  链接槽函数
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.runButton.clicked.connect(self.Draw)
        self.pushButton.clicked.connect(self.clea)
        self.pushButton_1.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.cal)
        plt.plot()
        self.canvas.draw()

        # 根据材料 填写数据
        self.Si.toggled.connect(self.materInput)
        self.Ge.toggled.connect(self.materInput)
        self.GaAs.toggled.connect(self.materInput)

    def save(self):
        RanNum = np.random.uniform(1, 2, )
        img_src = os.path.join(os.path.expanduser("~"), 'Desktop', "python_practice", str(RanNum)[2:8] + '.png')
        if self.radioButton.isChecked() == True:
            plt.savefig(img_src, dpi=100)
        else:
            plt.savefig(img_src, dpi=300)
        # 提示保存框
        QtWidgets.QMessageBox.about(main_window, "保存图表", "已将图表保存至桌面")

    def clea(self):
        self.figure.clear()
        plt.plot()
        self.canvas.draw()
        self.i = 1

    # 材料选择改变时 填写数据
    def materInput(self):
        if self.Si.isChecked() == True:
            self.Eg.setText('1.12')
            self.ni.setText('1.5 * (10 ** 10)')
            self.es.setText('13.1 * 8.85 * 10 ** (-14)')
            self.Dn.setText('25')
            self.Dp.setText('10')
            self.tn0.setText('1 * (10 ** (-7))')
            self.tp0.setText('5 * (10 ** (-7))')
        elif self.GaAs.isChecked() == True:
            self.Eg.setText('1.42')
            self.ni.setText('1.8 * (10 ** 6)')
            self.es.setText('11.7 * 8.85 * 10 ** (-14)')
            self.Dn.setText('210')
            self.Dp.setText('8')
            self.tn0.setText('1 * (10 ** (-7))')
            self.tp0.setText('5 * (10 ** (-8))')
        elif self.Ge.isChecked() == True:
            self.Eg.setText('0.66')
            self.ni.setText('2.4 * (10 ** 13)')
            self.es.setText('16.0 * 8.85 * 10 ** (-14)')
            self.Dn.setText('48')
            self.Dp.setText('90')
            self.tn0.setText('2 * (10 ** (-6))')
            self.tp0.setText('2 * (10 ** (-6))')

    # 计算的代码
    def cal(self):

        T = 300  # 温度

        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度

        LLp = eval(self.LLp.text())  ### p区长度
        LLn = eval(self.LLn.text())  ### n区长度

        Eg = eval(self.Eg.text())
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度

        np0 = (ni ** 2) / Na  # p区少子浓度
        self.np0.setText(str(np0))  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度
        self.pn0.setText(str(pn0))

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压 为负时应当小于Vbi
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        self.Vbi.setText(str(Vbi))
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        self.Xp.setText(str(Xp))
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        self.Xn.setText(str(Xn))

        Emax = (-e * Na / es) * Xp
        self.Emax.setText(str(Emax))

    #####################

    # ND能带  ND已经OK
    def DrawND(self):
        Vbe = 0.4
        Vce = 5
        Vcb = Vce - Vbe

        Xe = 0.05 * 10 ** (-4)
        Xb = 0.05 * 10 ** (-4)
        Xc = 0.05 * 10 ** (-4)

        Ne = 5 * (10 ** 18)  # n区
        Nb = 5 * (10 ** 18)  # p区
        Nc = 5 * (10 ** 18)  # n区

        Eg = 1.12
        ni = 1.5 * (10 ** (10))

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = 11.7 * 8.85 * 10 ** (-14)  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Vbi1 = Vt * np.log(Ne * Nb / (ni ** 2))  # 内建电场
        Vtotal = Vbi1 - Vbe  # 总电压
        X1 = np.sqrt((2 * es * Vtotal / e) * (Nb / Ne) * (1 / (Ne + Nb)))  # n区内建宽度
        X2 = np.sqrt((2 * es * Vtotal / e) * (Ne / Nb) * (1 / (Ne + Nb)))  # p区内建宽度
        x1 = np.linspace(-X1, 0, 100)  # 从-1到1生成100个点
        x2 = np.linspace(0, X2, 100)
        Q1 = ((e * Nb / (2 * es)) * (X2 ** 2) + (e * Ne / es) * (X1 * (-x1) - ((-x1) ** 2) / 2))  # n区电势 0<x<Xn
        Q2 = ((e * Nb / (2 * es)) * (((-x2) + X2) ** 2))  # p区电势   -Xp<x<0

        Vbi2 = Vt * np.log(Ne * Nc / (ni ** 2))  # 内建电场
        Vtotal = Vbi2 + Vcb  # 总电压
        X3 = np.sqrt((2 * es * Vtotal / e) * (Nc / Nb) * (1 / (Nc + Nb)))  # p区内建宽度
        X4 = np.sqrt((2 * es * Vtotal / e) * (Nb / Nc) * (1 / (Nc + Nb)))  # n区内建宽
        x3 = np.linspace(-X3 + Xb, 0 + Xb, 100)  # 从-1到1生成100个点
        x4 = np.linspace(0 + Xb, X4 + Xb, 100)
        Q3 = ((e * Nc / (2 * es)) * ((x3 - Xb + X3) ** 2))  # p区电势   -Xp<x<0
        Q4 = ((e * Nc / (2 * es)) * (X3 ** 2) + (e * Nc / es) * (X4 * (x4 - Xb) - ((x4 - Xb) ** 2) / 2))  # n区电势 0<x<Xn

        x5 = np.linspace(-Xe, -X1, 100)
        Q5 = ((e * Nb / (2 * es)) * (X2 ** 2) + (e * Ne / es) * (X1 * (X1) - ((X1) ** 2) / 2)) + x5 - x5
        x6 = np.linspace(X2, (Xb - X3), 100)
        Q6 = 0 + x6 - x6
        x7 = np.linspace(Xb + X4, Xb + Xc, 100)
        Q7 = ((e * Nc / (2 * es)) * (X3 ** 2) + (e * Nc / es) * (
                X4 * (X4 + Xb - Xb) - ((X4 + Xb - Xb) ** 2) / 2)) + x7 - x7  # n区电势 0<x<Xn

        plt.plot(x1 * (10 ** 4), -e * Q1, )
        plt.plot(x2 * (10 ** 4), -e * Q2, '--', )
        plt.plot(x3 * (10 ** 4), -e * Q3, )
        plt.plot(x4 * (10 ** 4), -e * Q4, '--', )
        plt.plot(x5 * (10 ** 4), -e * Q5, '--', label='Ec仿真' + str(self.i))
        plt.plot(x6 * (10 ** 4), -e * Q6, )
        plt.plot(x7 * (10 ** 4), -e * Q7, )
        plt.plot(x1 * (10 ** 4), -e * Q1 - e * Eg, )
        plt.plot(x2 * (10 ** 4), -e * Q2 - e * Eg, '--', )
        plt.plot(x3 * (10 ** 4), -e * Q3 - e * Eg, )
        plt.plot(x4 * (10 ** 4), -e * Q4 - e * Eg, '--', )
        plt.plot(x5 * (10 ** 4), -e * Q5 - e * Eg, '--', label='Ev仿真' + str(self.i))
        plt.plot(x6 * (10 ** 4), -e * Q6 - e * Eg, )
        plt.plot(x7 * (10 ** 4), -e * Q7 - e * Eg, )
        self.i = self.i + 1
        plt.title('BJT内部能带分布图', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('能级（ev）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        self.canvas.draw()

    # SZ 少子分布
    # npn型
    def DrawSZ(self):

        Vbe = 0.1
        Vce = 5

        Xe = 0.8 * 10 ** (-4)
        Xb = 2 * 10 ** (-4)
        Xc = 2 * 10 ** (-4)

        Ne = 5 * (10 ** 18)
        Nb = 1 * (10 ** 17)
        Nc = 5 * (10 ** 15)

        De = 15
        Db = 15
        Dc = 15

        te0 = 5 * 10 ** (-8)
        tb0 = 5 * 10 ** (-8)
        tc0 = 5 * 10 ** (-8)

        ni = 1.5 * (10 ** (10))
        # 以上数据要获取

        Le = np.sqrt(De * te0)
        Lb = np.sqrt(Db * tb0)
        Lc = np.sqrt(Dc * tc0)

        Pe0 = (ni ** 2) / Ne
        Nb0 = (ni ** 2) / Nb
        Pc0 = (ni ** 2) / Nc
        # 以上为数据

        # e 发射区少子分布
        x1 = np.linspace(-Xe, 0, 100)
        # x2 = np.linspace(0, Xe, 100)
        Pex = (Pe0 / Le) * (np.exp(Vbe / 0.0259) - 1) * (Xe + x1) + Pe0
        # Pex = (Pe0 / np.sinh(Xe/Le)) * (np.exp(Vbe / 0.0259) - 1) * np.sinh((Xe + x1)/Le) + Pe0
        Pe0 = Pe0 + x1 - x1

        # b 基区少子分布
        x2 = np.linspace(0, Xb, 100)
        # Nbx = (Nb0 / Xb) * ((Xb - x2) * (np.exp(Vbe / 0.0259) - 1) - x2) + Nb0
        Nbx = (Nb0 / np.sinh(Xb / Lb)) * (np.sinh((Xb - x2) / Lb) * (np.exp(Vbe / 0.0259) - 1) - np.sinh(x2 / Lb)) + Nb0
        Nb0 = Nb0 + x2 - x2

        # c 集电区少子分布
        Xd = Xb + Xc
        x3 = np.linspace(Xb, Xd, 100)
        Pcx = Pc0 - Pc0 * (np.exp(-(x3 - Xb) / Lc))
        Pc0 = Pc0 + x3 - x3

        # label与legend一起设置图例

        # 画平衡
        plt.plot(x1, np.log10(Pe0), )
        plt.plot(x2, np.log10(Nb0), )
        plt.plot(x3, np.log10(Pc0), )

        plt.plot(x1, np.log10(Pex), )
        plt.plot(x2, np.log10(Nbx), )
        plt.plot(x3, np.log10(Pcx), )

        plt.title('BJT少子分布图', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        plt.ylabel('浓度', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # I-V 关系
    def DrawIV(self):

        ni = 1.5 * (10 ** (10))
        Ne = 10 ** 18
        Nb = 1 * (10 ** 17)
        Nc = 10 ** 16
        De = 8
        Db = 15
        Dc = 12
        te0 = 10 ** (-8)
        tb0 = 5 * 10 ** (-8)
        tc0 = 10 ** (-7)
        Le = np.sqrt(De * te0)
        Lb = np.sqrt(Db * tb0)
        Lc = np.sqrt(Dc * tc0)
        Xe = 0.2 * 10 ** (-4)
        Xb = 0.1 * 10 ** (-4)
        Xc = 0.1 * 10 ** (-4)
        Vbe = 0.6
        Vce = 5
        Pe0 = (ni ** 2) / Ne
        Nb0 = (ni ** 2) / Nb
        Pc0 = (ni ** 2) / Nc

    # 正式测试
    def Draw(self):
        self.cal()
        self.DrawND()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()
