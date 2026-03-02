import akshare as ak

# 使用新浪财经接口获取全市场A股数据（包含市净率）
df = ak.stock_zh_a_spot()

# 查看数据结构，确认包含市净率字段
print(df.columns.tolist())  # 输出列名，确认有 'pb'

# 统计破净股占比
total_stocks = len(df)
below_pb_count = len(df[df['pb'] < 1])
ratio = below_pb_count / total_stocks

print(f"全市场股票总数: {total_stocks}")
print(f"破净股数量: {below_pb_count}")
print(f"破净股占比: {ratio:.2%}")
