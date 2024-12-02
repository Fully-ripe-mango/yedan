import json

# 文件路径，使用原始字符串来处理包含中文字符的路径
file_path = r'液氮\液氮数据.txt'

# 初始化两个空列表来存储时间和电压
time = []
voltage = []

# 打开并读取文件
with open(file_path, 'r') as file:
    for line in file:
        # 移除行末的换行符并分割数据
        parts = line.strip().split('\t')  # 按制表符分割
        if len(parts) == 2:  
            # 将时间和电压添加到对应的列表
            time.append(float(parts[0]))    # 时间
            voltage.append(float(parts[1]))  # 电压

# 创建字典并存储时间和电压数据
dingbiao = {}
dingbiao["time"] = time
dingbiao["voltage"] = voltage

# 将数据写入 JSON 文件
with open("yedan.json", "w", encoding="utf-8") as file2:
    json.dump(dingbiao, file2, indent=4, ensure_ascii=False)  # 保证中文字符能正确写入

print("数据已成功保存到 dingbiao.json")
