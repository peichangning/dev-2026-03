import pandas as pd
import os

def main():
    # 1. 读取原始数据：读取本地的xlsx数据集文件
    print("正在加载数据集...")
    df = pd.read_excel('data/online_retail_II.xlsx')
    
    original_rows = len(df)
    print(f"原始数据总行数: {original_rows}")
    
    # 2. 删除完全重复的记录
    duplicate_count = df.duplicated().sum()
    print(f"发现完全重复数据: {duplicate_count} 条")
    df = df.drop_duplicates()
    
    # 3. 删除Customer ID为空的记录
    null_customer_count = df['Customer ID'].isna().sum()
    print(f"发现Customer ID为空的数据: {null_customer_count} 条")
    df = df.dropna(subset=['Customer ID'])
    
    # 4. 删除Quantity小于等于0的记录
    invalid_quantity_count = len(df[df['Quantity'] <= 0])
    print(f"发现Quantity无效(<=0)的数据: {invalid_quantity_count} 条")
    df = df[df['Quantity'] > 0]
    
    # 5. 删除Price小于等于0的记录
    invalid_price_count = len(df[df['Price'] <= 0])
    print(f"发现Price无效(<=0)的数据: {invalid_price_count} 条")
    df = df[df['Price'] > 0]
    
    # 6. 把InvoiceDate转成正确的日期时间格式
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print("已将InvoiceDate转换为日期时间格式")
    
    # 7. 准备输出目录
    os.makedirs('output', exist_ok=True)
    
    # 8. 导出清洗后的结果
    cleaned_rows = len(df)
    output_csv = 'output/cleaned_retail.csv'
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"清洗后的数据已导出到: {output_csv}")
    
    # 9. 生成并输出统计信息
    summary = f"""数据清洗统计信息
====================
原始数据总行数: {original_rows}
清洗后数据总行数: {cleaned_rows}
删除重复数据: {duplicate_count} 条
删除空Customer ID数据: {null_customer_count} 条
删除无效Quantity数据: {invalid_quantity_count} 条
删除无效Price数据: {invalid_price_count} 条
"""
    print("\n" + summary)
    
    # 写入统计信息文件
    summary_file = 'output/summary.txt'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"统计信息已写入到: {summary_file}")
    
    print("数据清洗任务完成！")

if __name__ == "__main__":
    # 切换到脚本所在目录，保证路径正确
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
