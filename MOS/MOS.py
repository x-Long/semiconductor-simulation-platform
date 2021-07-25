import os

from UI_MOS import Ui_Form
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
        self.Ag.toggled.connect(self.materInput1)
        self.Al.toggled.connect(self.materInput1)
        self.An.toggled.connect(self.materInput1)

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
            self.XX.setText('4.01')

        elif self.GaAs.isChecked() == True:
            self.Eg.setText('1.42')
            self.ni.setText('1.8 * (10 ** 6)')
            self.es.setText('11.7 * 8.85 * 10 ** (-14)')
            self.XX.setText('4.07')


        elif self.Ge.isChecked() == True:
            self.Eg.setText('0.66')
            self.ni.setText('2.4 * (10 ** 13)')
            self.es.setText('16.0 * 8.85 * 10 ** (-14)')
            self.XX.setText('4.13')

        # 根据材料 填写数据

    def materInput1(self):
        if self.Al.isChecked() == True:
            self.Qm.setText('4.28')

        elif self.Ag.isChecked() == True:
            self.Qm.setText('4.26')

        elif self.An.isChecked() == True:
            self.Qm.setText('5.1')

    # 计算的代码
    def cal(self):
        if self.P.isChecked() == True:
            self.tabWidget_3.setCurrentWidget(self.PCD)
            # 根据材料
            ni = eval(self.ni.text())
            Eg = eval(self.Eg.text())
            Qm = eval(self.Qm.text())  # 金属功函数
            XX = eval(self.XX.text())  # 亲和能

            # 定值
            e = 1.6 * (10 ** (-19))
            eox = 3.9 * 8.85 * 10 ** (-14)
            es = eval(self.es.text())
            Vt = 0.0259

            # 获取
            Qss = eval(self.Qss.text())
            tox = eval(self.tox.text())

            Na = eval(self.NN.text())
            # Na = 10 ** 15

            Qfp = Vt * np.log(Na / ni)

            Xdt = np.sqrt(4 * es * Qfp / (e * Na))

            Qsdmax = e * Na * Xdt
            Qms = (Qm - (XX + Eg / 2 + Qfp))
            VTN = (Qsdmax - Qss * e) * tox / eox + Qms + 2 * Qfp

            self.Qfn_2.setText(str(Qfp))
            self.Xdt_2.setText(str(Xdt))
            self.Qsdmax_2.setText(str(Qsdmax))
            self.Qms_2.setText(str(Qms))
            self.VTP_2.setText(str(VTN))
        else:
            self.tabWidget_3.setCurrentWidget(self.NCD)
            # 根据材料
            ni = eval(self.ni.text())
            Eg = eval(self.Eg.text())
            Qm = eval(self.Qm.text())  # 金属功函数
            XX = eval(self.XX.text())  # 亲和能

            # 定值
            e = 1.6 * (10 ** (-19))
            eox = 3.9 * 8.85 * 10 ** (-14)
            es = eval(self.es.text())
            Vt = 0.0259

            # 获取
            Qss = eval(self.Qss.text())
            tox = eval(self.tox.text())

            Nd = eval(self.NN.text())
            # Na = 10 ** 15

            Qfn = Vt * np.log(Nd / ni)
            Xdt = np.sqrt(4 * es * Qfn / (e * Nd))
            Qsdmax = e * Nd * Xdt
            Qms = (Qm - (XX + Eg / 2 - Qfn))
            VTP = (-Qsdmax - Qss * e) * tox / eox + Qms - 2 * Qfn

            self.Qfn.setText(str(Qfn))
            self.Xdt.setText(str(Xdt))
            self.Qsdmax.setText(str(Qsdmax))
            self.Qms.setText(str(Qms))
            self.VTP.setText(str(VTP))

    # n沟道 p衬底
    # VTN 与掺杂浓度的关系 在不同Qss下
    def DrawVTN(self):
        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        Na = np.linspace(10 ** 14, 10 ** 18, 50)
        # Na = 10 ** 15

        # 以上 公共数据

        Qfp = Vt * np.log(Na / ni)
        Xdt = np.sqrt(4 * es * Qfp / (e * Na))
        Qsdmax = e * Na * Xdt
        Qms = (Qm - (XX + Eg / 2 + Qfp))
        VTN = (Qsdmax - Qss * e) * tox / eox + Qms + 2 * Qfp

        plt.plot(np.log10(Na), VTN, ':.', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('n沟道MOSFET阈值电压与掺杂浓度的关系', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('掺杂浓度Na（10^x/cm^3）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('阈值电压Vtn（v）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # p沟道 n衬底
    # VTP 与掺杂浓度的关系 在不同Qss下
    def DrawVTP(self):
        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        Nd = np.linspace(10 ** 14, 10 ** 18, 50)
        # Nd = 10 ** 15

        # 以上 公共数据

        Qfn = Vt * np.log(Nd / ni)
        Xdt = np.sqrt(4 * es * Qfn / (e * Nd))
        Qsdmax = e * Nd * Xdt
        Qms = (Qm - (XX + Eg / 2 - Qfn))
        VTP = (-Qsdmax - Qss * e) * tox / eox + Qms - 2 * Qfn

        plt.plot(np.log10(Nd), VTP, ':.', linewidth='2', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('p沟道MOSFET阈值电压与掺杂浓度的关系', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('掺杂浓度Nd（10^x/cm^3）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('阈值电压Vtp（v）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # Xdt 与掺杂浓度的关系 （Na Nd 应该都行）
    # 绑定后 直接触发即可
    def DrawXdt(self):
        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        Na = np.linspace(10 ** 14, 10 ** 18, 50)
        # Na = 10 ** 15

        # 以上 公共数据

        Qfp = Vt * np.log(Na / ni)
        Xdt = np.sqrt(4 * es * Qfp / (e * Na))

        plt.plot(np.log10(Na), np.log10(Xdt), '--p', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('最大空间电荷区宽度与掺杂浓度的关系', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('掺杂浓度N（10^x/cm^3）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('最大空间电荷区宽度Xdt（10^y cm）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # 上方不用获取掺杂
    # 电子反型电荷密度  掺杂浓度需要获取 Na与 Nd  浓度是获取的定值
    # 没有采用对数坐标，所以不是书上的直线
    # 绑定后 获取浓度 然后触发 不用管p型或n型
    # NS 原本横坐标应加上2Qfp
    def DrawNS(self):

        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        # Nd = np.linspace(10 ** 14, 10 ** 18, 100)
        Nd = eval(self.NN.text())

        # 以上 公共数据

        Qfn = Vt * np.log(Nd / ni)

        nsx = np.linspace(0.01, 0.12, 20)
        nst = ni * np.exp(Qfn / Vt)
        ns = nst * np.exp(nsx / Vt)

        plt.plot(nsx, ns, '--s', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('电子反型电荷密度与表面电势的关系', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('表面电势(v)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电子反型电荷密度ns(cm^-3)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # 对数坐标
    def DrawNSDS(self):

        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        # Nd = np.linspace(10 ** 14, 10 ** 18, 100)
        Nd = eval(self.NN.text())

        # 以上 公共数据

        Qfn = Vt * np.log(Nd / ni)

        nsx = np.linspace(0.01, 0.12, 20)
        nst = ni * np.exp(Qfn / Vt)
        ns = nst * np.exp(nsx / Vt)

        plt.plot(nsx, np.log10(ns), '--s', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('电子反型电荷密度与表面电势的关系', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('表面电势(v)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('电子反型电荷密度log10(ns)(cm^-3)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # 左边衬底选择（n型 p型）右边掺杂浓度  需要获取掺杂浓度
    # 输出特性曲线
    # 书上只有n沟道 p衬底
    # SC 先检测是否为 p衬底 然后在调用
    def DrawSC(self):
        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        # 获取
        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        # Na = np.linspace(10 ** 14, 10 ** 18, 100)
        Na = eval(self.NN.text())

        # 以上 公共数据

        #  专有获取
        L = eval(self.L.text())
        W = eval(self.W.text())
        Un = 650  # 其实是定值
        VGS = self.VGS.value()

        # 计算Cox
        Cox = eox / tox

        # 计算阈值电压
        Qfp = Vt * np.log(Na / ni)
        Xdt = np.sqrt(4 * es * Qfp / (e * Na))
        Qsdmax = e * Na * Xdt
        Qms = (Qm - (XX + Eg / 2 + Qfp))
        VTN = (Qsdmax - Qss * e) * tox / eox + Qms + 2 * Qfp

        # 调整坐标轴，与外围框线
        # ax = plt.gca()
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        # ax.spines['bottom'].set_position(('data', 0))
        # ax.spines['left'].set_position(('data', 0))

        # 绘图
        # 输入 输出
        x = VGS - VTN
        VDS = np.linspace(0, x, 100)
        ID = (W * Un * Cox) / (2 * L) * (2 * (VGS - VTN) * VDS - VDS ** 2)

        # 后边饱和区
        VDS1 = np.linspace(x, 10, 100)
        ID1 = (W * Un * Cox) / (2 * L) * ((VGS - VTN) ** 2) + VDS1 - VDS1

        plt.plot(VDS, ID * 10 ** 3, label='VDS=' + str(VGS) + "V")
        plt.plot(VDS1, ID1 * 10 ** 3, "b:")
        self.i = self.i + 1

        plt.title('n沟道耗尽型MOSFET的I-V特性曲线簇', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('VDS(v)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('ID（mA）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # 书上只有n沟道 p衬底
    # ZY 转移曲线
    def DrawZY(self):
        # 根据材料
        ni = eval(self.ni.text())
        Eg = eval(self.Eg.text())
        Qm = eval(self.Qm.text())  # 金属功函数
        XX = eval(self.XX.text())  # 亲和能

        # 定值
        e = 1.6 * (10 ** (-19))
        eox = 3.9 * 8.85 * 10 ** (-14)
        es = eval(self.es.text())
        Vt = 0.0259

        Qss = eval(self.Qss.text())
        tox = eval(self.tox.text())

        # Nd = np.linspace(10 ** 14, 10 ** 18, 100)
        Na = eval(self.NN.text())

        # 以上 公共数据

        #  专有获取
        L = eval(self.L.text())
        W = eval(self.W.text())
        Un = 650  # 其实是定值
        VGS = self.VGS.value()

        # 计算Cox
        Cox = eox / tox

        # 计算阈值电压
        Qfp = Vt * np.log(Na / ni)
        Xdt = np.sqrt(4 * es * Qfp / (e * Na))
        Qsdmax = e * Na * Xdt
        Qms = (Qm - (XX + Eg / 2 + Qfp))
        VTN = (Qsdmax - Qss * e) * tox / eox + Qms + 2 * Qfp

        # 调整坐标轴，与外围框线
        # ax = plt.gca()
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        # ax.spines['bottom'].set_position(('data', 0))
        # ax.spines['left'].set_position(('data', 0))

        # 绘图
        # 转移曲线
        VGS = np.linspace(VTN, 5, 50)
        ID1 = (W * Un * Cox) / (2 * L) * (VGS - VTN) ** 2
        plt.plot(VGS, ID1 * 10 ** 3, '--+', linewidth='1', label='仿真' + str(self.i))
        self.i = self.i + 1

        plt.title('n沟道耗尽型MOSFET的转移特性曲线', fontsize='15', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.3))
        plt.legend(loc='best', ncol=2)  # 设置图例
        plt.xlabel('VGS(v)', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))  # xy描述
        plt.ylabel('ID（mA）', fontsize='12', bbox=dict(facecolor='b', edgecolor='blue', alpha=0.1))

        # 绘图
        self.canvas.draw()

    # 正式测试
    def Draw(self):
        self.cal()
        if self.Ge_2.isChecked() == True:
            self.DrawVTN()
        elif self.Ge_3.isChecked() == True:
            self.DrawVTP()
        elif self.Ge_4.isChecked() == True:
            self.DrawXdt()
        elif self.Ge_5.isChecked() == True:
            self.DrawNS()
        elif self.Ge_6.isChecked() == True:
            self.DrawSC()
        elif self.Ge_7.isChecked() == True:
            self.DrawZY()
        elif self.Ge_8.isChecked() == True:
            self.DrawNSDS()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()
