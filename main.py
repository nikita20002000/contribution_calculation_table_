labels = ('Месяц', 'Сумма на вкладе', 'Начисление')
p, y, I = input().split()
p, y, I = int(p), int(y), float(I)

with open('output.csv', 'w') as csv_file:
    print(*labels, sep=',', file=csv_file)
    for i in range(y * 12):
        k_0 = I / 12
        k_1 = p * k_0 / 100
        p += (p * k_0 / 100)

        print(f"{i + 1},{p:0.2f},{k_1:0.2f}", file=csv_file)
