# A = {1,2}  pares: (1,1) (1,2) (2,1) (2,2) mapeados em 4 bits
def classifica_funcao(r): #falta fazer
    return ""

def verifica_funcao(r,b):
    classe=""
    flag1=0
    for y in range(4):
        x=0
        if(b[x][y] == True):
            flag1 +=1
            if(flag1==1):
                y1=y

    flag2=0
    for y in range (4):
        x=1
        if(b[x][y] == True):
            flag2 +=1
            if(flag2==1):
                y2=y            
    flag3=0
    for y in range (4):
        x=2
        if(b[x][y] == True):
            flag3 +=1
            if(flag3==1):
                y3=y            
    flag4=0
    for y in range(4):
        x=3
        if(b[x][y] == True):
            flag4 +=1
            if(flag4==1):
                y4=y               
    if(r>4095 and (flag1==1 and flag2==1 and flag3==1 and flag4==1)):
        classe += "F"
        if(y1 != y2 and y1 != y3 and y1 != y4 and y2 != y3 and y2 != y4 and y3 != y4):
            classe += "Fb"
            classe += "Fi"
            classe += "Fs"
        else:
            classe += "Fs"
            
    return classe

def classifica(r,b):
    classe = ""
    # reflexividade
    # O 9 = 1001 se olhar na lista de binarios isto é [0,0][1,1] já o 73 = 1001001 = [0,0][1,1][2,2]
    reflexiva=False
    if (r>=513 and r&585==585) :
        classe += "R"
        reflexiva=True
        
    # simetria
    simetrica = False
    # o 4 = 100 , já o 2 = 10, se os 2 forem true tenho 2 conjuntos simetricos 0110 , [1,0][0,1], caso os 2 forem falsos 1001 = [0,0][1,1] também simetricos
   # b = [["","","",""],["","","",""],["","","",""],["","","",""]]
    #b[0][3]= r & 32768 == 32768 #9  0  
    #b[2][3]= r & 16384 == 16384 #9  0  
    #b[1][3]= r & 8192 == 8192 #9  0     
    #b[3][2]= r & 4096 == 4096 #9  0     
    #b[3][1]= r & 2048 == 2048 #9  0     
    #b[3][0]= r & 1024 == 1024 #9  0    
    #b[3][3]= r & 512 == 512 #9  0
    #b[2][0]= r & 256 == 256 #9  0
    #b[0][2]= r & 128 == 128 #8  0
    #b[2][2]= r & 64 == 64   #7  0
    #b[1][2] = r & 32 == 32  #6  1
    #b[2][1]= r & 16 == 16   #5  0
    #b[0][0] = r & 8 == 8    #4  0
    #b[0][1] = r & 4 == 4    #3  1
    #b[1][0] = r & 2 == 2    #2  0
    #b[1][1] = r & 1 == 1    #1  1

    
    if (b[0][1]==b[1][0] and b[2][1]==b[1][2] and b[0][2]==b[2][0] and b[0][3]==b[3][0] and b[2][3]==b[3][2] and b[1][3]==b[3][1]):
        classe += "S"
    # antisimetrica tá bugado.
    #if ((((r&1 ==1 and (r&2==2 or r&32 == 32)) or (r&8==8 and (r&4==4 or r&128==128)) or (r&64 == 64 and (r&256==256 or r&16 ==16 ))) and simetrica == False) and ((b01 and b10)==False) and ((b02 and b20) == False) and ((b12 and b21) == False) ) :
        #classe += "P"
        
    # transitividade
    transitiva = True
    for x in range (4):
        for y in range (4):
            if b[x][y]:
                for z in range (4):
                    if b[y][z]:
                       if not (b[x][z]):
                           transitiva=False
    if(transitiva == True):
        classe += "T"
            
    # irreflexividade
    if reflexiva==False:
        classe += "I"
        

        
    # funcao
    classe += verifica_funcao(r,b)
    classe += classifica_funcao(r)
    return classe

        
def imprime_relacao(relacao,r,b):
#aqui é simples de entender, para 9 relações se têm 111111111
# 1 = "têm a relação" 0="não têm a relação"
# quanto aos "==" também é simples, 1<<1 = 2^1 1<<2 = 2^2 ...
# como o ultimo conjunto é 256 = 100000000, a presença de todos conjuntos é 111111111 = 511.
#assim, sem fazer contas de combinações, sabe-se a quantia de conjuntos totais = 511
#com o número de combinações totais dentro de um for pode-se testar bit a bit de todos os conjuntos, dessa forma e retornado todas as funções
#ex: 2=10, 3=11 ... ao se passar o 2 Têm-se que (10 & 10 =2, 10 & 1 =0) assim apenas o conjunto 2 será usado
# para o 3(11&10 =2),(11&11=3),(11&01=1) assim o número 3 irá representar os conjuntos 1,2 e 3
        c=relacao[r]
        resp = '{'
        for i in range(4):
            for j in range(4):                
                if b[i][j]:
                    resp += "("+ str(i+1) + "," + str(j+1) +")"
        resp += '}'
        ref_arquivo.write(resp)
        ref_arquivo.write(" "+c)
        ref_arquivo.write("\n")
        
ref_arquivo = open("relacoes.txt","w")
resp = {}
for r in range(65536):
    if resp.get(r) == None:
        b = [["","","",""],["","","",""],["","","",""],["","","",""]]
        b[0][3]= r & 32768 == 32768 #9  0  
        b[2][3]= r & 16384 == 16384 #9  0  
        b[1][3]= r & 8192 == 8192 #9  0     
        b[3][2]= r & 4096 == 4096 #9  0     
        b[3][1]= r & 2048 == 2048 #9  0     
        b[3][0]= r & 1024 == 1024 #9  0    
        b[3][3]= r & 512 == 512 #9  0
        b[2][0]= r & 256 == 256 #9  0
        b[0][2]= r & 128 == 128 #8  0
        b[2][2]= r & 64 == 64   #7  0
        b[1][2] = r & 32 == 32  #6  1
        b[2][1]= r & 16 == 16   #5  0
        b[0][0] = r & 8 == 8    #4  0
        b[0][1] = r & 4 == 4    #3  1
        b[1][0] = r & 2 == 2    #2  0
        b[1][1] = r & 1 == 1    #1  1
        resp[r] = classifica(r,b)    
        imprime_relacao(resp,r,b)
ref_arquivo.close()