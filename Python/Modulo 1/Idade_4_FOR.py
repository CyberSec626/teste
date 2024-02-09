idade = 41
tentativas = 5
for rodada in range (0, tentativas):
  print('Iniciando a rodada '+str(rodada+1))
  palpite = int(input('Descubra minha idade: '))
  acertou = palpite == idade
  maior = palpite > idade
  menor = palpite < idade
  if (acertou):
    print('Acertou!')
    break
  elif (maior):
    print('Errou! Seu palpite foi maior que a minha idade')
  elif (menor):
    print('Errou! Seu palpite foi menor que a minha idade')
print('Eu tenho '+str(idade)+' anos.')
