### Main Introduction
# Name: Blood Glucose Calculator_Version_1.0_12191134
# #Developer: Leader: QiangWei; 1st_GuLifan
# Organization: The First Affiliated Hospital of Xi'an Jiaotong University
# Checking time: 2024.12.19_1st_Not Reviewed
# 注意，一定要将需要处理的文件复制而不是剪切，该程序会修改原始表格文件！
""""""
import os  # os库用于文件操作
import pandas as pd  # pandas库用于数据处理
import math  # math库用于数学计算
import glob
""""""
# 指定文件夹路径，在这里修改自己的需要处理的文件夹的路径。注意，一定要将需要处理的文件复制而不是剪切，该程序会修改原始表格文件！
folder_path = r"C:\Users\lifan\Desktop\10001"
""""""
def convert_excel_to_csv_and_delete(folder_path):
    # 获取文件夹内所有excel文件的路径
    excel_files = glob.glob(os.path.join(folder_path, '*.xlsx')) + glob.glob(os.path.join(folder_path, '*.xls'))
    for excel_file in excel_files:
        # 读取excel文件，跳过第一行
        df = pd.read_excel(excel_file, skiprows=1)
        # 获取csv文件的路径（将扩展名从.xlsx或.xls改为.csv）
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        # 将数据框保存到csv文件
        df.to_csv(csv_file, index=False)
        # 删除原始的excel文件
        os.remove(excel_file)
        print(f"Converted {excel_file} to {csv_file} and deleted the original file.")
# 调用函数执行转换和删除操作
convert_excel_to_csv_and_delete(folder_path)
""""""
# MAGE计算函数
def calculate_mage(ls_in, th):
    ls_out, flag_arrow = [], 0
    temp_max, temp_min = ls_in[0], ls_in[0]
    for i in range(1, len(ls_in)):
        now = ls_in[i]
        if flag_arrow == 0:  # 尚未确定波动方向
            temp_max, temp_min = max(temp_max, now), min(temp_min, now)
            if temp_max - temp_min >= th:
                flag_arrow = 1 if now == temp_max else -1
                ls_out.extend([temp_min, temp_max] if flag_arrow == 1 else [temp_max, temp_min])
        else:  # 已确定波动方向
            if (flag_arrow == 1 and now < ls_out[-1]) or (flag_arrow == -1 and now > ls_out[-1]):
                if abs(now - ls_out[-1]) >= th:
                    ls_out.append(now)
                    flag_arrow *= -1
                else:
                    ls_out[-1] = now  # 更新最后一个波谷或波峰值

    # 计算 MAGE
    mage = sum(abs(ls_out[i] - ls_out[i - 1]) for i in range(1, len(ls_out), 2)) / (len(ls_out) // 2) if len(
        ls_out) >= 2 else 0
    return mage, ls_out
""""""
# LBGI、HBGI、ADRR计算函数
def calc_lbgi_hbgi(df_in):
    df_in = df_in[df_in['BG'] != 0]
    df_in['BG'] = df_in['BG'].apply(lambda x: 1.0 if x < 1.0 else x)
    df_in['fbg'] = df_in['BG'].apply(lambda x: 1.794 * ((math.log(x)) ** 1.026 - 1.861))
    df_in['rbg'] = df_in['fbg'].apply(lambda x: 10 * (x ** 2))
    df_lbgi = df_in[df_in['fbg'] < 0]
    df_hbgi = df_in[df_in['fbg'] > 0]
    adrr = (sum(df_lbgi['rbg']) + sum(df_hbgi['rbg'])) / len(df_in)
    lbgi = df_lbgi['rbg'].mean() if not df_lbgi.empty else 0
    hbgi = df_hbgi['rbg'].mean() if not df_hbgi.empty else 0
    return lbgi, hbgi, adrr
""""""
# MODD计算函数
def calculate_modd(df_in):
    # 确保数据按日期排序
    df_in = df_in.sort_values(by='datetime')
    # 计算连续两天之间的血糖值差异
    df_in['day'] = df_in['datetime'].dt.date
    daily_diffs = df_in.groupby('day')['BG'].diff().abs().dropna()
    # 计算MODD
    modd = daily_diffs.mean()
    return modd
""""""
# 遍历文件夹中的所有文件
load_folder = folder_path
for filename in os.listdir(load_folder):
    file_path = os.path.join(load_folder, filename)
    if filename.endswith('.csv'):  # 读取 CSV 文件
        df = pd.read_csv(file_path)
        # df = df.iloc[1:]  # 去掉第一行
        df['datetime'] = pd.to_datetime(df.iloc[:, 0])  # 将第一列转换为datetime格式
        df['BG'] = df.iloc[:, 1].astype(float)  # 将第二列转换为浮点数
        try:
            ### GMI, MEAN, CV, SD
            MEAN = df['BG'].mean()  # 计算平均值MG
            # eA1c=(MEAN + 0.582) / 1.198
            GMI = 12.71 + 4.70587 * MEAN  # 计算GMI，执行mmol单位标准
            SD = df['BG'].std()  # 计算标准差SDBG
            CV = SD / MEAN  # 计算变异系数CV

            ### TIR TAR TBR TITR TIR-TITR
            total_rows = len(df)  # 总行数
            TIR = df[(df['BG'] >= 3.9) & (df['BG'] <= 10)].shape[0] / total_rows  # 3.9-10
            TAR = df[df['BG'] > 10].shape[0] / total_rows  # >10
            TBR = df[df['BG'] < 3.9].shape[0] / total_rows  # <3.9
            TITR = df[(df['BG'] >= 3.9) & (df['BG'] <= 7.8)].shape[0] / total_rows  # 3.9-7.8
            TIR_TITR = TIR - TITR

            ### 计算 MAGE和LAGE
            blood_glucose_list = df['BG'].tolist()  # 转为列表
            mage, peaks_and_valleys = calculate_mage(blood_glucose_list, th=SD)  # 假设波动阈值th是一个标准差
            lage = df['BG'].max() - df['BG'].min()

            ### 计算 LBGI HBGI ADRR
            lbgi, hbgi, adrr = calc_lbgi_hbgi(df)

            ### 计算MODD
            modd = calculate_modd(df)

            ### 计算凌晨 0 点到 6 点之间的平均值和标准差
            df_06 = df[(df['datetime'].dt.hour >= 0) & (df['datetime'].dt.hour < 6)]
            mean_06 = df_06['BG'].mean()
            sd_06 = df_06['BG'].std()
            cv_06 = sd_06 / mean_06
            df_60 = df[(df['datetime'].dt.hour >= 6) & (df['datetime'].dt.hour < 24)]
            mean_60 = df_60['BG'].mean()
            sd_60 = df_60['BG'].std()
            cv_60 = sd_60 / mean_60
            df_24 = df[(df['datetime'].dt.hour >= 2) & (df['datetime'].dt.hour < 4)]
            mean_24 = df_24['BG'].mean()
            sd_24 = df_24['BG'].std()
            cv_24 = sd_24 / mean_24

            # 显式创建副本，避免警告
            df_06 = df_06.copy()
            df_06['date'] = df_06['datetime'].dt.date
            # 找到每天的最小值及其对应时间
            df_min_06 = df_06.loc[df_06.groupby('date')['BG'].idxmin()]

            # 找到每天最接近凌晨2点的时间点
            def closest_to_2am(group):
                times = group['datetime']
                two_am = pd.to_datetime(group.name) + pd.Timedelta(hours=2)  # 使用group.name获取日期
                closest_time_idx = (times - two_am).abs().idxmin()
                return group.loc[closest_time_idx]
            # 应用函数找到每天最接近凌晨2点的血糖值
            df_closest_02 = df_06.groupby('date').apply(closest_to_2am).reset_index(drop=True)
            sd_2am = df_closest_02['BG'].std()
            # 找到每天最接近凌晨3点的时间点
            def closest_to_3am(group):
                times = group['datetime']
                three_am = pd.to_datetime(group.name) + pd.Timedelta(hours=3)
                closest_time_idx = (times - three_am).abs().idxmin()
                return group.loc[closest_time_idx]
            # 应用函数找到每天最接近凌晨3点的血糖值
            df_closest_03 = df_06.groupby('date').apply(closest_to_3am).reset_index(drop=True)
            sd_3am = df_closest_03['BG'].std()
            # 找到每天最接近凌晨4点的时间点
            def closest_to_4am(group):
                times = group['datetime']
                four_am = pd.to_datetime(group.name) + pd.Timedelta(hours=4)
                closest_time_idx = (times - four_am).abs().idxmin()
                return group.loc[closest_time_idx]
            # 应用函数找到每天最接近凌晨4点的血糖值
            df_closest_04 = df_06.groupby('date').apply(closest_to_4am).reset_index(drop=True)
            sd_4am = df_closest_04['BG'].std()

            ### 计算每天 2 点到 4 点的中位数平均值、最小值及其时间
            # 提取凌晨 2 点到 4 点的数据
            df_24 = df[(df['datetime'].dt.hour >= 2) & (df['datetime'].dt.hour < 4)]
            # 显式创建副本，避免警告
            df_24 = df_24.copy()
            df_24['date'] = df_24['datetime'].dt.date

            # 计算中位数的平均值
            median_24_MEAN = df_24.groupby('date')['BG'].median().mean()
            # 计算最小值的平均值
            min_24_MEAN = df_24.groupby('date')['BG'].min().mean()
            # 找到每天的最小值及其对应时间
            df_min_24 = df_24.loc[df_24.groupby('date')['BG'].idxmin()]
            """"""
            # 打印结果
            print(f"File: {filename}")
            print(f"GMI(mmol): {GMI:.2f}, MEAN: {MEAN:.2f}, SD: {SD:.2f}, CV: {100 * CV:.2f}%")
            print(f"------------")
            print(f"TIR: {100*TIR:.2f}%, TAR: {100*TAR:.2f}%, TBR: {100*TBR:.2f}%, TITR: {100*TITR:.2f}%, TIR-TITR: {100*TIR_TITR:.2f}%")
            print(f"------------")
            print(f"MAGE(此为14天数据)：{mage:.2f}, LAGE(此为14天的极值之差，不是每日数据): {lage:.2f}")
            print(f"------------")
            print(f"LBGI: {lbgi:.4f}, HBGI: {hbgi:.4f}, ADRR: {adrr:.4f}, MODD: {modd:.4f}")
            print(f"------------")
            print(f"0AM-6AM MEAN: {mean_06:.2f}, SD: {sd_06:.2f}, CV: {100 * cv_06:.2f}%")
            print(f"6AM-0AM MEAN: {mean_60:.2f}, SD: {sd_60:.2f}, CV: {100 * cv_60:.2f}%")
            print(f"2AM-4AM MEAN: {mean_24:.2f}, SD: {sd_24:.2f}, CV: {100 * cv_24:.2f}%")
            print(f"SD_2AM: {sd_2am:.2f}, SD_3AM: {sd_3am:.2f}, SD_4AM: {sd_4am:.2f}")
            print(f"------------")
            print(f"2AM-4AM 血糖中位数的多日均值: {median_24_MEAN:.2f}")
            print(f"2AM-4AM 血糖最小值的多日均值: {min_24_MEAN:.2f}")
            print(f"------------")
            print(f"每日 2AM-4AM 最低血糖值以及出现时间:")
            # 对于2AM-4AM的血糖数据
            print("2AM-4AM 最低血糖值及出现时间:")
            for _, row in df_min_24.iterrows():
                # 格式化时间，只显示到分钟
                formatted_time = row['datetime'].strftime('%Y-%m-%d %H:%M')
                print(f"2AM-4AM 最低血糖值: {row['BG']:.2f}, 出现时间: {formatted_time}")
            print("------------")
            # 对于0AM-6AM的血糖数据
            print("每日 0AM-6AM 最低血糖值以及出现时间:")
            for _, row in df_min_06.iterrows():
                # 格式化时间，只显示到分钟
                formatted_time = row['datetime'].strftime('%Y-%m-%d %H:%M')
                print(f"0AM-6AM 最低血糖值: {row['BG']:.2f}, 出现时间: {formatted_time}")
            print("------------\n------------")

        except Exception as e:
            print(f"Error processing file {filename}: {e}")
