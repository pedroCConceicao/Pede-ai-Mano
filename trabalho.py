#Desenvolva o Pede aí, mano em codigo

#imports
import time
import os
import qrcode
Biblioteca Pillow para abrir a imagem
#from PIL import Image

#Produtos Hamburguer
produtosH = ['X-Bacon','Bacon Especial','X-Salada']
precoH = [18.90, 22.50, 16.00]

#Produtos Pizza
produtosP = ['Pizza Calabresa', 'Frango Catupiry', 'Pizza Doce'] 
precoP = [32.00, 35.00, 28.50]


#Carrinho
carrinho = []

#Apresente a loja e suas opções
print(f'''Olá, seja bem-vindo(a) a loja Pede aí, mano.

As opções disponiveis que temos para hoje é:
      
      1- Hambúrguer
      2- Pizza
''')
print('='*80)

#Faça o retorno do teclado
pedido = int(input('Qual das duas opções voce deseja? '))
print('='*80)

#if/else

if pedido == 1: 
    print('A opção escolhida foi Hambúrguer!')
    print('='*80)
    time.sleep(2)
    os.system('cls')    

    #Imprimir as opções na tela

    while True:
        print('='*80)
        print('''As opções de Hambúrguer disponivel é:
      
      1-  X-Bacon: R$18,90
      2-  Bacon Especial: R$22,50
      3-  X-Salada: R$16,0
      4- Para finalizar pedido''') 

        burguerop = int (input('Qual das opções voce deseja? '))

        if burguerop == 1:
            carrinho.append(('H', 0))
            print('='*80)
            print('A opção escolhida é X-Bacon')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)

        elif burguerop == 2:
            carrinho.append(('H', 1))
            print('='*80)
            print('A opção escolhida foi Bacon Especial')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)

        elif burguerop == 3:
            carrinho.append(('H', 2))
            print('='*80)
            print('A opção escolhida foi X-Salada')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)

        elif burguerop == 4:
            print('Encaminhando para a finalização das compras')
            time.sleep(3)
            print('='*80)
            break

        else:
            print('Opção invalida.')
            time.sleep(1)

#Opção Pizza
elif pedido == 2:
    print('A opção escolhida foi Pizza!')
    print('='*80)
    time.sleep(2)
    os.system('cls')

    while True:
        print('='*80)
        print('''As opções de Pizza disponivel é:
      
        1-  Pizza Calabresa - R$ 32.00
        2-  Frango Catupiry - R$ 35.00
        3-  Pizza Doce - R$ 28.50
        4- Para finalizar pedido''') 

        pizzaop = int(input('Qual das opções voce deseja? '))

        if pizzaop == 1:
            carrinho.append(('P', 0))
            print('A opção escolhida é Pizza Calabresa')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)
        elif pizzaop == 2:
            carrinho.append(('P', 1))
            print('A opção escolhida é Frango Catupiry')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)
        elif pizzaop == 3:
            carrinho.append(('P', 2))
            print('A opção escolhida é Pizza Doce')
            time.sleep(1.5)
            print('='*80)
            print('Adicionando ao Carrinho')
            time.sleep(2)
            print('='*80)
            print('Adicionado ao Carrinho!')
            time.sleep(2)
            print('='*80)
            
        elif pizzaop == 4:
            print('Encaminhando para a finalização das compras')
            time.sleep(3)
            print('='*80)
            break
        else:
            print('Opção invalida.') 

        
else:
    print('Opção invalida')


os.system('cls')

#Mostrar carrinho
print('='*80)
print('Os produtos do seu carrinho são:')
total = 0

for tipo, indice in carrinho:
    if tipo == 'H':
        print(f'{produtosH[indice]} - R${precoH[indice]:.2f}')
        total += precoH[indice]
    elif tipo == 'P':
        print(f'{produtosP[indice]} - R${precoP[indice]:.2f}')
        total += precoP[indice]
    print('='*80)

print(f'Total a pagar: R${total:.2f}')

time.sleep(2)
os.system('cls')

print('Redirecionando você para opção de pagamento')
time.sleep(2)
 
#opção de pagamento 
# Acrescentar pix, boleto e cartão
# Apresentar formas de pagamento

print('''Temos às seguintes opções de pagamento: 
1 - Pix
2 - Dinheiro Fisico
3 - Cartão''')

print('='*80)

pagamento = int(input('Quais dessas opções você deseja realizar seu pagamento? '))

print('='*80)

# Pix
if pagamento == 1:
    print('Você selecionou a opção Pix!')
    
    time.sleep(1)
    os.system('cls')
    print('='*80)
    print('Gerando QR Code para pagamento via Pix...')
    time.sleep(2)

#Chave pix
    chave_pix = "00020101021126330014BR.GOV.BCB.PIX0111183432046115204000053039865802BR5914Lucas Henrique6009SAO PAULO62080504daqr6304BB16"

#Gera o QRCode com esse texto
    qr = qrcode.make(chave_pix)

#Salva o QRCode como um arquivo de imagem
    qr.save("qrcode_pix.png")

#Abre a imagem gerada com Pillow
    img = Image.open("qrcode_pix.png")
    img.show()  # Isso vai abrir a imagem do QR Code
    print('='*80)

    time.sleep(3)
    print("Aguardando pagamento...")
    time.sleep(3)
    print('='*80)

    print('Pagamento sendo processado...')
    time.sleep(3)
    os.system('cls')
    print('='*80)
    
    print('Pagamento efetuado!')
    time.sleep(1.5)
    os.system('cls')
    print('='*80)
    
    print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
    print('='*80)
    time.sleep(2)
    os.system('cls')

#Dinheiro Fisico
elif pagamento == 2:
    print('Você selecionou a opção Dinheiro Fisico!')
    
    time.sleep(1)
    os.system('cls')
    print('='*80)
   
    print('Pagamento sendo processado...')
    time.sleep(3)
    os.system('cls')
    print('='*80)
    
    print('Pagamento efetuado!')
    time.sleep(1.5)
    os.system('cls')
    print('='*80)
    
    print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
    print('='*80)
    time.sleep(2)
    os.system('cls')

# Cartão
elif pagamento == 3:
    print('Você selecionou a opção Cartão!')
    
    time.sleep(1)
    os.system('cls')
    print('='*80)

    # Opções de parcelamento
    print('''Opções de parcelamento: 
    1x
    2x
    3x
    4x''')

    print('='*80)

    parcela = int(input('Quantas vezes deseja parcelar? '))

    time.sleep(0.5)
    os.system('cls')
    print('='*80)

    # Parcelado em 1x
    if parcela == 1:
        print('Pagamento sendo processado...')
        time.sleep(3)
        os.system('cls')
        print('='*80)
        print('Pagamento efetuado!')
        time.sleep(1.5)
        os.system('cls')
        print('='*80)
        print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
        print('='*80)
        time.sleep(2)
        os.system('cls')

    # Parcelado em 2x
    elif parcela == 2:
        print('Pagamento sendo processado...')
        time.sleep(3)
        os.system('cls')
        print('='*80)
        print('Pagamento efetuado!')
        time.sleep(1.5)
        os.system('cls')
        print('='*80)
        print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
        print('='*80)
        time.sleep(2)
        os.system('cls')

    # Parcelado em 3x
    elif parcela == 3:
        print('Pagamento sendo processado...')
        time.sleep(3)
        os.system('cls')
        print('='*80)
        print('Pagamento efetuado!')
        time.sleep(1.5)
        os.system('cls')
        print('='*80)
        print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
        print('='*80)
        time.sleep(2)
        os.system('cls')

    # Parcelado em 4x
    elif parcela == 4:
        print('Pagamento sendo processado...')
        time.sleep(3)
        os.system('cls')
        print('='*80)
        print('Pagamento efetuado!')
        time.sleep(1.5)
        os.system('cls')
        print('='*80)
        print('Obrigado por comprar em nossa loja, esperamos por você novamente!')
        print('='*80)
        time.sleep(2)
        os.system('cls')

    else:
        print('Opção inválida!')

else:
    print('Opção inválida!')
