import akshare as ak

# 测试各个可能的接口
interfaces = [
    ("东方财富全A", "stock_zh_a_spot_em"),
    ("新浪全A", "stock_zh_a_spot_sina"),
    ("腾讯全A", "stock_zh_a_spot"),
    ("深市A股", "stock_sz_a_spot_em"),
    ("沪市A股", "stock_sh_a_spot_em"),
]

for name, func_name in interfaces:
    try:
        func = getattr(ak, func_name)
        df = func()
        print(f"=== {name} ({func_name}) 接口 ===")
        print(f"总行数: {len(df)}")
        print(f"列名: {list(df.columns)[:15]}")  # 只显示前15列
        print("是否包含市净率相关列:", any("市净率" in col or "pb" in col.lower() for col in df.columns))
        print()
    except Exception as e:
        print(f"{name} 接口失败: {str(e)[:100]}\n")
