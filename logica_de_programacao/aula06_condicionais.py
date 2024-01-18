# if / elif / else

nomeUsuario = input('Qual seu nome? ')
senhaUsuario = input('Digite sua senha: ')

if senhaUsuario == '':
    print(f'{nomeUsuario}, você não preencheu o campo de senha.')
elif senhaUsuario != 'abc123':
    print('Digite sua senha novamente, {}.'.format(nomeUsuario))
else:
    print(f'Parabéns, {nomeUsuario}, você entrou no sistema.')

