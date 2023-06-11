import os
import json
import subprocess

# 检查所需模块是否存在，如果不存在，则安装它们
missing_modules = []
try:
    import openpyxl
except ImportError:
    missing_modules.append('openpyxl')

try:
    import xlrd
except ImportError:
    missing_modules.append('xlrd')

try:
    import csv
except ImportError:
    missing_modules.append('csv')

if missing_modules:
    print(f"缺少以下模块: {', '.join(missing_modules)}")
    print("正在安装模块，请稍候...")
    venv_dir = os.path.join(os.path.dirname(__file__), "..", "env")
    pip_cmd = os.path.join(venv_dir, "Scripts", "pip")
    install_cmd = f"{pip_cmd} install {' '.join(missing_modules)}"
    subprocess.check_call(install_cmd, shell=True)
    print("模块安装完成！继续执行脚本...")
else:
    print("支持 .xlsx .csv .xls")

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = input("请输入数据源文件路径: ")
# 判断文件类型并加载数据
file_extension = os.path.splitext(file_path)[1]
if file_extension == ".xlsx":
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active
    data = worksheet.iter_rows(min_row=2, values_only=True)
elif file_extension == ".csv":
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 跳过标题行
        data = reader
elif file_extension == ".xls":
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_index(1)
    data = [worksheet.row_values(i) for i in range(1, worksheet.nrows)]
else:
    raise ValueError("不支持的文件格式")

results = []

for row in data:
    instruction = row[0]
    output = row[1]
    MBTI = row[2]


    result = {"instruction": instruction, "input":"", "output": output, "MBTI":MBTI}

    results.append(result)

output_file_path = os.path.join(script_dir, "loradata.json")

with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(results, output_file, ensure_ascii=False, indent=4)

print("已保存到 loradata.json 文件...")
