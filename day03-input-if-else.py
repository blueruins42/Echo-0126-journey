# Day 3: input() 函数 + if / elif / else 条件判断
# 目标：学会从用户获取输入，根据输入内容执行不同分支

print("欢迎体验条件判断练习程序")
print("请输入你的选择，我会给出对应回应。\n")

# 获取用户输入，并去除首尾空白
choice = input("请输入一个词（开心 / 累 / 饿 / 其他）：").strip()

# 把输入转为小写，便于比较（忽略大小写差异）
choice_lower = choice.lower()

# 使用 if-elif-else 进行多分支判断
if choice_lower == "开心":
    print("很好！保持这种状态。")
elif choice_lower == "累":
    print("辛苦了，记得适当休息。")
elif choice_lower == "饿":
    print("快去吃点东西吧，别饿着。")
else:
    print(f"收到：{choice}。已记录。")

# 额外交互：询问是否继续
again = input("\n要再试一次吗？（是 / 否）：").strip().lower()

if again == "是":
    print("好的，再来一次！\n")
    # 这里可以复制上面的代码实现循环，但为了保持简单，先不加
else:
    print("练习结束，感谢参与。")
