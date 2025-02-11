
while True:

    n1 = int(input('De um número:'))
    n2 = int(input('De um número:'))
    print('1:Soma\n2:Subtração\n3:Multiplicação\n4:Divisão\n5:Quadradon\n6:Divisão Inteira\n7:Resto da Divisão')

    escolha = int(input('\nEscolha uma Opção:'))

    match escolha:
        case 1:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1,n2,soma))
        case 2 :
            subtracao = n1 - n2
            print('{} - {} = {}'.format(n1,n2,subtracao))
        case 3 :
            multiplica = n1 * n2
            print('{} x {} = {}'.format(n1,n2,multiplica))
        case 4:
            divisao = n1 / n2
            print('{} / {} = {}'.format(n1,n2,divisao))
        case 5:
            quadrado = n1 ** n2
            print('{} ** {} = {}'.format(n1,n2,quadrado))
        case 6:
            divisaointeira = n1 // n2
            print('{} // {} = {}'.format(n1,n2,divisaointeira))
        case 7:
            restodivisao = n1 % n2
            print('{} % {} = {}'.format(n1,n2,restodivisao))
        case _:
            print('Erro!! Por favor, escolha uma opção válida.')

    continuar = input("\nDeseja realizar outro cálculo? (sim/não)").strip().lower()
    if continuar not in ['sim','s']:
        print('Encerrando Programa!!')
        break