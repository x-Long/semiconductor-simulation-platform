import os

from UI_PN import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
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

    # 槽函数
    def save(self):
        RanNum = np.random.uniform(1, 2, )
        img_src = os.path.join(os.path.expanduser("~"), 'Desktop', "python_practice", str(RanNum)[2:8] + '.png')
        if self.radioButton.isChecked() == True:
            plt.savefig(img_src, dpi=100)
        else:
            plt.savefig(img_src, dpi=300)
        # 提示保存框
        QtWidgets.QMessageBox.about(main_window, "保存图表", "已将图表保存至桌面")

    # 清除figure
    def clea(self):
        self.figure.clear()
        plt.plot()
        self.canvas.draw()
        self.i = 1

    # 根据材料 填写数据
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

    # Qp 均匀掺杂pn结空间电荷区电势
    def DrawQp(self):

        T = 300  # 温度
        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压 为负时应当小于Vbi
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        # 以上 公共数据
        print(Xp)
        print(Xn)

        # Qp 均匀掺杂pn结空间电荷区电势
        xp = np.linspace(-Xp, 0, 20)  # 从-1到1生成100个点
        xn = np.linspace(0, Xn, 20)
        Qp = ((e * Na / (2 * es)) * ((xp + Xp) ** 2))  # p区电势   -Xp<x<0
        Qn = ((e * Na / (2 * es)) * (Xp ** 2) + (e * Nd / es) * (Xn * xn - (xn ** 2) / 2))  # n区电势 0<x<Xn

        # Qp 均匀掺杂pn结空间电荷区电势
        plt.plot(xp * (10 ** 4), Qp, '--p', label='P区' + str(self.i))
        plt.plot(xn * (10 ** 4), Qn, ':>', label='N区' + str(self.i))
        self.i = self.i + 1
        plt.title('均匀掺杂pn结空间电荷区电势', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电势（伏）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        self.canvas.draw()

    # Ep 均匀掺杂pn结空间电荷区电场
    def DrawEp(self):
        T = 300  # 温度

        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        # 以上 公共数据

        # Ep 均匀掺杂pn结空间电荷区电场
        xep = np.linspace(-Xp, 0, 20)  # 从-1到1生成100个点
        xen = np.linspace(0, Xn, 20)
        Ep = (-e * Na / es) * (xep + Xp)
        En = (-e * Nd / es) * (Xn - xen)
        # Ep 均匀掺杂pn结空间电荷区电场

        # 调整坐标轴，与外围框线
        ax = plt.gca()
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        ax.spines['top'].set_position(('data', 0))
        ax.spines['right'].set_position(('data', 0))

        plt.plot(xep * 10 ** 4, Ep * 10 ** (-4), '--.', linewidth='3', label='P区' + str(self.i))

        plt.plot(xen * 10 ** 4, En * 10 ** (-4), '--', linewidth='3', label='N区' + str(self.i))
        self.i = self.i + 1
        plt.title('均匀掺杂pn结空间电荷区电场', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))

        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电场强度（10^4 V/CM）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        self.canvas.draw()

    # Pp 突变pn结空间电荷密度
    def DrawPp(self):
        T = 300  # 温度

        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度

        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        # 以上 公共数据

        # Pp 突变pn结空间电荷密度
        xepp = np.linspace(-Xp, 0, 100)  # 从-1到1生成100个点
        xenn = np.linspace(0, Xn, 100)
        Pp = -e * Na + xepp - xepp
        Pn = e * Nd + xepp - xepp

        # Pp 突变pn结空间电荷密度
        plt.plot(xepp * 10 ** 4, Pp, label='P区' + str(self.i), linewidth='3', )
        plt.plot(xenn * 10 ** 4, Pn, label='N区' + str(self.i), linewidth='3', )
        self.i = self.i + 1

        # 组成矩形
        Pp1 = np.linspace(0, (-e * Na), 100)
        Pn4 = np.linspace(0, (e * Nd), 100)
        xepp1 = (-Xp) + Pp1 - Pp1
        xenn4 = Xn + Pn4 - Pn4

        plt.plot(xepp1 * 10 ** 4, Pp1, ':', linewidth='3', )
        plt.plot(xenn4 * 10 ** 4, Pn4, ':', linewidth='3', )

        plt.title('突变pn结空间电荷密度', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))

        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电荷密度（C/cm^3）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # # 调整坐标轴，与外围框线
        ax = plt.gca()
        ax.spines['top'].set_position(('data', 0))
        ax.spines['right'].set_position(('data', 0))

        # 绘图
        self.canvas.draw()

    # I-V关系
    def DrawIV(self):
        T = 300  # 温度

        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        # 以上 公共数据

        # I-V关系
        Dn = eval(self.Dn.text())  ###
        Dp = eval(self.Dp.text())  ###
        tn0 = eval(self.tn0.text())  ###
        tp0 = eval(self.tp0.text())  ###
        Ln = np.sqrt(tn0 * Dn)
        Lp = np.sqrt(tp0 * Dp)

        Js = e * Dp * pn0 / Lp + e * Dn * np0 / Ln
        v = np.linspace(-0.06, 0.06, 50)
        J = Js * (np.exp(v / 0.0259) - 1)

        # v,J pn结二极管的理想I-V特性
        plt.plot(v, J, '--p', label='I-V线' + str(self.i))  # np.log(J)
        self.i = self.i + 1
        plt.title('pn结二极管的理想I-V特性', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))

        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('偏压-Va', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电流-I', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        self.canvas.draw()

    # I-V关系 对数坐标
    def DrawIVDS(self):
        T = 300  # 温度

        Nd = eval(self.Nd.text())
        # Nd = 2 * (10 ** 16)  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())  ### 反偏电压 负数为正偏电压
        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度
        # 以上 公共数据

        # I-V关系
        Dn = eval(self.Dn.text())  ###
        Dp = eval(self.Dp.text())  ###
        tn0 = eval(self.tn0.text())  ###
        tp0 = eval(self.tp0.text())  ###
        Ln = np.sqrt(tn0 * Dn)
        Lp = np.sqrt(tp0 * Dp)

        Js = e * Dp * pn0 / Lp + e * Dn * np0 / Ln
        v = np.linspace(-0.06, 0.06, 50)
        J = Js * (np.exp(v / 0.0259) - 1)

        # v,J pn结二极管的理想I-V特性
        plt.plot(v, np.log(J), '--p', label='I-V线' + str(self.i))  # np.log(J)
        self.i = self.i + 1
        plt.title('pn结二极管的理想I-V特性', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))

        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('偏压-Va', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电流-In(I)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        self.canvas.draw()

    # ND pn结能带图
    def DrawND(self):

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
        # 以上 公共数据

        xp1 = np.linspace(-LLp, -Xp, 30)
        xp2 = np.linspace(-Xp, 0, 30)  # 从-1到1生成100个点
        xn3 = np.linspace(0, Xn, 30)
        xn4 = np.linspace(Xn, LLn, 30)
        Qp = ((e * Na / (2 * es)) * ((xp2 + Xp) ** 2))  # p区电势   -Xp<x<0
        Qn = ((e * Na / (2 * es)) * (Xp ** 2) + (e * Nd / es) * (Xn * xn3 - (xn3 ** 2) / 2))  # n区电势 0<x<Xn

        EEp1 = 0 + xp1 - xp1
        EEp2 = -e * Qp
        EEn3 = -e * Qn
        EEn4 = -e * ((e * Na / (2 * es)) * (Xp ** 2) + (e * Nd / es) * (Xn * Xn - (Xn ** 2) / 2)) + (xn4 - xn4)

        # Qp 均匀掺杂pn结空间电荷区电势   上方能带
        plt.plot(xp1 * (10 ** 4), EEp1, '--', linewidth='2', label='Ec仿真' + str(self.i))
        plt.plot(xp2 * (10 ** 4), EEp2, linewidth='2', )
        plt.plot(xn3 * (10 ** 4), EEn3, '--', linewidth='2', )
        plt.plot(xn4 * (10 ** 4), EEn4, linewidth='2', )

        # Qn 均匀掺杂pn结空间电荷区电势   下方能带
        plt.plot(xp1 * (10 ** 4), EEp1 - e * Eg, '--', linewidth='2', label='Ev仿真' + str(self.i))
        plt.plot(xp2 * (10 ** 4), EEp2 - e * Eg, linewidth='2', )
        plt.plot(xn3 * (10 ** 4), EEn3 - e * Eg, '--', linewidth='2', )
        plt.plot(xn4 * (10 ** 4), EEn4 - e * Eg, linewidth='2', )

        self.i = self.i + 1

        plt.title('突变pn结能带图', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('势垒宽度（微米）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('能级（ev）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        # plt.plot(x, y, linewidth='1', label="test", color=' coral ', linestyle=':', marker='|')
        self.canvas.draw()

    # pnx 正偏条件下pn结内部的稳态少子浓度
    def Drawpnx(self):

        T = 300  # 温度

        # Nd = eval(self.shuru.text())
        Nd = eval(self.Nd.text())  ### n区掺杂浓度

        Na = eval(self.Na.text())  ### p区掺杂浓度
        ni = eval(self.ni.text())  ### 硅 本征载流子浓度
        np0 = (ni ** 2) / Na  # p区少子浓度
        pn0 = (ni ** 2) / Nd  # n区少子浓度

        e = 1.6 * (10 ** (-19))  # 电子电量
        es = eval(self.es.text())  # 介电常数 cm
        Vt = 0.0259  # Vt = 0.0259v

        Va = eval(self.Va.text())
        # Va = -0.5  ### 反偏电压 负数为正偏电压

        Vbi = Vt * np.log(Na * Nd / (ni ** 2))  # 内建电场
        Vtotal = Vbi + Va  # 总电压

        Xp = np.sqrt((2 * es * Vtotal / e) * (Nd / Na) * (1 / (Na + Nd)))  # p区内建宽度
        Xn = np.sqrt((2 * es * Vtotal / e) * (Na / Nd) * (1 / (Na + Nd)))  # n区内建宽度

        Dn = eval(self.Dn.text())
        Dp = eval(self.Dp.text())
        tn0 = eval(self.tn0.text())
        tp0 = eval(self.tp0.text())
        Ln = np.sqrt(tn0 * Dn)
        Lp = np.sqrt(tp0 * Dp)
        # 以上 公共数据

        # pnx 正偏条件下pn结内部的稳态少子浓度
        Xpnx = np.linspace(Xn, 0.011, 100)
        Xnpx = np.linspace(-0.011, -Xp, 100)
        pnx = pn0 * (np.exp((-Va) / 0.0259) - 1) * (np.exp((Xn - Xpnx) / Lp)) + pn0
        npx = np0 * (np.exp((-Va) / 0.0259) - 1) * (np.exp((Xp + Xnpx) / Ln)) + np0

        # pnx 正偏条件下pn结内部的稳态少子浓度
        plt.plot(Xnpx, npx, '+', label='P区' + str(self.i))
        plt.plot(Xpnx, pnx, linestyle='-', linewidth='3', label='N区' + str(self.i))
        self.i = self.i + 1
        plt.title('正偏条件下pn结内部的稳态少子浓度', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))

        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('位置', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('浓度', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))
        # 绘图
        self.canvas.draw()

    # 正式测试
    def Draw(self):
        self.cal()
        if self.Ge_2.isChecked() == True:
            self.DrawQp()
        elif self.Ge_3.isChecked() == True:
            self.DrawEp()
        elif self.Ge_4.isChecked() == True:
            self.DrawPp()
        elif self.Ge_5.isChecked() == True:
            self.DrawIV()
        elif self.Ge_6.isChecked() == True:
            self.DrawND()
        elif self.Ge_7.isChecked() == True:
            self.Drawpnx()
        elif self.Ge_8.isChecked() == True:
            self.DrawIVDS()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()
