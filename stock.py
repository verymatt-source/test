# 1. 导入库
import akshare as ak
from datetime import datetime

print("步骤1: 导入库完成")

# 2. 获取数据
print("步骤2: 开始获取股票数据...")
try:
    stock_df = ak.stock_zh_a_spot_em()
    print(f"步骤2: 获取成功，共 {len(stock_df)} 行数据")
except Exception as e:
    print(f"步骤2: 获取失败 - {e}")
    exit(1)

# 3. 生成文件名
filename = f'stock_data.csv'
print(f"步骤3: 将保存到当前目录下的 {filename}")

# 4. 保存CSV
print("步骤4: 正在保存CSV文件...")
try:
    stock_df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"步骤4: 保存成功！文件: {filename}")
except Exception as e:
    print(f"步骤4: 保存失败 - {e}")
    exit(1)

# 5. 完成
print("步骤5: 脚本执行完成！")
print(f"数据已保存到: {filename}")