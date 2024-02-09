idade = 41
tentativas = 3
rodada = 1
while (tentativas > 0):
  print('Você possui '+str(tentativas)+' tentaivas para descobrir! Iniciando a rodada '+str(rodada))
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
  tentativas = tentativas -1
  rodada = rodada +1
print('Eu tenho '+str(idade)+' anos.')
