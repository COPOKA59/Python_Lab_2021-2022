N=M=int(input('Сколько чисел(N) в последовательности(N>2): '))
P=1
for i in range(1,M):
    P=P*(1-1/(N*N))
    N=N-1
print('Сумма чисел в последовательности равна: ', "{:1.5f}".format(P))