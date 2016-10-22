import sys

def hundreds(i):
    if isinstance(i,int) == False:
        print('Invalid input, please supply an integer')
        sys.exit()
    if i > 999:
        print('Invalid input, integer is too large for the hundreds function')
        sys.exit()
    wrdig=['one','two','three','four','five','six','seven','eight','nine']
    wrteen=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    wrtens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    strnum = str(i)
    if len(strnum) > 3:
        sys.exit('Invalid input, integer is too large')
    wrhund = ''
    if len(strnum) == 3:
        if int(strnum[0]) != 0:
            wrhund = wrhund + wrdig[int(strnum[0])-1] + ' hundred'
            strnum = strnum[1:]
            if int(strnum) != 0:
                wrhund = wrhund + ' and '
        else:
            strnum = strnum[1:]
    if len(strnum) == 2:
        if int(strnum[0]) == 1:
            wrhund = wrhund + wrteen[int(strnum[1])]
            strnum = ''
        elif int(strnum[0]) != 0:
            wrhund = wrhund + wrtens[int(strnum[0])-2]
            strnum = strnum[1:]
            if int(strnum) > 0:
                wrhund = wrhund + '-'
        else:
            strnum = strnum[1:]
    if len(strnum) == 1:
        if int(strnum) != 0:
            wrhund = wrhund + wrdig[int(strnum)-1]
    return wrhund

def n2t(i):
    if isinstance(i,int) == False:
        print('Invalid input, please supply an integer')
        sys.exit()
    if i >= int(1e36):
        print('Invalid input, integer too large')
        sys.exit()
    beyond=['thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion']
    groups = format(i,',').split(',')
    wrnum = ''
    while len(groups) > 1:
        if int(groups[0]) != 0:
            hund = hundreds(int(groups[0]))
            wrnum = wrnum + hund + ' ' + beyond[len(groups)-2] + ' '
        del groups[0]
    wrnum = wrnum + hundreds(int(groups[0]))
    wrnum = wrnum.strip()
    if wrnum == '':
        wrnum = 'zero'
    return wrnum

