def passwordGenerator(num, tab):
    import random
    kodi = []
    kodi = [0 for i in range(num)] 
    i = 0
    ln = len(tab)
    while i < num:

        
        r = random.randrange(0,ln)
        kodi[i] = tab[r]
        i = i + 1

    return kodi    

#A aB bC cD dE eF fG gH hI iJ jK kL lM mN nO oP pQ qR rS sT tU uV vW wX xY yZ z  

def printTab(tab):
    i = 0
    while i < len(tab):
        print(tab[i])
        i = i + 1





def main():
    print('Ju lutem pergjigjuni disa pyetjeve perpara se ne mund te gjenerojme nje password sipas deshirave tuaja! ' )
    num = input('Ju lutem vendosni nje nr per te treguar sa te gjate e doni passwordin: ')
    num = int(num)


    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print('tabela fillestare e karaktereve konsiston ne keto karaktere: ', printTab(tab))
    p = input('Deshironi te shtoni dhe karakteret ne uppercase: (true, false) ')
    p = bool(p)

    if p == True:
        tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    else:
        tab = tab    

    q = input('Deshironi te shtoni karaktere te tjera: ')
    q = bool(q)
    if q == True:
        tab = tab + ['.', ',', '@', '$', '_']
         
    else:
        tab = tab

    r = input('Deshironi te shtoni numra (1-9): ')
    r = bool(r)
    if r == True:
        tab = tab + [1, 2, 3, 4, 5, 6, 7, 8, 9]  

    else:
        tab = tab
    
    printTab(passwordGenerator(num, tab))

while True:
    answer = input('Pershendetje! Shtypni po nese doni te gjeneroni nje password te ri: ')
    if answer == 'po':
        main()
    else:
        break     
            








