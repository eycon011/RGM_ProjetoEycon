import subprocess
from datetime import datetime, timedelta

subprocess.run('cls', shell=True)

def formatar_valor(valor):
    return f"R$ {valor:.2f}".replace(',', '.')


try:
    inv =  (input("Escolha o tipo de investimento (CDB OU LCI): "))
    capital = float(input("Digite o valor do capital: "))
    taxa = float(input("Digite a taxa de juros mensal(em %): "))
    prazo = int(input('Digite o número de meses: '))

    input('\n Pressione Enter para calcular o montante...')

    montante = capital * (1 + taxa/100)**prazo
    hoje = datetime.now()   
    vencimento = hoje + timedelta(days=30*prazo)
except ValueError:
    print("Entrada inválida!\nInsira valores numéricos para o capital, taxa de juros e meses.")

    input("\nPressione Enter para sair...")

else: 
    print('\nResumo do investimento: ')
    print(f'Tipo de investimento: {inv}')
    print(f'Capital inicial: R$ {formatar_valor(capital)}')
    print(f'Taxa de juros: {taxa:.2f}%')
    print(f'Prazo: {prazo} meses')
    print(f'Montante: R$ {formatar_valor(montante)}')
    print('\nDatas: ')
    print(f'Aplicação: {hoje.strftime("%d/%m/%Y")}')
    print(f'Vencimento: {vencimento.strftime("%d/%m/%Y")}')

    input("\nPressione enter para sair...")