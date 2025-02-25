# Pregnancy Blood Glucose Management System_Version_1.0_02140000
# Developer: GuLifan, DongRuiQing; Leader: QiangWei; Adviser: SongQing, JiaDan; Organization: FAHXJTU
# 启动代码：在终端粘贴 streamlit run 250218PBGMS.py
import os
import pandas as pd
import math
from datetime import datetime, time, timedelta
import openpyxl
import streamlit as st
if __name__ == '__main__':
    ### 页面信息，整个网页只能调用一次
    st.set_page_config(page_title="2型糖尿病患者妊娠前及妊娠期血糖体重管理系统_V1.0", page_icon=":hospital:", layout="wide")
    def calc_lbgi_hbgi_adrr(df):
        # 过滤掉glucose为0的数据
        df = df[df['glucose'] > 0].copy()
        # 计算fBG
        df['fBG'] = df['glucose'].apply(lambda x: 1.794 * (math.log(x) ** 1.026 - 1.861))
        # 计算risk
        df['risk'] = df['fBG'].apply(lambda x: 10 * (x ** 2))
        # 计算lbgi
        lbgi = df[df['fBG'] < 0]['risk'].mean() if not df[df['fBG'] < 0].empty else 0
        # 计算hbgi
        hbgi = df[df['fBG'] > 0]['risk'].mean() if not df[df['fBG'] > 0].empty else 0
        # 计算adrr
        adrr = df['risk'].mean()
        # 返回lbgi, hbgi, adrr
        return lbgi, hbgi, adrr
    def calc_modd(df):
        # 计算每日差异
        daily_differences = []
        # 获取唯一日期
        unique_dates = pd.unique(df['timestamp'].dt.date)
        # 遍历日期
        for i in range(1, len(unique_dates)):
            # 获取前一天数据
            prev_day_data = df[df['timestamp'].dt.date == unique_dates[i - 1]]
            # 获取当天数据
            curr_day_data = df[df['timestamp'].dt.date == unique_dates[i]]
            # 遍历时间点
            for time_point in pd.unique(prev_day_data['timestamp'].dt.time):
                # 获取前一天血糖值
                prev_glucose = prev_day_data[prev_day_data['timestamp'].dt.time == time_point]['glucose'].values
                # 获取当天血糖值
                curr_glucose = curr_day_data[curr_day_data['timestamp'].dt.time == time_point]['glucose'].values
                # 如果前一天和当天都有数据，则计算差异并添加到列表中
                if prev_glucose.size and curr_glucose.size:
                    daily_differences.append(abs(prev_glucose[0] - curr_glucose[0]))
        # 返回每日差异的平均值，保留四位小数，如果没有差异则返回None
        return round(pd.Series(daily_differences).mean(), 4) if daily_differences else None
    def process_patient_file(file_path, minlennum, hourbefore, duringhour):
        # 尝试读取文件
        try:
            df = pd.read_excel(file_path, header=None)
            # 删除第一行
            df = df.drop(0).reset_index(drop=True)
            # 设置列名
            df.columns = ['timestamp', 'glucose']
            # 将时间戳转换为datetime类型
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')
            # 将血糖值转换为数值类型，并限制在1.8到33.3之间
            df['glucose'] = pd.to_numeric(df['glucose'], errors='coerce').clip(1.8, 33.3)
        except Exception as e:
            # 如果读取或格式转换失败，则输出错误信息
            st.error(f"文件读取或格式转换失败: {e}")
            return None
        # 如果数据行数小于minlennum，则输出错误信息
        if len(df) < minlennum:
            st.error("数据不足，无法计算")
            return None
        # 计算开始时间和结束时间
        start_time = df['timestamp'].min() + timedelta(hours=hourbefore)
        end_time = start_time + timedelta(hours=duringhour)
        # 筛选出在结束时间之前的数据
        df = df[df['timestamp'] <= end_time]
        # 如果筛选后的数据为空，则输出错误信息
        if df.empty:
            st.error("数据时长不足")
            return None
        # 计算总行数
        total_rows = len(df)
        # 计算TIR、TAR、TBR、TITR
        tir = round(df[(df['glucose'] >= 3.9) & (df['glucose'] <= 10)].shape[0] / total_rows, 4)
        tar = round(df[df['glucose'] > 10].shape[0] / total_rows, 4)
        tbr = round(df[df['glucose'] < 3.9].shape[0] / total_rows, 4)
        titr = round(df[(df['glucose'] >= 3.5) & (df['glucose'] <= 7.8)].shape[0] / total_rows, 4)
        # 计算LBGI、HBGI、ADRR
        lbgi, hbgi, adrr = calc_lbgi_hbgi_adrr(df)
        # 计算MODD
        modd = calc_modd(df)
        # 返回结果
        return {
            'patient_id': os.path.splitext(os.path.basename(file_path))[0],
            'start_time': start_time,
            'end_time': end_time,
            'MEAN': round(df['glucose'].mean(), 4),
            'GMI': round(12.71 + 4.70587 * df['glucose'].mean(), 4),
            'SD': round(df['glucose'].std(), 4),
            'CV': round(df['glucose'].std() / df['glucose'].mean(), 4),
            'TIR': tir, 'TAR': tar, 'TBR': tbr, 'TITR': titr, 'LBGI': round(lbgi, 4),
            'HBGI': round(hbgi, 4), 'ADRR': round(adrr, 4), 'MODD': modd
        }
    # mode是患者和医生模式的标识，患者mode = 0，医生mode = 1
    if 'mode' not in st.session_state:
        st.session_state.mode = 0
    # doctor_confirm是医生身份验证的标识，验证成功为True，否则为False
    if 'doctor_confirm' not in st.session_state:
        st.session_state.doctor_confirm = False
    # 侧边栏固定区块
    with st.sidebar:
        st.header("请在此处选择您的身份")
        # 模式切换按钮，点击可以切换功能和界面
        btn_label = "切换到医师模式" if st.session_state.mode == 0 else "切换到患者模式"
        if st.button(btn_label, key="mode_toggle"):
            st.session_state.mode = 1 - st.session_state.mode # 点击一次（尝试）切换一次状态
        # 医生模式身份验证
        if st.session_state.mode == 1:
            doctor_id = st.text_input(
                "请输入您的工号验证医师身份:",
                value=st.session_state.get("doctor_id", ""),
                key="doctor_id_input"
            )
            if doctor_id:
                if doctor_id in [
                    "123456", "654321" # 此处为医生工号，可自行添加，实装后改为SQL注入，在网站后台数据库修改
                ]: # 医生工号验证
                    st.session_state.doctor_confirm = True
                    st.success("验证成功")
                else:
                    st.error("未匹配到您的信息")
                    st.session_state.mode = 0  # 自动回退到患者模式
    if st.session_state.mode == 0:
        st.write("当前模式：患者模式")
        # 侧边栏中输入患者的基本信息
        st.sidebar.subheader("患者信息")
        # 患者姓名
        patient_name = st.sidebar.text_input("姓名", placeholder="请输入您的姓名")
        # 患者年龄
        patient_age = st.sidebar.number_input("年龄", min_value=20, max_value=50, step=1)
        # 首诊日期
        visit_date = st.sidebar.date_input("您的首诊日期")
        # 首诊科室
        visit_department = st.sidebar.selectbox("首诊科室", ["内分泌代谢科", "妇产科", "其他科室"])
        patient_phonenumber = st.sidebar.text_input("手机号码", placeholder="1xx-xxxx-xxxx") # 联系方式
        st.sidebar.markdown("---") # 显示患者的基本信息，分割
        st.sidebar.subheader("信息预览") # 信息预览
        if patient_name:
            st.sidebar.write(f" {patient_name} **女士**")
        if patient_age:
            st.sidebar.write(f"**年龄：** {patient_age} 岁")
        st.sidebar.write(f"**首诊时间：** {visit_date}")
        ### 标题信息区块
        st.title("2型糖尿病患者妊娠前及妊娠期血糖体重管理系统")  # 标题
        # st.subheader("Pregnancy Blood Glucose Management System_Version_1.0.1_202502181818")  # 更小标题
        st.text("由 西安交通大学第一附属医院内分泌代谢科 开发") # 作者名称
        ### 主内容区块
        placeholder = st.empty()  # 创建占位符,为顶端提示框留出空间，顶端提示框不影响空间布局
        if patient_name and patient_phonenumber:
            # 检测手机号是否为 11 位数字
            if patient_phonenumber.isdigit() and len(patient_phonenumber) == 11:
                # 显示success提示框
                with (placeholder):
                    st.success(f'{patient_name} 女士 的信息已录入')
            else:
                # 显示手机号错误提示
                with placeholder:
                    st.error('请您输入正确的手机号码')
        else:
            # 提示用户输入完整信息
            with placeholder:
                with placeholder:
                    st.warning('请您填写、核对个人信息')
        # 设置页面标题
        st.subheader("您当前的身高和体重")
        # 使用 columns模块 来水平排列输入框，输入患者的身高体重，height和weight变量是初始值，后续调用注意数据形式
        col01, col02 = st.columns(2) # col0x是第一个横排文本框
        with col01:
            height = st.text_input("请输入身高（厘米）:", key="height_input")
        with col02:
            weight = st.text_input("请输入体重（公斤）:", key="weight_input")
        # 尝试将输入转换为浮点数，并计算 BMI
        try:
            # fl的后缀标志着该变量已经改为了float格式，以下各个变量都应该使用fl形式进行计算
            height_fl = float(height)
            weight_fl = float(weight)
            # 判断身高体重是否在合理范围内！！！校对！！！
            if 140 <= height_fl <= 200 and 45 <=weight_fl <= 100:
                # 计算 BMI，bmi_fl是bmi的浮点数形式
                bmi_fl = weight_fl / (height_fl * height_fl / 10000)
                # 显示 BMI 结果
                st.info(f"您当前的 BMI 是: {bmi_fl:.2f}")
            else:
                st.error("身高或体重输入可能有误，您可以再核对")
        except ValueError:
            st.write("请输入有效的数字")
        ### 怀孕状态部分
        st.subheader("您的怀孕状态")
        ### 此处注意：对下方的变量进行全局化保存
        # 初始化 session_state 变量，怀孕代码和用药代码，没写就是-1，0就是未，该变量应当全局保存
        if 'pregnancy_status_code' not in st.session_state:
            st.session_state.pregnancy_status_code = -1
        if 'pregnancy_status' not in st.session_state:
            st.session_state.pregnancy_status = "NA"
        if 'using_medication_code' not in st.session_state:
            st.session_state.using_medication_code = -1
        if 'using_medication' not in st.session_state:
            st.session_state.using_medication = "NA"
        # 创建备孕状态按钮
        cola1, cola2 = st.columns(2)
        # 使用 HTML 和 Streamlit 的 markdown 功能来增强视觉效果，主要是将布局改为水平均匀分布
        st.markdown(
            """
            <style>
            .big-font {
                font-size: 18px !important;
                font-weight: bold;
                color: #4A90E2;
            }
            .stButton>button {
                width: 100%;
                height: 50px;
                font-size: 18px;
                font-weight: bold;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            </style>
            """,
            unsafe_allow_html=True, # 允许使用 HTML 标签
        )
        with cola1:
            # 备孕选项
            if st.button("备孕当中"):
                st.session_state.pregnancy_status_code = 0
                st.session_state.pregnancy_status = "备孕当中"
        with cola2:
            # 怀孕选项
            if st.button("已经怀孕"):
                st.session_state.pregnancy_status_code = 1
                st.session_state.pregnancy_status = "已经怀孕"
        # 显示备孕状态后的内容
        if st.session_state.pregnancy_status_code != -1:
            st.success(f"您选择了：“{st.session_state.pregnancy_status}”，请您继续填写下面的信息")
            # 备孕状态下的逻辑
            if st.session_state.pregnancy_status_code == 0:
                st.subheader("控糖药物及指标查询")
                colb1, colb2 = st.columns(2)
                with colb1:
                    if st.button("目前不使用任何糖尿病药物"):
                        st.session_state.using_medication_code = 0
                        st.session_state.using_medication = "不用药"
                with colb2:
                    if st.button("目前有使用糖尿病药物控制症状"):
                        st.session_state.using_medication_code = 1
                        st.session_state.using_medication = "用药"
                # 显示用药状态后的内容
                if st.session_state.using_medication_code != -1:
                    st.success(f"您选择了：“{st.session_state.using_medication}”，请您继续填写下面的信息")
                    if st.session_state.using_medication_code == 1:
                        # 显示用药的输入框和药物选择
                        col21, col22, col23 = st.columns(3)
                        with col21:
                            fpg = st.text_input("请输入您的FPG指标:")
                        with col22:
                            ppg = st.text_input("请输入您的PPG指标:")
                        with col23:
                            hba1c = st.text_input("请输入您的HbA1c指标:")
                        st.title('药品分类选择')
                        medications_yidaosu = st.multiselect("胰岛素类:",
                                                             ["短效人胰岛素(RI)",
                                                              "门冬胰岛素赖脯胰岛素谷赖胰岛素",
                                                              "中效人胰岛素(NPH)",
                                                              "长效胰岛素(PZI)",
                                                              "甘精胰岛素U100",
                                                              "甘精胰岛素 U300",
                                                              "地特胰岛素",
                                                              "德谷胰岛素",
                                                              "预混人胰岛素(30R,70/30)",
                                                              "预混人胰岛素(40R)",
                                                              "预混人胰岛素(5OR)",
                                                              "预混门冬胰岛素30",
                                                              "预混门冬胰岛素50",
                                                              "预混赖脯胰岛素 25",
                                                              "预混赖脯胰岛素 50",
                                                              "双胰岛素类似物(德谷门冬双胰岛素70/30)"])
                        medications_shuanggua = st.multiselect("二甲双胍:", ["二甲双胍",
                                                                             "二甲双胍缓释片"])
                        medications_huangniao = st.multiselect("磺脲类:",
                                                               ["格列本脲",
                                                                "格列吡嗪",
                                                                "格列吡嗪控释片",
                                                                "格列齐特",
                                                                "格列齐特控释片",
                                                                "格列喹酮",
                                                                "格列美脲"])
                        medications_gelienai = st.multiselect("格列奈类:", ["瑞格列奈",
                                                                            "那格列奈",
                                                                            "米格列奈钙片"])
                        medications_tzd = st.multiselect("TZD类:", ["吡格列酮",
                                                                    "罗格列酮"])
                        medications_atanggan = st.multiselect("α糖苷酶抑制剂:", ["阿卡波糖",
                                                                                 "伏格列波糖",
                                                                                 "米格列醇"])
                        medications_dpp = st.multiselect("DPP-4i:",
                                                         ["西格列汀",
                                                          "沙格列汀",
                                                          "利格列汀",
                                                          "阿格列汀",
                                                          "瑞格列汀",
                                                          "考格列汀"])
                        medications_sglt2 = st.multiselect("SGLT-2i:",
                                                           ["达格列净",
                                                            "恩格列净",
                                                            "卡格列净",
                                                            "艾托格列净",
                                                            "恒格列净",
                                                            "加格列净"])
                        medications_gka = st.multiselect("GKA:", ["多格列艾汀"])
                        medications_glp1 = st.multiselect("GLP-1RA:",
                                                          ["司美格鲁肽片",
                                                           "贝纳鲁肽",
                                                           "艾塞那肽",
                                                           "利司那肽",
                                                           "利拉鲁肽",
                                                           "艾塞那肽周制剂",
                                                           "度拉唐肽",
                                                           "洛塞那肽",
                                                           "司美格鲁肽注射液",
                                                           "替尔泊肽"])
                        medications_ppar = st.multiselect("PPAR泛激动剂:", ["西格列他钠"])
                        medications_other = st.multiselect("其他药物:", ["其他药物"])
                        if st.button("药物选择完成"):
                            #反馈药物选择的结果
                            st.write("您选择的药物有：", medications_yidaosu,
                                     medications_shuanggua,
                                     medications_huangniao,
                                     medications_gelienai,
                                     medications_tzd,
                                     medications_dpp,
                                     medications_sglt2,
                                     medications_gka,
                                     medications_glp1,
                                     medications_ppar,
                                     medications_other)
                            if (
                                    medications_huangniao == [] and medications_gelienai == [] and medications_tzd == []
                                    and medications_dpp == [] and medications_sglt2 == [] and medications_gka == [] and
                                    medications_glp1 == [] and medications_ppar == [] and medications_other == []):
                                # 判断身高体重是否在合理范围内！！！校对！！！
                                if 0.5 > float(fpg) or float(fpg) >= 15 or 0.5 > float(ppg) or float(ppg) >= 15 or 0.5 > float(hba1c) or float(hba1c) >= 25:
                                    st.error("血糖指标输入可能有误，您可以再核对")
                                elif (3.9 <= float(fpg) <= 6.5) and (float(ppg) <= 8.5) and (float(hba1c)) <= 7:
                                    st.success("您的指血指标目前在正常范围内，请继续保持良好的生活习惯和饮食习惯。")
                                    if medications_yidaosu != []:
                                        st.success("胰岛素类药物可以在备孕以及孕期继续使用。甘精胰岛素U100建议孕期停用。更换药物务必先咨询医师。")
                                        st.info("使用胰岛素的患者请注意运动时可能存在的低血糖风险！")
                                    if medications_shuanggua != []:
                                        st.warning(
                                            "研究未见二甲双胍会增加胎儿先天异常及新生儿毒性风险。药物说明书不推荐备孕和孕期使用。充分知情者可使用。")
                                else:
                                    st.error("您的指血指标不在正常范围内，请优先控制血糖，或前往专科治疗后备孕。")
                            else:
                                st.error("您的药物方案不适合备孕。如您确需怀孕，请至专科门诊调整！")
                    elif st.session_state.using_medication_code == 0:
                        # 水平排列输入框：FPG, PPG1h, PPG2h
                        col31, col32, col33 = st.columns(3)
                        with col31:
                            fpg = st.text_input("请输入FPG指标:")
                        with col32:
                            ppg1h = st.text_input("请输入PPG1h指标:")
                        with col33:
                            ppg2h = st.text_input("请输入PPG2h指标:")
                        if fpg and ppg1h and ppg2h:
                            # 可以在这里添加对输入指标的进一步处理或显示
                            st.info(f"FPG: {fpg}, PPG1h: {ppg1h}, PPG2h: {ppg2h}")
                            if (float(fpg) <= 6.1) and (float(ppg1h) <= 7.8) and (float(ppg2h)) <= 6.5:
                                st.success("您的指血指标目前在正常范围内，请继续保持良好的生活习惯和饮食习惯。")
                                # 根据BMI值给出建议
                                if bmi_fl < 18.5:
                                    st.warning(
                                        f"您体重偏瘦。可通过适当增加食物量和规律运动增加体重，每天可有1~2次的加餐，如每天增加牛奶200mL或粮谷/畜肉类50g或蛋类/鱼类75g，体重适宜再备孕。")
                                elif 18.5 <= bmi_fl <= 24.0:
                                    st.success(
                                        f"您体重正常。建议您在孕前完善各项备孕检查！\n您在孕期总增重范围为11.5至16.0kg.\n建议孕中晚期增重速率控制在0.42（0.35~0.50）kg/周。")
                                else:
                                    st.warning(
                                        f"您初始体重过高。应改变不良饮食习惯，减慢进食连度，避免过量，减少高热量、高脂肪、高糖食物的摄入，多选择低生糖指数、富含隔食纤维、营养密度高的食物。同时，应增加运动，推荐每天30~90min中等强度的运动。体重合适后再备孕。")
                                    if bmi_fl <= 32.5:
                                        st.warning("初始6每周减去0.5-1kg，每月2-4kg，6个月内减重5-15%并维持。")
                                    else:
                                        st.warning("3-6月内阶段性减重5%、10%、15%，有需要则及时就医。")
                            else:
                                st.error(
                                    "您的血糖指标控制不佳，请严格控制生活习惯，必要时应当就医！建议咨询专科医生再备孕！\n（参考范围fpg <6.1、ppg1h<7.8、ppg2h<6.5）")
            elif st.session_state.pregnancy_status_code == 1:
                st.subheader("体型与血糖指标")
                col51, col52 = st.columns(2)
                with col51:
                    weight0 = st.text_input("请输入孕期初始体重（公斤）:")
                with col52:
                    pweek = st.text_input("请输入孕周:")
                # 水平排列输入框：FPG, PPG1h, PPG2h,TIR
                col61, col62, col63 = st.columns(3)
                with col61:
                    fpg = st.text_input("请输入FPG指标:")
                with col62:
                    ppg1h = st.text_input("请输入PPG1h指标:")
                with col63:
                    ppg2h = st.text_input("请输入PPG2h指标:")
                if pweek and weight0 and fpg and ppg1h and ppg2h:
                    # 可以在这里添加对输入指标的进一步处理或显示
                    st.info(f"孕周: {pweek}，怀孕时初始体重：{weight0}，FPG: {fpg}, PPG1h: {ppg1h}, PPG2h: {ppg2h}")
                    if (0.5 > float(fpg) or float(fpg) >= 15 or 0.5 > float(ppg1h)
                            or float(ppg1h) >= 15 or 0.5 > float(ppg2h) or float(ppg2h) >= 25
                            or float(pweek) <= 2 or float(pweek) >= 38 or float(weight0) <= 45
                            or float(weight0) >= 105):
                        st.error("上述指标输入可能有误，您可以再核对")
                    else:
                        if float(pweek) <= 12 :
                            st.success("您正处于孕早期，请注意控制您的营养摄入和体重增长速率,若无运动禁忌证，1周中至少五天每天进行半小时中等强度的运动。")
                        elif float(pweek) <=27:
                            st.success("您正处于孕中期，请注意控制您的营养摄入和体重增长速率，注意血糖变化以及可能的并发症。")
                        else:
                            st.success("您正处于孕晚期，请注意控制您的营养摄入和体重增长速率！")
                        if (float(fpg) <=5.3) and (float(ppg1h)<=7.8) and (float(ppg2h))<=6.7:
                            st.success("您的指血指标目前在正常范围内，请继续保持孕期良好的生活习惯和饮食习惯。")
                        else:
                            st.error("您的血糖指标目前控制不佳，请严格控制生活习惯，必要时及时就医！\n（参考范围fpg <5.3、ppg1h<7.8、ppg2h<6.7）")
                    # 尝试将输入转换为浮点数，并计算 BMI0
                    try:
                        height_fl = float(height)
                        weight0_fl = float(weight0)
                        if 140 <= height_fl <= 200 and 45 <= weight0_fl <= 100:
                            # 计算 BMI
                            bmi0_fl = weight0_fl / (height_fl * height_fl / 10000)
                            ### 此处放置对照表格
                            # 展示表格
                            st.markdown("""
                            **表： 妊娠期妇女体重增长范围和妊娠中晚期每周体重增长推荐值**

                            | 妊娠前体质指数分类 | 总增长值范围 /kg | 妊娠早期增长值 /kg | 妊娠中晚期每周体重增长值及范围 /kg |
                            |----------------------|------------------|--------------------|------------------------------------|
                            | 低体重（BMI＜18.5kg/m²） | 11.0~16.0        | 0~2.0              | 0.46（0.37~0.56）                   |
                            | 正常体重（18.5 kg/m²≤BMI＜24.0 kg/m²） | 8.0~14.0          | 0~2.0              | 0.37（0.26~0.48）                   |
                            | 超重（24.0kg/m²≤BMI＜28.0 kg/m²） | 7.0~11.0          | 0~2.0              | 0.30（0.22~0.37）                   |
                            | 肥胖（BMI≥28.0kg/m²） | 5.0~9.0           | 0~2.0              | 0.22（0.15~0.30）                   |
                            """)
                            # 根据BMI值给出建议
                            if bmi0_fl <= 18.5:
                                weight_add = int(weight0_fl + 17- float(weight))
                                st.warning(f"您初始体重偏瘦。建议您在孕期加强营养摄入，以促进胎儿发育。必要时可联系专业人士。\n您在孕期总增重范围为12.5至18.0kg，目前建议增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.51（0.44~0.58）kg/周。")
                            elif 18.5 < bmi0_fl <= 24.9:
                                weight_add = int(weight0_fl + 15- float(weight))
                                st.success(f"您初始体重属于正常范围。建议您在孕期保持营养均衡，适量运动、保持良好的睡眠等。\n您在孕期总增重范围为11.5至16.0kg，目前尚可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.42（0.35~0.50）kg/周。")
                            elif 24.9 < bmi0_fl <= 29.9:
                                weight_add = int(weight0_fl + 11 - float(weight))
                                st.error(f"您初始体重偏胖，您在孕期应适当控制饮食，减少高热高脂摄入，增加蔬菜、水果等富含纤维的食物摄入。\n您在孕期总增重范围为7.0至11.5kg，目前尚可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.28（0.23~0.33）kg/周。")
                            else:
                                weight_add = int(weight0_fl + 8.5 - float(weight))
                                st.warning(f"您初始体重超重，务必在孕期严格控制饮食，必要时求医。\n您在孕期总增重范围为5.0至9.0kg，最多可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.22（0.17~0.27）kg/周。")
                        else:
                            st.error("身高或体重输入可能有误，请核对")
                    except ValueError:
                        st.write("请输入有效的数字")
        else:
            st.info("请选择您的怀孕状态：")
        question_text = st.text_area(label='若您有其他问题或需求，可于此处告知我们',value='请输入...', height=75, max_chars=250,
                            help='最大长度限制为250字符')
        if st.button('我已充分知晓以上信息并确认，提交')  and (question_text != ''):
            st.success('您的问题或需求已发送至服务器,感谢您的支持！')
    elif st.session_state.mode == 1 :
        if st.session_state.doctor_confirm == False:
            st.warning("请先在侧边栏验证身份")
        else:
            st.write("当前模式：医生模式")
            st.sidebar.subheader("此处填写患者信息")
            # 患者信息输入（所有输入组件添加 key）
            patient_name = st.sidebar.text_input("姓名", placeholder="输入患者姓名", key='patient_name')
            patient_age = st.sidebar.number_input("年龄", min_value=20, max_value=50, step=1, key='patient_age')
            visit_date = st.sidebar.date_input("患者首诊日期", key='visit_date')
            visit_department = st.sidebar.selectbox("操作科室", ["内分泌代谢科", "妇产科", "其他科室"], key='visit_department')
            patient_number = st.sidebar.text_input("住院/就诊的标识", placeholder="可填写住院号等患者标识", key='patient_number')
            patient_phonenumber = st.sidebar.text_input("患者联系方式（选填）", placeholder="可填写患者手机号码", key='patient_phonenumber')
            st.sidebar.markdown("---")  # 显示患者的基本信息，分割
            st.sidebar.link_button("向维护者报告", "https://github.com/GuLifan")
            ### 标题信息区块
            st.title("2型糖尿病患者妊娠前及妊娠期血糖体重管理系统")  # 标题
            st.subheader("Pregnancy Blood Glucose Management System_Version_1.0.1_202502181818")  # 更小标题
            st.text("西安交通大学第一附属医院内分泌代谢科__2025年2月18日内部发布版本") # 单位名称
            ### 主内容区块
            placeholder = st.empty()  # 创建占位符,为顶端提示框留出空间，顶端提示框不影响空间布局
            if patient_name or patient_phonenumber:
                # 检测
                with (placeholder):
                    st.success(f'{patient_name} 的信息已录入')
            else:
                with (placeholder):
                    st.warning('请您核对患者信息')
            # 设置页面标题
            st.subheader("患者基本参数")
            # 使用 columns模块 来水平排列输入框，输入患者的身高体重，height和weight变量是初始值，后续调用注意数据形式
            col01, col02 = st.columns(2)  # col0x是第一个横排文本框
            with col01:
                height = st.text_input("身高（厘米）:", key="height_input")
            with col02:
                weight = st.text_input("体重（公斤）:", key="weight_input")
            # 尝试将输入转换为浮点数，并计算 BMI
            try:
                # fl的后缀标志着该变量已经改为了float格式，以下各个变量都应该使用fl形式进行计算
                height_fl = float(height)
                weight_fl = float(weight)
                # 判断身高体重是否在合理范围内！！！校对！！！
                if 140 <= height_fl <= 200 and 45 <= weight_fl <= 100:
                    # 计算 BMI，bmi_fl是bmi的浮点数形式
                    bmi_fl = weight_fl / (height_fl * height_fl / 10000)
                    # 显示 BMI 结果
                    st.info(f"当前 BMI 是: {bmi_fl:.2f}")
                else:
                    st.error("身高或体重输入可能有误")
            except ValueError:
                st.write("请输入有效的数字")
            ### 怀孕状态部分
            st.subheader("患者当前怀孕状态")
            ### 此处注意：对下方的变量进行全局化保存
            # 初始化 session_state 变量，怀孕代码和用药代码，没写就是-1，0就是未，该变量应当全局保存
            if 'pregnancy_status_code' not in st.session_state:
                st.session_state.pregnancy_status_code = -1
            if 'pregnancy_status' not in st.session_state:
                st.session_state.pregnancy_status = "NA"
            if 'using_medication_code' not in st.session_state:
                st.session_state.using_medication_code = -1
            if 'using_medication' not in st.session_state:
                st.session_state.using_medication = "NA"
            # 创建备孕状态按钮
            cola1, cola2 = st.columns(2)
            # 使用 HTML 和 Streamlit 的 markdown 功能来增强视觉效果，主要是将布局改为水平均匀分布
            st.markdown(
                """
                <style>
                .big-font {
                    font-size: 18px !important;
                    font-weight: bold;
                    color: #4A90E2;
                }
                .stButton>button {
                    width: 100%;
                    height: 50px;
                    font-size: 18px;
                    font-weight: bold;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                </style>
                """,
                unsafe_allow_html=True,  # 允许使用 HTML 标签
            )
            with cola1:
                # 备孕选项
                if st.button("备孕"):
                    st.session_state.pregnancy_status_code = 0
                    st.session_state.pregnancy_status = "备孕当中"
            with cola2:
                # 怀孕选项
                if st.button("怀孕"):
                    st.session_state.pregnancy_status_code = 1
                    st.session_state.pregnancy_status = "已经怀孕"
            # 显示备孕状态后的内容
            if st.session_state.pregnancy_status_code != -1:
                # 备孕状态下的逻辑
                if st.session_state.pregnancy_status_code == 0:
                    st.subheader("用药")
                    colb1, colb2 = st.columns(2)
                    with colb1:
                        if st.button("不用任何药物"):
                            st.session_state.using_medication_code = 0
                            st.session_state.using_medication = "不用药"
                    with colb2:
                        if st.button("使用糖尿病药物"):
                            st.session_state.using_medication_code = 1
                            st.session_state.using_medication = "用药"
                    # 显示用药状态后的内容
                    if st.session_state.using_medication_code != -1:
                        # 显示用药的输入框和药物选择
                        if st.session_state.using_medication_code == 1:
                            # 显示用药的输入框和药物选择
                            col21, col22, col23 = st.columns(3)
                            with col21:
                                fpg = st.text_input("FPG指标:")
                            with col22:
                                ppg = st.text_input("PPG指标:")
                            with col23:
                                hba1c = st.text_input("HbA1c指标:")
                            st.title('药品分类')
                            medications_yidaosu = st.multiselect("胰岛素类:",
                                                                 ["短效人胰岛素(RI)",
                                                                  "门冬胰岛素赖脯胰岛素谷赖胰岛素",
                                                                  "中效人胰岛素(NPH)",
                                                                  "长效胰岛素(PZI)",
                                                                  "甘精胰岛素U100",
                                                                  "甘精胰岛素 U300",
                                                                  "地特胰岛素",
                                                                  "德谷胰岛素",
                                                                  "预混人胰岛素(30R,70/30)",
                                                                  "预混人胰岛素(40R)",
                                                                  "预混人胰岛素(5OR)",
                                                                  "预混门冬胰岛素30",
                                                                  "预混门冬胰岛素50",
                                                                  "预混赖脯胰岛素 25",
                                                                  "预混赖脯胰岛素 50",
                                                                  "双胰岛素类似物(德谷门冬双胰岛素70/30)"])
                            medications_shuanggua = st.multiselect("二甲双胍:",
                                                                   ["二甲双胍", "二甲双胍缓释片"])
                            medications_huangniao = st.multiselect("磺脲类:",
                                                                   ["格列本脲",
                                                                    "格列吡嗪",
                                                                    "格列吡嗪控释片",
                                                                    "格列齐特",
                                                                    "格列齐特控释片",
                                                                    "格列喹酮",
                                                                    "格列美脲"])
                            medications_gelienai = st.multiselect("格列奈类:", ["瑞格列奈",
                                                                                "那格列奈",
                                                                                "米格列奈钙片"])
                            medications_tzd = st.multiselect("TZD类:", ["吡格列酮",
                                                                        "罗格列酮"])
                            medications_atanggan = st.multiselect("α糖苷酶抑制剂:",
                                                                  ["阿卡波糖",
                                                                   "伏格列波糖",
                                                                   "米格列醇"])
                            medications_dpp = st.multiselect("DPP-4i:",
                                                             ["西格列汀",
                                                              "沙格列汀",
                                                              "利格列汀",
                                                              "阿格列汀",
                                                              "瑞格列汀",
                                                              "考格列汀"])
                            medications_sglt2 = st.multiselect("SGLT-2i:",
                                                               ["达格列净",
                                                                "恩格列净",
                                                                "卡格列净",
                                                                "艾托格列净",
                                                                "恒格列净",
                                                                "加格列净"])
                            medications_gka = st.multiselect("GKA:", ["多格列艾汀"])
                            medications_glp1 = st.multiselect("GLP-1RA:",
                                                              ["司美格鲁肽片",
                                                               "贝纳鲁肽",
                                                               "艾塞那肽",
                                                               "利司那肽",
                                                               "利拉鲁肽",
                                                               "艾塞那肽周制剂",
                                                               "度拉唐肽",
                                                               "洛塞那肽",
                                                               "司美格鲁肽注射液",
                                                               "替尔泊肽"])
                            medications_ppar = st.multiselect("PPAR泛激动剂:", ["西格列他钠"])
                            medications_other = st.multiselect("其他药物:", ["其他药物"])
                            if st.button("药物选择完成"):
                                # 反馈药物选择的结果
                                """
                                st.write("您选择的药物有：", medications_yidaosu, medications_shuanggua,
                                         medications_huangniao,
                                         medications_gelienai, medications_tzd, medications_dpp, medications_sglt2,
                                         medications_gka, medications_glp1, medications_ppar, medications_other)
                                """
                                if (
                                        medications_huangniao == [] and medications_gelienai == [] and
                                        medications_tzd == [] and medications_dpp == [] and medications_sglt2 == [] and
                                        medications_gka == [] and medications_glp1 == [] and medications_ppar == [] and
                                        medications_other == []):
                                    # 判断身高体重是否在合理范围内！！！校对！！！
                                    if (0.5 > float(fpg) or float(fpg) >= 15 or 0.5 > float(ppg) or
                                            float(ppg) >= 15 or 0.5 > float(hba1c) or float(hba1c) >= 25):
                                        st.error("血糖指标输入可能有误")
                                    elif (3.9 <= float(fpg) <= 6.5) and (float(ppg) <= 8.5) and (float(hba1c)) <= 7:
                                        st.success("您的指血指标目前在正常范围内，请继续保持良好的生活习惯和饮食习惯。")
                                        if medications_yidaosu != []:
                                            st.success(
                                                "胰岛素类药物可以在备孕以及孕期继续使用。甘精胰岛素U100建议孕期停用。")
                                            st.info("使用胰岛素的患者要注意运动时可能存在的低血糖风险！")
                                        if medications_shuanggua != []:
                                            st.warning(
                                                "研究未见二甲双胍会增加胎儿先天异常及新生儿毒性风险。需向患者说明。")
                                    else:
                                        st.error("您的指血指标不在正常范围内，请优先控制血糖，或前往专科治疗后备孕。")
                                else:
                                    st.error("您的药物方案不适合备孕。如您确需怀孕，请至专科门诊调整！")
                        elif st.session_state.using_medication_code == 0:
                            # 水平排列输入框：FPG, PPG1h, PPG2h
                            col31, col32, col33 = st.columns(3)
                            with col31:
                                fpg = st.text_input("请输入FPG指标:")
                            with col32:
                                ppg1h = st.text_input("请输入PPG1h指标:")
                            with col33:
                                ppg2h = st.text_input("请输入PPG2h指标:")
                            if fpg and ppg1h and ppg2h:
                                # 可以在这里添加对输入指标的进一步处理或显示
                                st.info(f"FPG: {fpg}, PPG1h: {ppg1h}, PPG2h: {ppg2h}")
                                if (float(fpg) <= 6.1) and (float(ppg1h) <= 7.8) and (float(ppg2h)) <= 6.5:
                                    st.success("指血指标目前在正常范围内")
                                    # 根据BMI值给出建议
                                    if bmi_fl < 18.5:
                                        st.warning(
                                            f"您体重偏瘦。可通过适当增加食物量和规律运动增加体重。")
                                    elif 18.5 <= bmi_fl <= 24.0:
                                        st.success(
                                            f"您体重正常。建议孕前完善各项备孕检查！孕期总增重范围为11.5至16.0kg。")
                                    else:
                                        st.warning(
                                            f"您初始体重过高。应改变不良饮食习惯，增加运动，推荐每天30~90min中等强度的运动。")
                                        if bmi_fl <= 32.5:
                                            st.warning("初始6每周减去0.5-1kg，每月2-4kg，6个月内减重5-15%并维持。")
                                        else:
                                            st.warning("3-6月内阶段性减重5%、10%、15%，有需要则及时就医。")
                                else:
                                    st.error(
                                        "您的血糖指标控制不佳，立刻干预！")
                elif st.session_state.pregnancy_status_code == 1:
                    st.subheader("体型与血糖指标")
                    col51, col52 = st.columns(2)
                    with col51:
                        weight0 = st.text_input("请输入孕期初始体重（公斤）:")
                    with col52:
                        pweek = st.text_input("请输入孕周:")
                    # 水平排列输入框：FPG, PPG1h, PPG2h,TIR
                    col61, col62, col63 = st.columns(3)
                    with col61:
                        fpg = st.text_input("请输入FPG指标:")
                    with col62:
                        ppg1h = st.text_input("请输入PPG1h指标:")
                    with col63:
                        ppg2h = st.text_input("请输入PPG2h指标:")
                    if pweek and weight0 and fpg and ppg1h and ppg2h:
                        # 可以在这里添加对输入指标的进一步处理或显示
                        st.info(f"孕周: {pweek}，怀孕时初始体重：{weight0}，FPG: {fpg}, PPG1h: {ppg1h}, PPG2h: {ppg2h}")
                        if (0.5 > float(fpg) or float(fpg) >= 15 or 0.5 > float(ppg1h) or float(ppg1h) >= 15
                                or 0.5 > float(ppg2h) or float(ppg2h) >= 25 or float(pweek) <= 2 or float(
                                pweek) >= 38 or float(weight0) <= 45 or float(weight0) >= 105):
                            st.error("上述指标输入可能有误，您可以再核对")
                        else:
                            if float(pweek) <= 12:
                                st.success(
                                    "孕早期，控制营养摄入和体重增长速率,若无运动禁忌证，1周中至少五天每天进行半小时中等强度的运动。")
                            elif float(pweek) <= 27:
                                st.success(
                                    "孕中期，控制营养摄入和体重增长速率，注意血糖变化以及可能的并发症。")
                            else:
                                st.success("您正处于孕晚期，注意控制营养摄入和体重增长速率！")
                            if (float(fpg) <= 5.3) and (float(ppg1h) <= 7.8) and (float(ppg2h)) <= 6.7:
                                st.success("指血指标目前在正常范围内，保持孕期良好的生活习惯和饮食习惯。")
                            else:
                                st.error(
                                    "血糖指标目前控制不佳，严格控制生活习惯！")
                        # 尝试将输入转换为浮点数，并计算 BMI0
                        try:
                            height_fl = float(height)
                            weight0_fl = float(weight0)
                            if 140 <= height_fl <= 200 and 45 <= weight0_fl <= 100:
                                # 计算 BMI
                                bmi0_fl = weight0_fl / (height_fl * height_fl / 10000)
                                ### 此处放置对照表格
                                # 展示表格
                                st.markdown("""
                                **表： 妊娠期妇女体重增长范围和妊娠中晚期每周体重增长推荐值**
                                | 妊娠前体质指数分类 | 总增长值范围 /kg | 妊娠早期增长值 /kg | 妊娠中晚期每周体重增长值及范围 /kg |
                                |----------------------|------------------|--------------------|---------------------|
                                | 低体重（BMI＜18.5kg/m²） | 11.0~16.0        | 0~2.0     | 0.46（0.37~0.56）  |
                                | 正常体重（18.5 kg/m²≤BMI＜24.0 kg/m²） | 8.0~14.0     | 0~2.0 | 0.37（0.26~0.48） |
                                | 超重（24.0kg/m²≤BMI＜28.0 kg/m²） | 7.0~11.0      | 0~2.0    | 0.30（0.22~0.37）  |
                                | 肥胖（BMI≥28.0kg/m²） | 5.0~9.0    | 0~2.0   | 0.22（0.15~0.30）  |
                                ------
                                **表： 表2 妊娠期高血糖孕妇每日各类食物的推荐摄入量[kcal(份)]**
                                |食物种类|1600 kcal|1800 kcal|2000 kcal|2200 kcal|
                                |--|--|--|--|--|
                                |谷薯类|800(9)|900(10)|920(10)|1000(11)|
                                |蔬菜类|90(1)|90(1)|140(1.5)|200(2)|
                                |水果类|90(1)|90(1)|90(1)|100(1)|
                                |奶制品|180(2)|270(3)|270(3)|270(3)|
                                |肉蛋豆类|270(3)|270(3)|360(4)|360(4)|
                                |油、坚果类|170(2)|180(2)|220(2.5)|270(3)|
                                |合计|1600(18)|1800(20)|2000(22)|2200(24)|
                                """)
                                # 根据BMI值给出建议
                                if bmi0_fl <= 18.5:
                                    weight_add = int(weight0_fl + 17 - float(weight))
                                    st.warning(
                                        f"初始体重偏瘦。孕期总增重范围为12.5至18.0kg，目前建议增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.51（0.44~0.58）kg/周。")
                                elif 18.5 < bmi0_fl <= 24.9:
                                    weight_add = int(weight0_fl + 15 - float(weight))
                                    st.success(
                                        f"初始体重属于正常范围。孕期总增重范围为11.5至16.0kg，目前尚可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.42（0.35~0.50）kg/周。")
                                elif 24.9 < bmi0_fl <= 29.9:
                                    weight_add = int(weight0_fl + 11 - float(weight))
                                    st.error(
                                        f"初始体重偏胖。孕期总增重范围为7.0至11.5kg，目前尚可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.28（0.23~0.33）kg/周。")
                                else:
                                    weight_add = int(weight0_fl + 8.5 - float(weight))
                                    st.warning(
                                        f"您初始体重超重，务必在孕期严格控制饮食，必要时求医。\n孕期总增重范围为5.0至9.0kg，最多可增加约{weight_add}公斤。\n建议孕中晚期增重速率控制在0.22（0.17~0.27）kg/周。")
                            else:
                                st.error("身高或体重输入可能有误，请核对")
                        except ValueError:
                            st.write("请输入有效的数字")
            else:
                st.info("选择怀孕状态：")
            ### 复诊时间规范化
            st.subheader("其他辅助工具")
            col71, col72 = st.columns(2)
            with col71:
                st.link_button(
                    "点击此处了解T2DM复诊时间规范化系统",
                    "https://github.com/GuLifan/Diabetes-Evaluation-and-Follow-up-Prediction-System")
                # 成人2型糖尿病复诊时间规范化系统[简称：糖尿病复诊规范化]V1.0软著登记号:2025SR0014523
            with col72:
                # Streamlit 界面
                st.subheader("CGM 数据分析")
                daybefore = st.number_input("起始前一天 (例如 0):", min_value=0, value=0, step=1)
                duringday = st.number_input("计算天数 (例如 6):", min_value=1, value=6, step=1)
                hourbefore = daybefore * 24
                duringhour = duringday * 24
                minlennum = (duringday * 12 * 24) + 1
                uploaded_file = st.file_uploader("上传 CGM 数据文件", type=["xlsx", "csv", "xls"])
                if st.button("计算 CGM 数据") and uploaded_file:
                    with open("temp_file", "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    stats = process_patient_file("temp_file", minlennum, hourbefore, duringhour)
                    if stats:
                        st.success(f"计算结果如下：\n"
                                   f"患者ID: {stats['patient_id']}\n"
                                   f"开始时间: {stats['start_time']}\n"
                                   f"结束时间: {stats['end_time']}\n"
                                   f"平均值 (MEAN): {stats['MEAN']}\n"
                                   f"血糖管理指标 (GMI): {stats['GMI']}\n"
                                   f"标准差 (SD): {stats['SD']}\n"
                                   f"变异系数 (CV): {stats['CV']}\n"
                                   f"目标范围内时间 (TIR): {stats['TIR']}\n"
                                   f"高于目标范围时间 (TAR): {stats['TAR']}\n"
                                   f"低于目标范围时间 (TBR): {stats['TBR']}\n"
                                   f"低血糖风险指数 (LBGI): {stats['LBGI']}\n"
                                   f"高血糖风险指数 (HBGI): {stats['HBGI']}\n"
                                   f"平均每日风险范围 (ADRR): {stats['ADRR']}\n"
                                   f"日间血糖波动 (MODD): {stats['MODD']}")
                    else:
                        st.error("文件处理失败，请检查文件格式和数据量。")
                st.warning("本功能为测试功能，请勿上传重要数据！计算结果仅供参考，不能作为医学证据。")