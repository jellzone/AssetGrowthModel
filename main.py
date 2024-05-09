def calculate_growth(C, Kr, L, S, E, P, T):
    return C * Kr * (L**T) * (S**P) * (E**T)

def get_input(prompt, min_value, max_value, description, is_int=False):
    print(description)
    while True:
        try:
            if is_int:
                value = int(input(prompt))
            else:
                value = float(input(prompt))
            if value < min_value or value > max_value:
                print(f"输入的值必须在 {min_value} 和 {max_value} 之间。")
            else:
                return value
        except ValueError:
            print("输入的值必须是一个数字。")

def main():
    print("欢迎使用资产增长模型！")
    C = get_input("请输入你的胆魄（C）: ", 0.1, 2.0, "胆魄反映了一个人愿意承担的风险程度。范围：0.1 - 2.0。在这个范围内，2.0证明你可以承担你现有总资产2倍的负债，1.5表示你可以承担你现有总资产1.5倍的负债，1.0表示你可以承担你现有总资产的负债，0.5表示你可以承担你现有总资产50%的负债，0.1表示你只能承担你现有总资产10%的负债。")
    Kr = get_input("请输入你的知识储备（Kr）: ", 0.1, 2.0, "知识储备反映了你在投入项目立项时的知识水平。范围：0.1 - 2.0,2.0 代表你是该领域的专家，0.1 代表完全不熟悉该领域，1代表在该领域工作过1年，建议该领域每工作增加1年数值增加0.1")
    L = get_input("请输入你的学习能力（L）: ", 1.0, 1.1, "学习能力反映了你每年增长的知识比例。范围：1.0 - 1.1")
    S = get_input("请输入你的项目成功率（S）: ", 0.5, 1.0, "项目成功率反映了你的项目成功的概率。范围：0.5 - 1.0")
    E = get_input("请输入你的外部环境因子（E）: ", 0.7, 1.5, "外部环境因子反映了外部环境对你的资产增长的影响。范围：0.9 - 1.1，行业年增长率10%为1.1，年增长率20%为1.2")
    P = get_input("请输入你的项目尝试次数（P）: ", 1, 10, "项目尝试次数反映了你在一定时间内可以尝试的项目数量。范围：1 - 10", True)
    T = get_input("请输入你的投资时间（以年为单位）: ", 1, 100, "投资时间是你计划投入的年数。范围：1 - 100", True)

    growth = calculate_growth(C, Kr, L, S, E, P, T)

    print(f"你的预期 {T} 年资产增长为你现在年收入的：{growth:.2f} 倍")

    if growth <= 1:
        print("看来你需要更多的努力！")
    elif growth <= 10:
        print("不错，你的成长在正轨上！")
    else:
        print("哇，你的增长潜力无限！")

    # 检查用户输入的数值是否低于平均值
    low_values = []
    if C < 1.0:
        low_values.append("胆魄（C）")
    if Kr < 1.0:
        low_values.append("知识储备（Kr）")
    if L < 1.05:
        low_values.append("学习能力（L）")
    if S < 0.75:
        low_values.append("项目成功率（S）")
    if E < 1.0:
        low_values.append("外部环境因子（E）")

    if low_values:
        print(f"您输入的 {', '.join(low_values)} 数值低于平均数值，在这些方面需要努力提升哦。")

main()
