inicio= int(input('Digite o inicio do intervalo: '))
final= int(input('Digite o final do intervalo: '))
soma= 0
pares= True

for i in range(inicio , final + 1 ):
    if i % 2 == 0:
       soma += i
       pares= True
       
else:
    if pares == False:
       print("Não ha numeros pares no intervalo!")
    else:
       print(f'A soma dos numeros pares é {soma}')
     
    

    

        
        