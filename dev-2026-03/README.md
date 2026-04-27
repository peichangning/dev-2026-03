# dev-2026-03 电商零售数据清洗项目

## 项目简介
这是一个使用 Python 和 pandas 完成的电商零售数据清洗项目，针对Online Retail II数据集完成基础数据清洗，去除脏数据并导出清洗后的结果。

## 我完成的内容
- 读取原始数据（支持读取本地的xlsx格式原始数据集）
- 删除完全重复的记录
- 删除 Customer ID 为空的记录
- 删除 Quantity <= 0 的无效记录
- 删除 Price <= 0 的无效记录
- 将 InvoiceDate 转换为标准的日期时间格式
- 导出清洗后的结果到 `output/cleaned_retail.csv`
- 生成并输出基础清洗统计信息，同时保存到 `output/summary.txt`

## 我的实现思路
### 1. 数据读取
使用 pandas 的 `read_excel` 读取原始的xlsx格式数据集，同时脚本会自动切换到自身所在目录，保证文件路径的正确性，避免路径错误。
### 2. 数据清洗
按照题目要求，依次完成各项清洗操作，每一步都统计了删除的记录数量：
1. **去重处理**：首先统计并删除完全重复的行记录，避免重复数据对后续分析造成干扰
2. **客户信息过滤**：过滤掉Customer ID为空的记录，保证客户信息的完整性
3. **数量有效性过滤**：过滤掉Quantity小于等于0的记录，这类记录通常是取消订单或者无效的退货数据
4. **价格有效性过滤**：过滤掉Price小于等于0的记录，去除免费商品或者无效的异常价格记录
5. **日期格式转换**：将InvoiceDate字段转换为pandas的datetime类型，统一日期格式，方便后续的时间相关处理
### 3. 导出结果
脚本会自动创建output目录，将清洗完成后的数据集导出为utf-8编码的csv文件，保证不同系统的兼容性。
### 4. 统计信息
在处理过程中统计各项数据的变化，包括原始行数、清洗后行数，以及每一步删除的记录数量，将这些信息打印到终端，同时保存到summary.txt文件中，方便查看清洗的整体效果。

## 运行方式
1. 创建并激活虚拟环境（按照项目要求）
```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
2. 安装依赖
```bash
pip install -r requirements.txt openpyxl
```
3. 下载数据集
你可以从[Kaggle数据集页面](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)下载原始数据集，将下载得到的`online_retail_II.xlsx`文件放到项目的`data/`目录下。
4. 运行清洗脚本
```bash
python main.py
```

## 输出说明
运行完成后，会在`output/`目录下生成两个文件：
1. `cleaned_retail.csv`：清洗完成后的数据集，可直接用于后续分析
2. `summary.txt`：数据清洗的统计信息，记录了原始数据、清洗后数据的行数，以及各步骤删除的记录数量
