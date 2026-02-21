# Day4：list(列表) + for 循环 - while 循环基础
# 目标：学会添加列表、添加元素、遍历列表、用循环收集用户输入

print("请输入几条内容，最后输入 '结束' 停止。")

# 创建一个空列表
items = []

# 用 while True 实现“无限输入直到退出”
while True:
    user_input = input("请输入一条内容（输入 '结束' 退出）：").strip()
    
    if user_input.lower() == "结束":
        break  # 退出循环
    
    if user_input:  # 避免添加空字符串
        items.append(user_input)
        print(f"已添加：{user_input}")
    else:
        print("输入为空，请重新输入。")

# 遍历列表并输出（带序号）
print("\n你输入的内容总结：")
if items:
    for index, value in enumerate(items, start=1):
        print(f"{index}. {value}")
    
    print(f"\n总共 {len(items)} 条。")
else:
    print("没有输入任何内容。")
