### Main Introduction
# Name: T2DM Follow-up Time Judgment System_Version_0.2_alpha_10102158
# #Developer: 1st_GuLifan; 2nd_DongRuiQing; Leader: QiangWei
# Organization: The First Affiliated Hospital of Xi'an Jiaotong University
# Checking time: 2024.10.10_2nd
# Status: NOT reviewed
""""""
import os
from tkinter import messagebox
from datetime import datetime, timedelta
import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
# import tkinter as tk
# from pytkUI.widgets import *
today = datetime.today().date() # 获取今日日期
### Import Layouts 导入布局文件
class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="flatly", hdpi=False) # 蓝色基调的主题是 cosmo，可以改
        self.__win()
        self.tk_label_frame_lbf_left = self.__tk_label_frame_lbf_left(self)
        self.tk_label_lbl_id = self.__tk_label_lbl_id(self.tk_label_frame_lbf_left)
        self.tk_input_inp_id = self.__tk_input_inp_id(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_sex = self.__tk_label_lbl_sex(self.tk_label_frame_lbf_left)
        self.tk_select_box_slb_sex = self.__tk_select_box_slb_sex(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_age = self.__tk_label_lbl_age(self.tk_label_frame_lbf_left)
        self.tk_input_inp_age = self.__tk_input_inp_age(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_department = self.__tk_label_lbl_department(self.tk_label_frame_lbf_left)
        self.tk_select_box_slb_department = self.__tk_select_box_slb_department(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_operator = self.__tk_label_lbl_operator(self.tk_label_frame_lbf_left)
        self.tk_select_box_slb_operator = self.__tk_select_box_slb_operator(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_data = self.__tk_label_lbl_data(self.tk_label_frame_lbf_left)
        self.tb_date_input_dip_date = self.__tb_date_input_dip_date(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_course = self.__tk_label_lbl_course(self.tk_label_frame_lbf_left)
        self.tk_select_box_slb_course = self.__tk_select_box_slb_course(self.tk_label_frame_lbf_left)
        self.tk_label_lbl_copyright = self.__tk_label_lbl_copyright(self)
        self.tk_tabs_tab_main = self.__tk_tabs_tab_main(self)
        self.tk_label_frame_lbf_body = self.__tk_label_frame_lbf_body(self.tk_tabs_tab_main_0)
        self.tk_label_lbl_height = self.__tk_label_lbl_height(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_sbp = self.__tk_label_lbl_sbp(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_weight = self.__tk_label_lbl_weight(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_dbp = self.__tk_label_lbl_dbp(self.tk_label_frame_lbf_body)
        self.tk_input_inp_height = self.__tk_input_inp_height(self.tk_label_frame_lbf_body)
        self.tk_input_inp_sbp = self.__tk_input_inp_sbp(self.tk_label_frame_lbf_body)
        self.tk_input_inp_weight = self.__tk_input_inp_weight(self.tk_label_frame_lbf_body)
        self.tk_input_inp_dbp = self.__tk_input_inp_dbp(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_bmi = self.__tk_label_lbl_bmi(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_bp = self.__tk_label_lbl_bp(self.tk_label_frame_lbf_body)
        self.tk_select_box_slb_bmi = self.__tk_select_box_slb_bmi(self.tk_label_frame_lbf_body)
        self.tk_select_box_slb_bp = self.__tk_select_box_slb_bp(self.tk_label_frame_lbf_body)
        self.tk_label_lbl_waistline = self.__tk_label_lbl_waistline(self.tk_label_frame_lbf_body)
        self.tk_input_inp_waistline = self.__tk_input_inp_waistline(self.tk_label_frame_lbf_body)
        self.tk_label_frame_lbf_blood = self.__tk_label_frame_lbf_blood(self.tk_tabs_tab_main_0)
        self.tk_label_lbl_hba1c = self.__tk_label_lbl_hba1c(self.tk_label_frame_lbf_blood)
        self.tk_input_inp_hba1c = self.__tk_input_inp_hba1c(self.tk_label_frame_lbf_blood)
        self.tk_label_lbl_bl = self.__tk_label_lbl_bl(self.tk_label_frame_lbf_blood)
        self.tk_input_inp_ldlc = self.__tk_input_inp_ldlc(self.tk_label_frame_lbf_blood)
        self.tk_label_lbl_ldlc = self.__tk_label_lbl_ldlc(self.tk_label_frame_lbf_blood)
        self.tk_label_lbl_tc = self.__tk_label_lbl_tc(self.tk_label_frame_lbf_blood)
        self.tk_input_inp_tc = self.__tk_input_inp_tc(self.tk_label_frame_lbf_blood)
        self.tk_label_lbl_bs = self.__tk_label_lbl_bs(self.tk_label_frame_lbf_blood)
        self.tk_select_box_slb_hd = self.__tk_select_box_slb_hd(self.tk_label_frame_lbf_blood)
        self.tk_label_lbl_bld = self.__tk_label_lbl_bld(self.tk_label_frame_lbf_blood)
        self.tk_label_frame_lbf_cn = self.__tk_label_frame_lbf_cn(self.tk_tabs_tab_main_0)
        self.tk_label_lbl_egfr = self.__tk_label_lbl_egfr(self.tk_label_frame_lbf_cn)
        self.tk_select_box_slb_egfr = self.__tk_select_box_slb_egfr(self.tk_label_frame_lbf_cn)
        self.tk_label_lbl_uacr = self.__tk_label_lbl_uacr(self.tk_label_frame_lbf_cn)
        self.tk_select_box_slb_uacr = self.__tk_select_box_slb_uacr(self.tk_label_frame_lbf_cn)
        self.tk_label_lbl_dn = self.__tk_label_lbl_dn(self.tk_label_frame_lbf_cn)
        self.tk_label_lbl_dr = self.__tk_label_lbl_dr(self.tk_label_frame_lbf_cn)
        self.tk_select_box_slb_dr = self.__tk_select_box_slb_dr(self.tk_label_frame_lbf_cn)
        self.tk_label_lbl_dns = self.__tk_label_lbl_dns(self.tk_label_frame_lbf_cn)
        self.tk_select_box_slb_dns = self.__tk_select_box_slb_dns(self.tk_label_frame_lbf_cn)
        self.tk_text_txt_allresult = self.__tk_text_txt_allresult(self.tk_tabs_tab_main_0)
        self.tk_frame_tkf_btn = self.__tk_frame_tkf_btn(self)
        self.tk_button_btn_cannel = self.__tk_button_btn_cannel(self.tk_frame_tkf_btn)
        self.tk_button_btn_confirm = self.__tk_button_btn_confirm(self.tk_frame_tkf_btn)
        self.tk_button_btn_print = self.__tk_button_btn_print(self.tk_frame_tkf_btn)
        # def __init__(self, parent):
    def __win(self):
        """
        初始化窗口标题和窗口属性
        """
        self.title("T2DM Follow-up Time Judgment System (for Aldut)_Version_1.0_beta_10102205")
        # 设置窗口标题

        # 设置窗口大小、居中
        width = 900  # 窗口宽度
        height = 700  # 窗口高度
        screenwidth = self.winfo_screenwidth()  # 获取屏幕宽度
        screenheight = self.winfo_screenheight()  # 获取屏幕高度
        # 计算窗口居中位置
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)  # 设置窗口大小和位置
        self.resizable(width=False, height=False)  # 禁止调整窗口大小
    def scrollbar_autohide(self, vbar, hbar, widget):
        """
        自动隐藏滚动条功能
        :param vbar: 垂直滚动条对象
        :param hbar: 水平滚动条对象
        :param widget: 关联的widget组件
        """
        def show():
            """显示滚动条"""
            if vbar:
                vbar.lift(widget)  # 提升垂直滚动条使其可见
            if hbar:
                hbar.lift(widget)  # 提升水平滚动条使其可见
        def hide():
            """隐藏滚动条"""
            if vbar:
                vbar.lower(widget)  # 降低垂直滚动条使其不可见
            if hbar:
                hbar.lower(widget)  # 降低水平滚动条使其不可见
        hide()  # 初始时隐藏滚动条
        # 绑定事件来显示或隐藏滚动条
        widget.bind("<Enter>", lambda e: show())  # 鼠标进入widget时显示滚动条
        if vbar:
            vbar.bind("<Enter>", lambda e: show())  # 鼠标进入垂直滚动条时显示滚动条
            vbar.bind("<Leave>", lambda e: hide())  # 鼠标离开垂直滚动条时隐藏滚动条
        if hbar:
            hbar.bind("<Enter>", lambda e: show())  # 鼠标进入水平滚动条时显示滚动条
            hbar.bind("<Leave>", lambda e: hide())  # 鼠标离开水平滚动条时隐藏滚动条
        widget.bind("<Leave>", lambda e: hide())  # 鼠标离开widget时隐藏滚动条
    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        """
        配置垂直滚动条
        :param vbar: 垂直滚动条对象
        :param widget: 关联的widget组件
        :param x, y, w, h: 滚动条相对于widget的位置和大小
        :param pw, ph: widget的父容器的大小
        """
        widget.configure(yscrollcommand=vbar.set)  # 将widget的垂直滚动事件绑定到滚动条
        vbar.config(command=widget.yview)  # 将滚动条的滚动事件绑定到widget
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')  # 放置滚动条
    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)  # 将widget的水平滚动事件绑定到滚动条
        hbar.config(command=widget.xview)  # 将滚动条的滚动事件绑定到widget
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')  # 放置滚动条
    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)  # 创建垂直滚动条
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)  # 配置垂直滚动条
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")  # 创建水平滚动条
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)  # 配置水平滚动条
        self.scrollbar_autohide(vbar, hbar, widget)  # 应用自动隐藏滚动条功能
    def new_style(self, widget):
        """
        为widget组件生成并应用新的随机样式名
        :param widget: 要应用新样式的widget组件
        :return: 新生成的样式名
        """
        ctl = widget.cget('style')  # 获取widget当前的样式名
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl  # 生成新的随机样式名
        widget.configure(style=ctl)  # 应用新样式名到widget
        return ctl  # 返回新样式名
    # 定义一个私有方法，用于创建一个包含基本信息的LabelFrame
    def __tk_label_frame_lbf_left(self, parent):
        frame = LabelFrame(parent, text="基本信息 Information",
                           bootstyle="default")  # 创建一个LabelFrame，标题为"基本信息 Information"
        frame.place(x=5, y=5, width=140, height=660)  # 设置LabelFrame的位置和大小
        return frame  # 返回创建的LabelFrame对象
    # 定义一个私有方法，用于创建一个显示"患者标识 Patient ID"的标签
    def __tk_label_lbl_id(self, parent):
        label = Label(parent, text="患者标识 Patient ID", anchor="center",
                      bootstyle="default")  # 创建一个标签，文本为"患者标识 Patient ID"
        label.place(x=5, y=10, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个输入患者标识的输入框
    def __tk_input_inp_id(self, parent):
        ipt = Entry(parent, bootstyle="default")  # 创建一个输入框
        ipt.place(x=5, y=45, width=130, height=30)  # 设置输入框的位置和大小
        return ipt  # 返回创建的输入框对象
    # 定义一个私有方法，用于创建一个显示"患者性别 Patient Sex"的标签
    def __tk_label_lbl_sex(self, parent):
        label = Label(parent, text="患者性别 Patient Sex", anchor="center",
                      bootstyle="default")  # 创建一个标签，文本为"患者性别 Patient Sex"
        label.place(x=5, y=80, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个选择患者性别的下拉框
    def __tk_select_box_slb_sex(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")  # 创建一个只读的下拉框
        cb['values'] = ("男性 Male", "女性 Female")  # 设置下拉框的选项
        cb.current(0)  # 设置默认选中的选项
        cb.place(x=5, y=115, width=130, height=30)  # 设置下拉框的位置和大小
        return cb  # 返回创建的下拉框对象
    # 定义一个私有方法，用于创建一个显示"患者年龄 Patient Age"的标签
    def __tk_label_lbl_age(self, parent):
        label = Label(parent, text="患者年龄 Patient Age", anchor="center",
                      bootstyle="default")  # 创建一个标签，文本为"患者年龄 Patient Age"
        label.place(x=5, y=150, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个输入患者年龄的输入框
    def __tk_input_inp_age(self, parent):
        ipt = Entry(parent, bootstyle="default")  # 创建一个输入框
        ipt.place(x=5, y=185, width=130, height=30)  # 设置输入框的位置和大小
        return ipt  # 返回创建的输入框对象
    # 定义一个私有方法，用于创建一个显示"科室 Department"的标签
    def __tk_label_lbl_department(self, parent):
        label = Label(parent, text="科室 Department", anchor="center",
                      bootstyle="default")  # 创建一个标签，文本为"科室 Department"
        label.place(x=5, y=385, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个选择科室的下拉框
    def __tk_select_box_slb_department(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="secondary")  # 创建一个只读的下拉框，样式为"secondary"
        cb['values'] = ("内分泌风湿免疫", "admin")  # 设置下拉框的选项
        cb.current(0)  # 设置默认选中的选项
        cb.place(x=5, y=420, width=130, height=30)  # 设置下拉框的位置和大小
        return cb  # 返回创建的下拉框对象
    # 定义一个私有方法，用于创建一个显示"操作人 Operator"的标签
    def __tk_label_lbl_operator(self, parent):
        label = Label(parent, text="操作人 Operator", anchor="center",
                      bootstyle="default")  # 创建一个标签，文本为"操作人 Operator"
        label.place(x=5, y=455, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个选择操作人的下拉框
    def __tk_select_box_slb_operator(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")  # 创建一个只读的下拉框
        cb['values'] = ("Dr.DongRQ", "Ug.GuLF", "Dr.QiangW")  # 设置下拉框的选项
        cb.current(0)  # 设置默认选中的选项
        cb.place(x=5, y=490, width=130, height=30)  # 设置下拉框的位置和大小
        return cb  # 返回创建的下拉框对象
    # 定义一个私有方法，用于创建一个显示"操作日期 Date"的标签
    def __tk_label_lbl_data(self, parent):
        label = Label(parent, text="操作日期 Date", anchor="center", bootstyle="default")  # 创建一个标签，文本为"操作日期 Date"
        label.place(x=5, y=525, width=130, height=30)  # 设置标签的位置和大小
        return label  # 返回创建的标签对象
    # 定义一个私有方法，用于创建一个输入操作日期的日期输入框
    def __tb_date_input_dip_date(self, parent):
        ipt = DateEntry(parent, width=1, bootstyle="primary")  # 创建一个日期输入框，样式为"primary"
        ipt.place(x=5, y=560, width=130, height=30)  # 设置日期输入框的位置和大小
        return ipt  # 返回创建的日期输入框对象
    # 定义一个私有方法，用于创建一个标签，显示“病程 Course of DM”
    def __tk_label_lbl_course(self, parent):
        # 创建一个标签，设置其父组件、文本内容、对齐方式和样式
        label = Label(parent, text="病程 Course of DM", anchor="center", bootstyle="default")
        # 放置标签，设置其位置、宽度和高度
        label.place(x=5, y=220, width=130, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建一个下拉选择框，用于选择病程
    def __tk_select_box_slb_course(self, parent):
        # 创建一个下拉选择框，设置其父组件、状态为只读和样式
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的选项值
        cb['values'] = (" ≤ 5 yr", "5-10 yr", "10-20 yr", "≥ 20 yr")
        # 设置默认选中的选项（第一个选项）
        cb.current(0)
        # 放置下拉选择框，设置其位置、宽度和高度
        cb.place(x=5, y=255, width=130, height=30)
        # 返回创建的下拉选择框对象
        return cb
    # 定义一个私有方法，用于创建一个标签，显示版权信息
    def __tk_label_lbl_copyright(self, parent):
        # 创建一个标签，设置其父组件、文本内容（版权信息）、对齐方式和样式
        label = Label(parent,
                      text="©2024 The First Affiliated Hospital of Xi'an Jiaotong University. All Rights Reserved.",
                      anchor="center", bootstyle="default")
        # 放置标签，设置其位置、宽度和高度
        label.place(x=150, y=670, width=600, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建一个包含标签页的笔记本组件（总览 Overview）
    def __tk_tabs_tab_main(self, parent):
        # 创建一个笔记本组件，设置其父组件
        frame = Notebook(parent)
        # 调用另一个私有方法，创建第一个标签页，并将其添加到笔记本组件中
        self.tk_tabs_tab_main_0 = self.__tk_frame_tab_main_0(frame)
        frame.add(self.tk_tabs_tab_main_0, text=" 总览 Overview ")
        # 放置笔记本组件，设置其位置、宽度和高度
        frame.place(x=155, y=10, width=740, height=600)
        # 返回创建的笔记本组件对象
        return frame
    # 定义一个私有方法，用于创建笔记本组件中的第一个标签页（框架）
    def __tk_frame_tab_main_0(self, parent):
        # 创建一个框架，设置其父组件（即笔记本组件）
        frame = Frame(parent)
        # 放置框架（虽然这里放置的位置和大小与笔记本组件重复，但通常是为了内部布局）
        # 实际上，如果框架是作为笔记本的一部分，通常不需要再次放置
        frame.place(x=155, y=10, width=740, height=600)
        # 返回创建的框架对象
        return frame
    # 定义一个私有方法，用于创建一个带有文本的标签框架，用于显示BMI和血压信息
    def __tk_label_frame_lbf_body(self, parent):
        # 创建一个标签框架，设置其父组件、文本标题和样式
        frame = LabelFrame(parent, text="BMI and blood pressure ", bootstyle="dark")
        # 放置标签框架，设置其位置、宽度和高度
        frame.place(x=5, y=10, width=730, height=150)
        # 返回创建的标签框架对象
        return frame
    # 定义一个私有方法，用于创建并返回一个显示“身高”的标签
    def __tk_label_lbl_height(self, parent):
        # 创建标签，父容器为parent，文本为“身高 (Height) /cm”，对齐方式为居中，样式为默认
        label = Label(parent, text="身高 (Height) /cm", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=10, y=10)，宽度150，高度30
        label.place(x=10, y=10, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个显示“收缩压”的标签
    def __tk_label_lbl_sbp(self, parent):
        # 创建标签，父容器为parent，文本为“收缩压 (S BP)/mmHg”，对齐方式为居中，样式为默认
        label = Label(parent, text="收缩压 (S BP)/mmHg", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=10, y=50)，宽度150，高度30
        label.place(x=10, y=50, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个显示“体重”的标签
    def __tk_label_lbl_weight(self, parent):
        # 创建标签，父容器为parent，文本为“体重 (Weight)/Kg”，对齐方式为居中，样式为默认
        label = Label(parent, text="体重 (Weight)/Kg", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=230, y=10)，宽度150，高度30
        label.place(x=230, y=10, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个显示“舒张压”的标签
    def __tk_label_lbl_dbp(self, parent):
        # 创建标签，父容器为parent，文本为“舒张压 (D BP)/mmHg”，对齐方式为居中，样式为默认
        label = Label(parent, text="舒张压 (D BP)/mmHg", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=230, y=50)，宽度150，高度30
        label.place(x=230, y=50, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于输入身高的输入框
    def __tk_input_inp_height(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=170, y=10)，宽度50，高度30
        ipt.place(x=170, y=10, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个用于输入收缩压的输入框
    def __tk_input_inp_sbp(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=170, y=50)，宽度50，高度30
        ipt.place(x=170, y=50, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个用于输入体重的输入框
    def __tk_input_inp_weight(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=390, y=10)，宽度50，高度30
        ipt.place(x=390, y=10, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个用于输入舒张压的输入框
    def __tk_input_inp_dbp(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=390, y=50)，宽度50，高度30
        ipt.place(x=390, y=50, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个显示“BMI”的标签
    def __tk_label_lbl_bmi(self, parent):
        # 创建标签，父容器为parent，文本为“BMI”，对齐方式为居中，样式为浅色反转
        label = Label(parent, text="BMI", anchor="center", bootstyle="light inverse")
        # 放置标签，位置为(x=450, y=10)，宽度150，高度30
        label.place(x=450, y=10, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个显示“血压范围”的标签
    def __tk_label_lbl_bp(self, parent):
        # 创建标签，父容器为parent，文本为“血压范围 (BP Range)”，对齐方式为居中，样式为浅色反转
        label = Label(parent, text="血压范围 (BP Range)", anchor="center", bootstyle="light inverse")
        # 放置标签，位置为(x=450, y=50)，宽度150，高度30
        label.place(x=450, y=50, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于选择BMI值的下拉选择框
    def __tk_select_box_slb_bmi(self, parent):
        # 创建下拉选择框，父容器为parent，状态为只读，样式为默认
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的选项值
        cb['values'] = ("请输入左侧数值", "＜18.5低体重", "18.5-23.9正常", "23.9-27.9超重", "≥28.0 肥胖")
        # 设置默认选中的选项为第一个
        cb.current(0)
        # 放置下拉选择框，位置为(x=610, y=10)，宽度110，高度30
        cb.place(x=610, y=10, width=110, height=30)
        # 返回创建的下拉选择框对象
        return cb
    # 定义一个私有方法，用于创建并返回一个用于选择血压范围的下拉选择框
    def __tk_select_box_slb_bp(self, parent):
        # 创建下拉选择框，父容器为parent，状态为只读，样式为默认
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的选项值，包含多个血压范围
        cb['values'] = ("请输入左侧数值", "＜120//＜80正常血压", "120-139//80-89正常高值血压", "140-159//90-99轻度高血压",
                        "160-179//100-109中度高血压", "≥180//≥110重度高血压")
        # 设置默认选中的选项为第一个
        cb.current(0)
        # 放置下拉选择框，位置为(x=610, y=50)，宽度110，高度30
        cb.place(x=610, y=50, width=110, height=30)
        # 返回创建的下拉选择框对象
        return cb
    # 定义一个私有方法，用于创建并返回一个显示“腰围”的标签
    def __tk_label_lbl_waistline(self, parent):
        # 创建标签，父容器为parent，文本为“腰围 (Waistline)/cm”，对齐方式为居中，样式为浅色反转
        label = Label(parent, text="腰围 (Waistline)/cm", anchor="center", bootstyle="light inverse")
        # 放置标签，位置为(x=10, y=90)，宽度150，高度30
        label.place(x=10, y=90, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于输入腰围的输入框
    def __tk_input_inp_waistline(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=170, y=90)，宽度50，高度30
        ipt.place(x=170, y=90, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个显示“Blood indicators”的标签框
    def __tk_label_frame_lbf_blood(self, parent):
        # 创建标签框，父容器为parent，文本为“Blood indicators”，样式为深色
        frame = LabelFrame(parent, text="Blood indicators", bootstyle="dark")
        # 放置标签框，位置为(x=5, y=170)，宽度730，高度150
        frame.place(x=5, y=170, width=730, height=150)
        # 返回创建的标签框对象
        return frame
    # 定义一个私有方法，用于创建并返回一个显示“糖化血红蛋白”的标签
    def __tk_label_lbl_hba1c(self, parent):
        # 创建标签，父容器为parent，文本为“糖化血红蛋白 (HbA1c)mmol/mol”，对齐方式为居中，样式为默认
        label = Label(parent, text="糖化血红蛋白 (HbA1c)mmol/mol", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=170, y=10)，宽度200，高度30
        label.place(x=170, y=10, width=200, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于输入糖化血红蛋白值的输入框
    def __tk_input_inp_hba1c(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=380, y=10)，宽度50，高度30
        ipt.place(x=380, y=10, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个显示“血脂”的标签
    def __tk_label_lbl_bl(self, parent):
        # 创建标签，父容器为parent，文本为“血脂 (Blood Lipids)”，对齐方式为居中，样式为浅色反转
        label = Label(parent, text="血脂 (Blood Lipids)", anchor="center", bootstyle="light inverse")
        # 放置标签，位置为(x=10, y=50)，宽度150，高度30
        label.place(x=10, y=50, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于输入低密度脂蛋白胆固醇值的输入框
    def __tk_input_inp_ldlc(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=380, y=50)，宽度50，高度30
        ipt.place(x=380, y=50, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个显示“低密度脂蛋白胆固醇”的标签
    def __tk_label_lbl_ldlc(self, parent):
        # 创建标签，父容器为parent，文本为“低密度脂蛋白胆固醇(LDL-C)mmol/L”，对齐方式为居中，样式为默认
        label = Label(parent, text="低密度脂蛋白胆固醇(LDL-C)mmol/L", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=170, y=50)，宽度200，高度30
        label.place(x=170, y=50, width=200, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个显示“总胆固醇”的标签
    def __tk_label_lbl_tc(self, parent):
        # 创建标签，父容器为parent，文本为“总胆固醇 (TC)mmol/L”，对齐方式为居中，样式为默认
        label = Label(parent, text="总胆固醇 (TC)mmol/L", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=440, y=50)，宽度200，高度30
        label.place(x=440, y=50, width=200, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于输入总胆固醇值的输入框
    def __tk_input_inp_tc(self, parent):
        # 创建输入框，父容器为parent，样式为默认
        ipt = Entry(parent, bootstyle="default")
        # 放置输入框，位置为(x=650, y=50)，宽度50，高度30
        ipt.place(x=650, y=50, width=50, height=30)
        # 返回创建的输入框对象
        return ipt
    # 定义一个私有方法，用于创建并返回一个显示“血糖”的标签
    def __tk_label_lbl_bs(self, parent):
        # 创建标签，父容器为parent，文本为“血糖 (Blood Sugar)”，对齐方式为居中，样式为浅色反转
        label = Label(parent, text="血糖 (Blood Sugar)", anchor="center", bootstyle="light inverse")
        # 放置标签，位置为(x=10, y=10)，宽度150，高度30
        label.place(x=10, y=10, width=150, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建并返回一个用于选择是否服用降脂药的下拉选择框
    def __tk_select_box_slb_hd(self, parent):
        # 创建下拉选择框，父容器为parent，状态为只读，样式为警告
        cb = Combobox(parent, state="readonly", bootstyle="warning")
        # 设置下拉选择框的选项值
        cb['values'] = ("否 No", "是 Yes")
        # 设置默认选中的选项为第一个
        cb.current(0)
        # 放置下拉选择框，位置为(x=410, y=90)，宽度100，高度30
        cb.place(x=410, y=90, width=100, height=30)
        # 返回创建的下拉选择框对象
        return cb
    # 定义一个私有方法，用于创建并返回一个显示“是否服用降脂药”的标签
    def __tk_label_lbl_bld(self, parent):
        # 创建标签，父容器为parent，文本为“是否服用降脂药 (hypolipidemic drugs?)”，对齐方式为居中，样式为默认
        label = Label(parent, text="是否服用降脂药 (hypolipidemic drugs?)", anchor="center", bootstyle="default")
        # 放置标签，位置为(x=170, y=90)，宽度230，高度30
        label.place(x=170, y=90, width=230, height=30)
        # 返回创建的标签对象
        return label
    # 定义一个私有方法，用于创建一个带有“Complication”标签的LabelFrame（标签框架）
    def __tk_label_frame_lbf_cn(self, parent):
        # 创建一个LabelFrame，父组件为传入的parent，文本为"Complication"，样式为"dark"
        frame = LabelFrame(parent, text="Complication", bootstyle="dark")
        # 放置LabelFrame，设置其位置和大小
        frame.place(x=5, y=330, width=730, height=110)
        # 返回创建的LabelFrame
        return frame
    # 定义一个私有方法，用于创建一个显示“肾小球滤过率 (eGFR)”的标签
    def __tk_label_lbl_egfr(self, parent):
        # 创建一个Label，父组件为传入的parent，文本为"肾小球滤过率 (eGFR)"，对齐方式为居中，样式为"default"
        label = Label(parent, text="肾小球滤过率 (eGFR)", anchor="center", bootstyle="default")
        # 放置Label，设置其位置和大小
        label.place(x=230, y=10, width=130, height=30)
        # 返回创建的Label
        return label
    # 定义一个私有方法，用于创建一个关于eGFR的下拉选择框
    def __tk_select_box_slb_egfr(self, parent):
        # 创建一个Combobox（下拉选择框），父组件为传入的parent，状态为只读，样式为"default"
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的值选项
        cb['values'] = (" ≥ 90 (G1)", "60-89 (G2) ", "45-59 (G3a)", "30-44 (G3b)", "15-29 (G4)", "<15/透析 (G5)")
        # 设置默认选中的值
        cb.current(0)
        # 放置Combobox，设置其位置和大小
        cb.place(x=360, y=10, width=100, height=30)
        # 返回创建的Combobox
        return cb
    # 定义一个私有方法，用于创建一个显示“尿白蛋白与肌酐比(UACR)”的标签
    def __tk_label_lbl_uacr(self, parent):
        # 创建一个Label，父组件为传入的parent，文本为"尿白蛋白与肌酐比(UACR)"，对齐方式为居中，样式为"default"
        label = Label(parent, text="尿白蛋白与肌酐比(UACR)", anchor="center", bootstyle="default")
        # 放置Label，设置其位置和大小
        label.place(x=470, y=10, width=140, height=30)
        # 返回创建的Label
        return label
    # 定义一个私有方法，用于创建一个关于UACR的下拉选择框
    def __tk_select_box_slb_uacr(self, parent):
        # 创建一个Combobox（下拉选择框），父组件为传入的parent，状态为只读，样式为"default"
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的值选项
        cb['values'] = (" < 30 (A1) ", "30-300 (A2)", " > 300 (A3)")
        # 设置默认选中的值
        cb.current(0)
        # 放置Combobox，设置其位置和大小
        cb.place(x=620, y=10, width=100, height=30)
        # 返回创建的Combobox
        return cb
    # 定义一个私有方法，用于创建一个显示“糖尿病肾病(Diabetic Nephropathy)”的标签
    def __tk_label_lbl_dn(self, parent):
        # 创建一个Label，父组件为传入的parent，文本为"糖尿病肾病(Diabetic Nephropathy)"，对齐方式为居中，样式为"light inverse"
        label = Label(parent, text="糖尿病肾病(Diabetic Nephropathy)", anchor="center", bootstyle="light inverse")
        # 放置Label，设置其位置和大小
        label.place(x=10, y=10, width=210, height=30)
        # 返回创建的Label
        return label
    # 定义一个私有方法，用于创建一个显示“视网膜病变(Diabetic Retinopathy)”的标签
    def __tk_label_lbl_dr(self, parent):
        # 创建一个Label，父组件为传入的parent，文本为"视网膜病变(Diabetic Retinopathy)"，对齐方式为居中，样式为"light inverse"
        label = Label(parent, text="视网膜病变(Diabetic Retinopathy)", anchor="center", bootstyle="light inverse")
        # 放置Label，设置其位置和大小
        label.place(x=10, y=50, width=210, height=30)
        # 返回创建的Label
        return label
    # 定义一个私有方法，用于创建一个关于视网膜病变的下拉选择框
    def __tk_select_box_slb_dr(self, parent):
        # 创建一个Combobox（下拉选择框），父组件为传入的parent，状态为只读，样式为"default"
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的值选项
        cb['values'] = ("无DR", "轻度DR", "中度DR", "重度DR")
        # 设置默认选中的值
        cb.current(0)
        # 放置Combobox，设置其位置和大小
        cb.place(x=230, y=50, width=130, height=30)
        # 返回创建的Combobox
        return cb
    # 定义一个私有方法，用于创建一个显示“神经系统病变(Diabetic Neuropathy)”的标签
    def __tk_label_lbl_dns(self, parent):
        # 创建一个Label，父组件为传入的parent，文本为"神经系统病变(Diabetic Neuropathy)"，对齐方式为居中，样式为"light inverse"
        label = Label(parent, text="神经系统病变(Diabetic Neuropathy)", anchor="center", bootstyle="light inverse")
        # 放置Label，设置其位置和大小
        label.place(x=370, y=50, width=220, height=30)
        # 返回创建的Label
        return label
    # 定义一个私有方法，用于创建一个关于神经系统病变的下拉选择框
    def __tk_select_box_slb_dns(self, parent):
        # 创建一个Combobox（下拉选择框），父组件为传入的parent，状态为只读，样式为"default"
        cb = Combobox(parent, state="readonly", bootstyle="default")
        # 设置下拉选择框的值选项
        cb['values'] = ("无", "有")
        # 设置默认选中的值
        cb.current(0)
        # 放置Combobox，设置其位置和大小
        cb.place(x=590, y=50, width=130, height=30)
        # 返回创建的Combobox
        return cb
    # 定义一个私有方法，用于创建一个多行文本输入框
    def __tk_text_txt_allresult(self, parent):
        # 创建一个Text（多行文本输入框），父组件为传入的parent
        text = Text(parent)
        # 放置Text，设置其位置和大小
        text.place(x=5, y=460, width=730, height=100)
        # 返回创建的Text
        return text
    # 定义一个私有方法，用于创建一个Frame（框架），通常用于布局
    def __tk_frame_tkf_btn(self, parent):
        # 创建一个Frame，父组件为传入的parent，样式为"default"
        frame = Frame(parent, bootstyle="default")
        # 放置Frame，设置其位置和大小
        frame.place(x=155, y=620, width=740, height=40)
        # 返回创建的Frame
        return frame
    # 定义一个私有方法，用于创建一个“取消 (Cannel)”按钮
    def __tk_button_btn_cannel(self, parent):
        # 创建一个Button（按钮），父组件为传入的parent，文本为"取消 (Cannel)"，不接收焦点，样式为"secondary"
        btn = Button(parent, text="取消 (Cannel)", takefocus=False, bootstyle="secondary")
        # 放置Button，设置其位置和大小
        btn.place(x=130, y=5, width=150, height=30)
        # 返回创建的Button
        return btn
    # 定义一个私有方法，用于创建一个“确认 (Confirm)”按钮
    def __tk_button_btn_confirm(self, parent):
        # 创建一个Button（按钮），父组件为传入的parent，文本为"确认 (Confirm)"，不接收焦点，样式为"dark"
        btn = Button(parent, text="确认 (Confirm)", takefocus=False, bootstyle="dark")
        # 放置Button，设置其位置和大小
        btn.place(x=330, y=5, width=150, height=30)
        # 返回创建的Button
        return btn
    # 定义一个私有方法，用于创建一个“确认并输出 (Print)”按钮
    def __tk_button_btn_print(self, parent):
        # 创建一个Button（按钮），父组件为传入的parent，文本为"确认并输出 (Print)"，不接收焦点，样式为"default"
        btn = Button(parent, text="确认并输出 (Print)", takefocus=False, bootstyle="default")
        # 放置Button，设置其位置和大小
        btn.place(x=530, y=5, width=200, height=30)
        # 返回创建的Button
        return btn
class MainWin(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_btn_cannel.bind('<Button-1>', self.ctl.cannelall)
        self.tk_button_btn_confirm.bind('<Button-1>', self.ctl.confirmall)
        self.tk_button_btn_print.bind('<Button-1>', self.ctl.printall)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_lbl_id), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_sex), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_age), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_department), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_operator), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_data), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_course), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_copyright), font=("微软雅黑", -10, "underline"))
        sty.configure(self.new_style(self.tk_label_lbl_height), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_sbp), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_weight), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_dbp), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_bmi), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_bp), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_waistline), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_hba1c), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_bl), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_ldlc), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_tc), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_bs), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_egfr), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_uacr), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lbl_dn), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_dr), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_lbl_dns), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_button_btn_cannel), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_btn_confirm), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_btn_print), font=("微软雅黑", -12))
        pass
"""
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
"""
### Import Controllers 导入窗口控制器，已合并，必须保持注释
class Controller:
    ui: WinGUI # 导入UI类后，替换 object 为 Win 类型，获得 IDE 属性提示功能
    def init(self, ui): # 得到UI实例，对组件进行初始化配置
        pass
        self.ui = ui # TODO 组件初始化 赋值操作
    ### 以下为功能函数部分
    # 左键单击确认的效果
    def confirmall(self,evt):
        # 获取患者基本信息和操作基本信息
        patient_id = str(self.ui.tk_input_inp_id.get())
        patient_age = int(self.ui.tk_input_inp_age.get())
        patient_sex = self.ui.tk_select_box_slb_sex.get()
        hp_department = self.ui.tk_select_box_slb_department.get()
        hp_operator = self.ui.tk_select_box_slb_operator.get()
        hp_date = self.ui.tb_date_input_dip_date.entry.get()
        # 注意！
        patient_course = self.ui.tk_select_box_slb_course.get()
        # 假设 self.ui.tk_select_box_slb_course 是一个 ttk.Combobox,获取索引值
        course_values = self.ui.tk_select_box_slb_course['values']  # 获取所有值
        course_index_3 = course_values[3]
        course_index_2 = course_values[2]
        course_index_1 = course_values[1]
        course_index_0 = course_values[0]
        ## 对患者信息的基本校验，首先校验患者的年龄，随后检验患者的年龄,是否和病程抵触
        if patient_age <= 18:
            messagebox.showerror("Attention!", "请注意检查患者年龄输入是否正确！")
            self.ui.tk_select_box_slb_course.current(0)
        elif patient_age <= 20 :
            if patient_course == course_index_3:
                self.ui.tk_select_box_slb_course.current(0)
                messagebox.showerror("Attention!", "请注意检查患者病程是否正确！")
            elif patient_course == course_index_2:
                self.ui.tk_select_box_slb_course.current(0)
                messagebox.showerror("Attention!", "请注意检查患者病程是否正确！")
        elif patient_age <= 30 :
            if patient_course == course_index_3:
                self.ui.tk_select_box_slb_course.current(0)
                messagebox.showerror("Attention!", "请注意检查患者病程是否正确！")
        elif patient_age >= 99 :
            messagebox.showerror("Attention!", "请注意检查患者年龄输入是否正确！")
            self.ui.tk_select_box_slb_course.current(0)
        # patient_course = self.ui.tk_select_box_slb_course.get()
        ## 这里指定了bmi相关控件的变化
        bmi_num = 1
        # 假设self.ui.tk_input_inp_height.get()和self.ui.tk_input_inp_weight.get()返回字符串
        height_str = str(self.ui.tk_input_inp_height.get())
        weight_str = str(self.ui.tk_input_inp_weight.get())
        # 检查height和weight是否为空或无效（例如，空字符串或者非数字）
        if not height_str or not weight_str or not height_str.replace('.', '', 1).isdigit() or not weight_str.replace(
                '.', '', 1).isdigit():
            # 如果height或weight为0，处理特殊情况，这时候以选择取代计算
            bmi = -1
            # 注意！
            bmi_select = self.ui.tk_select_box_slb_bmi.get()
            bmi_values = self.ui.tk_select_box_slb_bmi['values']  # 获取所有值
            bmi_index_0 = bmi_values[0]

            if bmi_select == bmi_index_0: # 选择也是空的就报错
                messagebox.showerror("Attention!", "请注意必须下拉选择或填写指标！")
            else:
                bmi_select  = self.ui.tk_select_box_slb_bmi.get()
        else:
            height = float(height_str)
            weight = float(weight_str)
            bmi = (10000 * weight) / (height * height)
            # 计算BMI
            if height > 210 or height <= 75:
                messagebox.showerror("Attention!", "请注意检查身高输入是否正确！")
                self.ui.tk_select_box_slb_bmi.current(0)
                bmi = 0
            elif weight > 160 or weight <= 30:
                messagebox.showerror("Attention!", "请注意检查体重输入是否正确！")
                self.ui.tk_select_box_slb_bmi.current(0)
                bmi = 0
            # 极限值校验没问题以后才能继续运算得出bmi
            # bmi = (10000 * weight) / (height * height)
        if bmi <= 0:
            self.ui.tk_select_box_slb_bmi.current(0)
            bmi_cal = "无BMI参数"
        elif bmi < 18.5 :
            self.ui.tk_select_box_slb_bmi.current(1)
            bmi_cal = "{:.4g}".format(bmi)
        elif bmi <= 23.9 :
            self.ui.tk_select_box_slb_bmi.current(2)
            bmi_cal = "{:.4g}".format(bmi)
        elif bmi <= 27.9:
            self.ui.tk_select_box_slb_bmi.current(3)
            bmi_cal = "{:.4g}".format(bmi)
            bmi_num = 12
        else:
            self.ui.tk_select_box_slb_bmi.current(4)
            bmi_cal = "{:.4g}".format(bmi)
            bmi_num = 12
        ## 这里指定了bp相关控件的变化
        sbp_str = str(self.ui.tk_input_inp_sbp.get())
        dbp_str = str(self.ui.tk_input_inp_dbp.get())
        sbp = 0
        dbp = 0
        bp_num = 1
        # 检查是否为空或无效（例如，空字符串或者非数字）
        if not sbp_str or not dbp_str or not sbp_str.replace('.', '', 1).isdigit() or not dbp_str.replace(
                '.', '', 1).isdigit():
            # 如果为0，处理特殊情况
            bp_values = self.ui.tk_select_box_slb_bp['values']  # 获取所有值
            bp_index_0 = bp_values[0]
            if self.ui.tk_select_box_slb_bp.get() == bp_index_0:
                messagebox.showerror("Attention!", "请注意检查血压输入是否正确！")
        else:
            sbp = float(sbp_str)
            dbp = float(dbp_str)
            if sbp > 280 or sbp <= 60:
                messagebox.showerror("Attention!", "请注意检查血压输入是否正确！")
                self.ui.tk_select_box_slb_bp.current(0)
            elif dbp > 220 or dbp <= 40:
                messagebox.showerror("Attention!", "请注意检查血压输入是否正确！")
                self.ui.tk_select_box_slb_bp.current(0)
            elif dbp >= sbp:
                messagebox.showerror("Attention!", "请注意检查血压输入是否正确！")
                self.ui.tk_select_box_slb_bp.current(0)
            else:
                if 60 < sbp < 120 :
                    self.ui.tk_select_box_slb_bp.current(1)
                elif sbp <= 139:
                    self.ui.tk_select_box_slb_bp.current(2)

                elif sbp <= 159:
                    self.ui.tk_select_box_slb_bp.current(3)
                    bp_num = 12
                elif sbp <= 179:
                    self.ui.tk_select_box_slb_bp.current(4)
                    bp_num = 12
                elif sbp <= 280:
                    self.ui.tk_select_box_slb_bp.current(5)
                    bp_num = 12
                else:
                    self.ui.tk_select_box_slb_bp.current(0)
        bp_select = self.ui.tk_select_box_slb_bp.get()
        ## 以下为腰围指标的控件
        waistline = float(self.ui.tk_input_inp_waistline.get())
        if waistline > 200 or waistline <= 50:
            waistline = -1
            messagebox.showerror("Attention!", "请注意检查患者腰围输入是否正确！")
        ## 以下为血液指标的控件
        hba1c = float(self.ui.tk_input_inp_hba1c.get())
        ldlc = float(self.ui.tk_input_inp_ldlc.get())
        tc = float(self.ui.tk_input_inp_tc.get())
        hd = self.ui.tk_select_box_slb_hd.get()
        hd_values = self.ui.tk_select_box_slb_hd['values']  # 获取所有值
        hd_index_1 = hd_values[1]
        hd_index_0 = hd_values[0]
        hba1c_num = 0
        bl_num = 0
        # 校验血液指标
        if hba1c > 18 or hba1c <= 3:
            messagebox.showerror("Attention!", "请注意检查患者糖化血红蛋白指标是否正确！")
            hba1c = -1
        elif ldlc > 20 or ldlc <= 0:
            messagebox.showerror("Attention!", "请注意检查患者胆固醇指标是否正确！")
            ldlc = -1
        elif tc > 20 or tc <= 0:
            messagebox.showerror("Attention!", "请注意检查患者胆固醇指标是否正确！")
            tc = -1
        else:
            if hba1c > 7:
                hba1c_num = 4
            elif hba1c <= 7:
                hba1c_num = 2
        if ldlc <= 2.6 or tc >= 5.69:
            bl_num = 4
        else:
            bl_num = 1
            if hd == hd_index_1:
                bl_num = 4
        ## 以下是糖尿病肾病
        egfr = self.ui.tk_select_box_slb_egfr.get()
        egfr_values = self.ui.tk_select_box_slb_egfr['values']  # 获取所有值
        egfr_index_5 = egfr_values[5]
        egfr_index_4 = egfr_values[4]
        egfr_index_3 = egfr_values[3]
        egfr_index_2 = egfr_values[2]
        egfr_index_1 = egfr_values[1]
        egfr_index_0 = egfr_values[0]
        uacr = self.ui.tk_select_box_slb_uacr.get()
        uacr_values = self.ui.tk_select_box_slb_uacr['values']  # 获取所有值
        uacr_index_2 = uacr_values[2]
        uacr_index_1 = uacr_values[1]
        uacr_index_0 = uacr_values[0]
        dn_num = 1
        dn_addtional = 0
        # 计算各项分数
        # G3,G4额外内容
        if uacr == uacr_index_0:
            if egfr == egfr_index_5:
                dn_num = 4
            elif egfr == egfr_index_4:
                dn_num = 3
                dn_addtional = 1
            elif egfr == egfr_index_3:
                dn_num = 2
                dn_addtional = 1
            elif egfr == egfr_index_2:
                dn_addtional = 1
            else:
                dn_num = 1
        elif uacr == uacr_index_1:
            if egfr == egfr_index_5:
                dn_num = 4
            elif egfr == egfr_index_4:
                dn_num = 3
                dn_addtional = 1
            elif egfr == egfr_index_3:
                dn_num = 3
                dn_addtional = 1
            elif egfr == egfr_index_2:
                dn_num = 2
                dn_addtional = 1
            else:
                dn_num = 1
        else:
            if egfr == egfr_index_5:
                dn_num = 4
            elif egfr == egfr_index_4:
                dn_num = 4
                dn_addtional = 1
            elif egfr == egfr_index_3:
                dn_num = 3
                dn_addtional = 1
            elif egfr == egfr_index_2:
                dn_num = 3
                dn_addtional = 1
            else:
                dn_num = 2
        ## 以下是视网膜
        dr = str(self.ui.tk_select_box_slb_dr.get())
        dr_values = self.ui.tk_select_box_slb_dr['values']  # 获取所有值
        dr_index_3 = dr_values[3]
        dr_index_2 = dr_values[2]
        dr_index_1 = dr_values[1]
        dr_index_0 = dr_values[0]
        # dr_num = 1
        if dr == dr_index_3:
            dr_num = 4
        elif dr == dr_index_2:
            dr_num = 2
        else:
            dr_num = 1
        ## 以下是糖尿病神经系统症状
        dns = self.ui.tk_select_box_slb_dns.get()
        dns_values = self.ui.tk_select_box_slb_dns['values']  # 获取所有值
        dns_index_1 = dns_values[1]
        dns_index_0 = dns_values[0]
        # dns_num = 0
        if dns == dns_index_1:
            dns_num = 1
        else:
            dns_num = 0
        print("患者编号:"+str(patient_id)+"; 年龄:"+str(patient_age)+"; 性别:"+str(patient_sex)+"; 病程:"+str(patient_course))
        print("操作科室:"+str(hp_department)+"; 操作人:"+str(hp_operator)+"; 日期:"+str(hp_date))
        """
        print("BMI:"+bmi_cal)
        print("收缩压："+str(sbp)+"；舒张压："+str(dbp)+"；血压范围："+str(bp_select))
        print("腰围："+str(waistline)+" cm；")
        print("血液指标  糖化血红蛋白："+str(hba1c)+"；低密度胆固醇："+str(ldlc)+"；总胆固醇："+str(tc))
        print("是否服用降血脂药物："+str(hd))
        print("肾功能指标  肾小球滤过率："+self.ui.tk_select_box_slb_egfr.get()+"；尿白蛋白与肌酐比："+self.ui.tk_select_box_slb_uacr.get())
        print("糖尿病视网膜  分级："+self.ui.tk_select_box_slb_dr.get())
        print("神经系统症状："+self.ui.tk_select_box_slb_dns.get())
        """
        print("复诊安排：")
        bmi_futuredate = today + timedelta(days=(360 / bmi_num))
        print("BMI:" + bmi_cal+ "，每年至少"+str(bmi_num)+"次测量身高体重，下次测量在"+str(bmi_futuredate)+"前后，注意控制体重和腰围；")
        bp_futuredate = today + timedelta(days=(360 / bp_num))
        print("收缩压：" + str(sbp) + "；舒张压：" + str(dbp) + "；血压范围：" + str(bp_select)+"；每年至少"+str(bp_num)+"次测量血压，下次测量在"+str(bp_futuredate)+"前后，注意控制血压及其他血液指标；")
        hba1c_futuredate = today + timedelta(days=(360 / hba1c_num))
        print("血液指标\n糖化血红蛋白：" + str(hba1c) + "，每年至少"+str(hba1c_num)+"次测量，下次测量在"+str(hba1c_futuredate)+"前后;")
        bl_futuredate = today + timedelta(days=(360 / bl_num))
        print("低密度胆固醇："+str(ldlc)+"；总胆固醇："+str(tc)+"是否服用降血脂药物："+str(hd)+"，每年至少测量血脂"+str(bl_num)+"次，下次测量在"+str(bl_futuredate)+"前后;")
        dn_futuredate = today + timedelta(days=(360 / dn_num))
        print("肾功能指标\n肾小球滤过率：" + self.ui.tk_select_box_slb_egfr.get() + "；尿白蛋白与肌酐比：" + self.ui.tk_select_box_slb_uacr.get())
        print("每年至少检查肾功能" + str(dn_num) + "次，下次检查在" + str(dn_futuredate) + "前后，复查血清肌酐、UACR、血钾；")
        if dn_addtional == 1:
            print("——根据肾小球滤过率指标，应当注意关注/检测：血红蛋白、碳酸氢钠、维生素D、血钙、血磷、甲状旁腺激素 等重要指标")
        dr_futuredate = today + timedelta(days=(360 / dr_num))
        print("糖尿病视网膜病变分级：" + self.ui.tk_select_box_slb_dr.get()+"，每年至少检查眼底"+str(dr_num)+"次，下次测量在"+str(dr_futuredate) +"前后;")
        if dns_num == 1:
            print("神经系统症状：" + self.ui.tk_select_box_slb_dns.get()+"，每年应当检查神经系统并发症"+str(dr_num)+"次，下次测量在"+str(dr_futuredate) +"前后;")
        #print(str(bmi_num)+str(bp_num)+str(hba1c_num)+str(bl_num)+str(dn_num)+str(dn_addtional)+str(dr_num)+str(dns_num))
        ### 将打印内容替换为追加到文本控件
        def append_to_text(text):
            self.ui.tk_text_txt_allresult.insert(tk.END, text + "\n")
        append_to_text("复诊安排：")
        bmi_futuredate = today + timedelta(days=(360 / bmi_num))
        append_to_text("BMI:" + str(bmi_cal) + "，每年测量身高体重" + str(bmi_num) + "次，下次测量在" + str(
            bmi_futuredate) + "前后，同时注意腰围；")
        bp_futuredate = today + timedelta(days=(360 / bp_num))
        append_to_text("；血压范围：" + str(bp_select) + "；每年至少测量血压，" + str(
            bp_num) + "次，下次测量在" + str(bp_futuredate) + "前后；")
        hba1c_futuredate = today + timedelta(days=(360 / hba1c_num))
        append_to_text(
            "血液指标\n糖化血红蛋白：" + str(hba1c) + "，每年至少" + str(hba1c_num) + "次测量，下次测量在" + str(
                hba1c_futuredate) + "前后;")
        bl_futuredate = today + timedelta(days=(360 / bl_num))
        append_to_text("低密度胆固醇：" + str(ldlc) + "；总胆固醇：" + str(tc) + "是否服用降血脂药物：" + str(
            hd) + "，每年至少测量血脂" + str(bl_num) + "次，下次测量在" + str(bl_futuredate) + "前后;")
        dn_futuredate = today + timedelta(days=(360 / dn_num))
        append_to_text("肾功能指标\n肾小球滤过率："+str(self.ui.tk_select_box_slb_egfr.get()) +"；尿白蛋白与肌酐比："+str(self.ui.tk_select_box_slb_uacr.get()))  # 这里需要替换为实际的UI控件值
        append_to_text(
            "每年至少检查" + str(dn_num) + "次肾功，下次检查在" + str(dn_futuredate) + "前后，复查血清肌酐、UACR、血钾；")
        if dn_addtional == 1:
            append_to_text(
                "——根据肾小球滤过率指标，应当注意关注/检测：血红蛋白、碳酸氢钠、维生素D、血钙、血磷、甲状旁腺激素 等重要指标")
        dr_futuredate = today + timedelta(days=(360 / dr_num))
        append_to_text("糖尿病视网膜病变分级："+str(self.ui.tk_select_box_slb_dr.get()) +" ，每年至少检查眼底" + str(dr_num) + "次，下次测量在" + str(
            dr_futuredate) + "前后;")
        if dns_num == 1:
            append_to_text("神经系统症状："+str(self.ui.tk_select_box_slb_dns.get()) +" ，每年应当检查神经系统并发症" + str(dr_num) + "次，下次测量在" + str(
                dr_futuredate) + "前后;")
        # 变量全局化
        self.patient_id = patient_id
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_course = patient_course
        self.hp_department = hp_department
        self.hp_operator = hp_operator
        self.hp_date = hp_date
        self.bmi_cal = bmi_cal
        self.bmi_num = bmi_num
        self.sbp = sbp
        self.dbp = dbp
        self.bp_select = bp_select
        self.bp_num = bp_num
        self.hba1c = hba1c
        self.hba1c_num = hba1c_num
        self.ldlc = ldlc
        self.tc = tc
        self.hd = hd
        self.bl_num = bl_num
        self.dn_num = dn_num
        self.dn_addtional = dn_addtional
        self.dr_num = dr_num
        self.dns_num = dns_num
        # 获取今天的日期
        self.today = datetime.now()
    def printall(self,evt):
        self.confirmall(evt)
        # 生成文件名
        filename = f"{self.patient_id}_{self.today.strftime('%Y%m%d_%H%M%S')}.txt"
        folder_path = "./20241010"
        file_path = os.path.join(folder_path, filename)
        # 创建文件夹（如果不存在）
        os.makedirs(folder_path, exist_ok=True)
        # 将内容写入txt文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(
                f"患者编号: {self.patient_id}; 年龄: {self.patient_age}; 性别: {self.patient_sex}; 病程: {self.patient_course}\n")
            f.write(f"操作科室: {self.hp_department}; 操作人: {self.hp_operator}; 日期: {self.hp_date}\n")

            f.write(f"复诊安排：\n")
            bmi_futuredate = self.today + timedelta(days=(360 / self.bmi_num))
            f.write(
                f"BMI: {self.bmi_cal}，每年至少{self.bmi_num}次测量身高体重，下次测量在{bmi_futuredate}前后，注意控制体重和腰围；\n")
            bp_futuredate = self.today + timedelta(days=(360 / self.bp_num))
            f.write(
                f"收缩压: {self.sbp}；舒张压: {self.dbp}；血压范围: {self.bp_select}；每年至少{self.bp_num}次测量血压，下次测量在{bp_futuredate}前后，注意控制血压及其他血液指标；\n")
            hba1c_futuredate = self.today + timedelta(days=(360 / self.hba1c_num))
            f.write(
                f"血液指标\n糖化血红蛋白: {self.hba1c}，每年至少{self.hba1c_num}次测量，下次测量在{hba1c_futuredate}前后;\n")
            bl_futuredate = self.today + timedelta(days=(360 / self.bl_num))
            f.write(
                f"低密度胆固醇: {self.ldlc}；总胆固醇: {self.tc} 是否服用降血脂药物: {self.hd}，每年至少测量血脂{self.bl_num}次，下次测量在{bl_futuredate}前后;\n")
            dn_futuredate = self.today + timedelta(days=(360 / self.dn_num))
            f.write(
                f"肾功能指标\n肾小球滤过率: {self.ui.tk_select_box_slb_egfr.get()}；尿白蛋白与肌酐比: {self.ui.tk_select_box_slb_uacr.get()}\n")
            f.write(f"每年至少检查肾功能{self.dn_num}次，下次检查在{dn_futuredate}前后，复查血清肌酐、UACR、血钾；\n")
            if self.dn_addtional == 1:
                f.write(
                    "——根据肾小球滤过率指标，应当注意关注/检测：血红蛋白、碳酸氢钠、维生素D、血钙、血磷、甲状旁腺激素 等重要指标\n")
            dr_futuredate = self.today + timedelta(days=(360 / self.dr_num))
            f.write(
                f"糖尿病视网膜病变分级: {self.ui.tk_select_box_slb_dr.get()}，每年至少检查眼底{self.dr_num}次，下次测量在{dr_futuredate}前后;\n")
            if self.dns_num == 1:
                f.write(
                    f"神经系统症状: {self.ui.tk_select_box_slb_dns.get()}，每年应当检查神经系统并发症{self.dr_num}次，下次测量在{dr_futuredate}前后;\n")
            else:
                f.write(f"积极预防神经系统的并发症。\n")
        print(f"文件已保存至 {file_path}")
    def cannelall(self,evt):
        self.ui.tk_input_inp_id.delete(0, 'end')
        self.ui.tk_select_box_slb_sex.current(0)
        self.ui.tk_input_inp_age.delete(0, 'end')
        self.ui.tk_input_inp_height.delete(0, 'end')
        self.ui.tk_input_inp_sbp.delete(0, 'end')
        self.ui.tk_input_inp_weight.delete(0, 'end')
        self.ui.tk_input_inp_dbp.delete(0, 'end')
        self.ui.tk_select_box_slb_bmi.current(0)
        self.ui.tk_select_box_slb_bp.current(0)
        self.ui.tk_input_inp_waistline.delete(0, 'end')
        self.ui.tk_input_inp_hba1c.delete(0, 'end')
        self.ui.tk_input_inp_ldlc.delete(0, 'end')
        self.ui.tk_input_inp_tc.delete(0, 'end')
        self.ui.tk_select_box_slb_hd.current(0)
        self.ui.tk_select_box_slb_egfr.current(0)
        self.ui.tk_select_box_slb_uacr.current(0)
        self.ui.tk_select_box_slb_dr.current(0)
        self.ui.tk_select_box_slb_dns.current(0)
        # 删除 Text 控件中的所有内容
        self.ui.tk_text_txt_allresult.delete(1.0, 'end')
        print("操作已取消")
# 将窗口控制器 传递给UI
app = MainWin(Controller())
if __name__ == "__main__":
    # 运行全程序
    app.mainloop()