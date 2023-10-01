print('Calculadora Python')
print('------------------')
print('Insira uma operação para seguir:')
print('------------------')
print('1: Adição')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')

operacao = input('Operação escolhida: ')

primeiro = float(input('Insira o primeiro valor: '))
segundo = float(input('Insira o segundo valor: '))

if operacao == '1':
    soma = primeiro + segundo
    print(f"{primeiro} + {segundo} = {soma}")

elif operacao == '2':
    sub = primeiro - segundo
    print(f"{primeiro} - {segundo} = {sub}")

elif operacao == '3':
    mult = primeiro * segundo
    print(f"{primeiro} x {segundo} = {mult}")

elif operacao == '4':
    div = primeiro / segundo
    print(f"{primeiro} x {segundo} = {div}")