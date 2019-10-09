'''
Aluno: João Otavio Martini Korczovei
RA: 1817833
JOGO DA FORCA
'''
from getpass import getpass
def forca():
    p=getpass('Informe a palavra do jogo da forca: ')
    print(50*'==--------====--------====--------====--------====--------====--------====--------====--------====--------====--------====--------====--------==''\n')
    p2=len(p)*'_'
    p3=p2
    erros=0
    tdletra=''
    print(len(p),'letras')
    while erros<6 and p!=p2:
        letra=input('Letra: ')
        p2=''
        for l in range(len(p)):
            if letra==p[l]:
                p2+=p[l]
            else:
                p2+=p3[l]
        
        if letra not in p:
            erros+=1
        if erros==0:
            print('Erros:',erros)
            print('|--|')
            print('|')
            print('|')
            print('|')
            print('|','\nPalavra:',p2)
            print(20*'=')
        if erros==1:
            print('Erros:',erros)
            print('|--|')
            print('|  o')
            print('|')
            print('|')
            print('|','\nPalavra:',p2)
            print(20*'=')
        if erros==2:
            print('Erros:',erros)
            print('|--|')
            print('|  o')
            print('|  |')
            print('|')
            print('|','\nPalavra:',p2)
            print(20*'=')
        if erros==3:
            print('Erros:',erros)
            print('|--|')
            print('|  o')
            print('| -|')
            print('|')
            print('|','\nPalavra:',p2)
            print(20*'=')
        if erros==4:
            print('Erros:',erros)
            print('|--|')
            print('|  o')
            print('| -|-')
            print('| /')
            print('|','\nPalavra:',p2)
            print(20*'=')
        if erros==5:
            print('Erros:',erros)
            print('|--|')
            print('|  o')
            print('| -|-')
            print('| / \\')
            print('|','\nPalavra:',p2)
            print(20*'=')
        tdletra+=letra+' '
        print('Letras ja digitadas:',tdletra)
        if p2==p:
            print('Parabéns, você acertou a palavra secreta')
        p3=p2
        if erros==5:
            print('ENFORCADO, a palavra era:',p)
forca()
