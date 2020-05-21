import pandas as pd #pandas version 1.0.1
import os
import time

log_users = []
log_passwords = []
log_data_dict = dict()

present_username = ""
present_password = ""

accounts = []
passwords = []
data_dict = dict()


def hash(para):
    def enc(string):
        l = len(string)
        temp1 = "qwertyuioplkjhgfdsazxcvbnm"
        j = 0
        s = []
        for i in string:
            s.append(ord(i) + l)
            s[j] = temp1[s[j] % 25]
            j += 1
        return "".join(s)

    def ordval(string):
        v = 0
        for i in string:
            v += ord(i)
        v += 321 - 123
        return (v % ord(string[-1])) % 100

    key = ['flxmlbwkmhncbmsjivwfcktmcljvsxsr',
           'dgueovqpwtrcwzmgusnmfhahkkywffzx',
           'hvjmtlfnratgyhsmzynupktrljfqnazl',
           'hfhwixkojhqnczgikjsjjhlrkpsxmzzx',
           'yipzyzcizhunignnzbfeqhmsgzqntwad',
           'cqwayhbtxbotqufmhjlpiynhxnntpakx',
           'dbmgprdnzhcxfeqesghtnphavncwjuyg',
           'xuzfiqgrknfkwukjaxzxsqtepstwthnu',
           'dpmsjylggzqclvrkjvbkfgjdatiygxnh',
           'icwqzlcenwnhenpqbfgoevekpnnsogfi',
           'cmnipkvbppwmdukaiegnujhvayepdogw',
           'kbnfcggfvyyroqkfaayqvililoldgrsn',
           'klnlfuqjbvhugnyirmwovzbuacmyubik',
           'uzjysmjlqiwtnydrwrmglsctvnhoiikh',
           'nszrijoyxgztettahewlzqmrwxflhvrk',
           'uoddmbtqxrhercqqctjvjcjxzyugrfrm',
           'jeyydzpaegrmzvrvmmuybokvawyyzxwd',
           'myljjwromxksqpuhfvztbldupyosplau',
           'ztbyweevrekkvxejwzgmcvqmpzadnbaf',
           'umqcrwsgqbbjbqbadoyjellvdwotsurv',
           'xodybnuuwrijbwqezwjosvimvtoitceh',
           'yiculwmuhobqesxivlhpquvlmcftgjya',
           'bcxlggsgjtlhlkepwbjxthvarcjfbghu',
           'wfzojbvmdnmoivmctzuiwbrfluwyhodd',
           'inpjcszcwbpujghpwwsweteyotsbdiru',
           'jnrhkxznawlchypporrpgskzxlilqdwh',
           'qnitthhvupkkxazxgaqewzzjpmutvqha',
           'iuechlexptrijnsbtejjeaddftrkzfut',
           'hsaymimhpkmpgxxcrekxvpihdhgkheox',
           'gbbmekjhrkpueuriurtlpxviaxdotwbe',
           'jxezpezyvfnsbgucimwmymkogqcvfdvw',
           'rupaggrcglaiwqnofqgeiqcufucvikcg',
           'vrfhdawkwrjhyvwlklmveiwhbrvptpfp',
           'gbuddognpaxvtelbruzflykchtsiwtit',
           'zhjaponowhhwtsiqqujtertoalzutukq',
           'mqgyukxoqmcxlfgucrsoksmzogpbauay',
           'faabnxfodpccahlspcbesrqcmomjygth',
           'zjhqigbehybqdwbrhxupcsanimhzhwxs',
           'ciirldodzummalywyamsgnbviodngqic',
           'inxedbvcynxiwbmbocssqmtvqyiozigu',
           'lpajhebmfnxgzzkvijgclacydklwdetw',
           'zuxsbwetotacdnzpvawsfroufptsiile',
           'xbifgqdnbxqtlbdyonnieauswfpcwauz',
           'exsjcvcvowgyfxocrcoiwmusubrqybtj',
           'xecdjljhltevrgtfymbnigfusvfrcayb',
           'lmuxfhvcylhpifvhuvrftzxhkbcoekgt',
           'xrurqbuydqboyevevvedbqpamiyqmimz',
           'wrlhvlbbhlfkuryniatjytzasbjxurhq',
           'kphqnenjojewbpperkjbjvsjoqhjakct',
           'spajyykxjyqhgdlxfmbzfqmncsvuccwk',
           'hdfiixghlerpkvnnsnzrrxxqcuxekqpn',
           'chpbywvpgehivyxmrdpmqjfuuszhfggu',
           'jjjesavlqwlbkxrsuwgrlgqybarckwrj',
           'uokpbvfiwxgfrjgadrjqxuauzcjerlua',
           'rxhlsgvclvzymudoahcndosjhdtsahkf',
           'ycwjponhmbxvowkjnuggnyejafyjcqvv',
           'glebrjfkpzkiipqanmdoujqyxzlhssal',
           'ykajmitfdgvaadhccgytxttavhdfhdzg',
           'fxmogafqtjkugbjzhkxmndootmzdkpyd',
           'lpwvjikbaijcatjrksdmwrvhydehywps',
           'rlsobhodbodzwfkoiktyqqqhauxsrpuq',
           'jgcltghwvnydjculpqjcinzqmwkposli',
           'bwwbhhrpufpbmsvwafnuhslwlwzoahwd',
           'bbpolsdrpoltxnbdhcseopfbeifwdysm',
           'omasseojktawzyfxcikrtmmrgvmkansd',
           'gcpiqdrotrpnoiqwywolibgrrbfmygjo',
           'kzrislkzjtexnghwboennnoqxmebeltb',
           'gtppbnyyxthmvdiphappmvzffftukbnh',
           'ognshhjszlppzszyluamblocepwmvcsg',
           'ttizybvujjrfmtypbuftwdhchxmldicc',
           'vwrekcggklzlkgizjbhcfgxmgozytdjk',
           'wmpwwtaqhivwsycqeqoyrxrsdivyukpv',
           'zqgjckyzaybgvcdrlsgpwjzgnoetiipc',
           'pkbkvleunngbtwxbvxfupeiywpmsnvyy',
           'gqqowxcawyalxjvegfcmesgamwygvwdw',
           'srrepwwiadyzlvyeeekrexnxdmuqgxjw',
           'ewfwhdwhlupwivevucncxhbzxjnqjocw',
           'mvewfgsuybdciduinqlrbvadcdoeokhw',
           'arqundivsfguwxhkyjdzcobdhvrlpfws',
           'eektuhgxpxkpkuzenrctnxrxnydyfvto',
           'emtxkapijmylzqquaxhwhmsoffwbfiwy',
           'enbjchxbuienhubdclmxaysjpbivkhrb',
           'xiwxrgddurumuqlzbkxuzaeumravygux',
           'qlutclzaneirupkzmxkvvxlhlezgzlfv',
           'lxwrayrhowxaducaodpnfmlwfmjidolj',
           'bbdudpkrjqztpwrchbahjktxbeacyjka',
           'einzdhlxqgtlnlohwciqwcjlcqhbhzze',
           'plajsodtslfycsxeoibywmsudoujcdsc',
           'yhgzlruckjaptxypxdbnwvzttltwrios',
           'qguqjvjqrksmlkozhedkifuankwenbpm',
           'ufgkhoutdhcathwhixmvhdiasjncuvqf',
           'thkfbjflywfwoagapraiumxjlqbnbqjo',
           'owwdgbyzfccblcnausnysthspfchfgpf',
           'ovrmkpforpadlwadaynvnoltzdhbhiio',
           'dqoerrqriibxbttjuwadcbmzaiyqhukv',
           'susipdgmoidtcllznepaoimcscidvkvf',
           'zntkphcnpdseakqalhxmlmouhfwncfwo',
           'rahbdcbfbpjewybayxqjglgoiqdyleep',
           'qvpniktgjvxscezhtinszcpfpoojkfbk',
           'rwgfpiuvtnqrqsgtowkctjgzdelulcxe']

    l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    data = para
    ov = int(ordval(data))
    en = enc(data)

    k = 0
    for i in range(8):
        for j in range(4):
            l[i][j] = key[ov][k]
            k += 1

    x = 0
    y = -1
    for i in en:
        l[x][y] = i
        if x == 7:
            x = 0
            y = -1
        else:
            x += 1
    y = ""
    for i in range(len(l)):
        for j in l[i]:
            y += j
    return y

def encrypt(string):
    temp = ""
    for i in string:
        temp += chr(ord(i) + 5)
    return temp


def decrypt(string):
    temp = ""
    for i in string:
        temp += chr(ord(i) - 5)
    return temp


def log_init():
    global log_users
    global log_data_dict
    global log_passwords

    try:
        temp = pd.read_csv('.log.csv')
        log_users = list(temp["@$D!_*"])
        log_passwords = list(temp["&#|K}"])
        log_data_dict = dict(zip(log_users, log_passwords))
        temp.to_csv('.log.csv', index=False)
        return 0
    except:
        temp = pd.DataFrame({'@$D!_*': [], '&#|K}': []})
        temp.to_csv('.log.csv', index=False)
        log_init()


def log_final():
    global log_users
    global log_data_dict
    global log_passwords

    temp = pd.DataFrame({'@$D!_*': log_users, '&#|K}': log_passwords})
    temp.to_csv(".log.csv", index=False)


def log_ststus(user, pas='0'):
    global log_users
    global log_data_dict
    global log_passwords

    if user not in log_users:
        return 0
    else:
        if log_data_dict[user] == pas:
            return 11
        else:
            return 1


def log_new():
    global log_users
    global log_data_dict
    global log_passwords

    log_init()
    while True:
        user = encrypt(input("Username >>> "))
        if (" " in decrypt(user) or user == 'log.csv' or user == '.log.csv'):
            print("Use Different Username")
        elif log_ststus(user):
            print("User already present")
        else:
            break

    while True:
        passw = encrypt(input("Password >>> "))
        if passw in user or user in passw or " " in decrypt(passw) or len(passw) > 15 or len(passw) < 5:
            print("Use different Password")
        else:
            passw =hash(decrypt(passw))
            break

    log_users.append(user)
    log_passwords.append(passw)
    temp_data = pd.DataFrame({'$G^&#': [], 'l.zMBC': []})
    temp_data.to_csv("." + user + ".csv", index=False)

    log_final()
    log_init()
    print("User Created Successfully")
    return 0


def log_user():
    log_init()
    global log_users
    global log_data_dict
    global log_passwords
    global present_username
    global present_password

    print("ENTER USERRNAME AND PASSWORD")
    print("For previous Menu press x ")

    while True:
        user = input("Username >> ")
        if user == 'x' or user == 'X':
            return 0
        user = encrypt(user)
        if not log_ststus(user):
            print("User Not Present")
        else:
            break
    while True:
        passw = input("Passsword >> ")
        if passw == 'x' or passw == 'X':
            return 0
        passw = hash(passw)
        if log_ststus(user, passw) == 1:
            print("Incorrect Password")
        else:
            break
    if log_data_dict[user] == passw:
        present_username = user
        present_password = passw
        main_user(decrypt(user))
        return 0


def del_log():
    log_init()
    global log_users
    global log_data_dict
    global log_passwords

    print("ENTER USERRNAME AND PASSWORD")
    print("For previous Menu press x ")

    while True:
        user = input("Username >> ")
        if user == 'x' or user == 'X':
            return 0
        user = encrypt(user)
        if not log_ststus(user):
            print("User Not Present")
        else:
            break
    while True:
        passw = input("Passsword >> ")
        if passw == 'x' or passw == 'X':
            return 0
        passw = hash(passw)
        if log_ststus(user, passw) == 1:
            print("Incorrect Password")
        else:
            break
    if log_data_dict[user] == passw:
        hold = '#'
        for i in range(len(log_users)):
            if user == log_users[i]:
                hold = i
                break
        s = input("Sure ? [y/n]")
        if s == 'y' or s == 'Y':
            if (hold != '#'):
                del log_users[hold]
                del log_passwords[hold]
                log_final()
                log_init()
                os.remove(f".{user}.csv")
                print("User Deleted ")
        elif s == 'n' or s == 'N':
            return 0
        else:
            print("Invaid selection Cannot Delete")
            return 0


def list_log():
    log_init()
    temp = pd.read_csv(".log.csv")
    temp = list(temp["@$D!_*"])
    temp = list(map(decrypt, temp))
    print("Users List")
    j = 1
    for i in temp:
        print(f"{j} : {i}")
        j += 1


def init():
    global accounts
    global passwords
    global data_dict

    temp = pd.read_csv('.' + present_username + '.csv')
    accounts = list(temp["$G^&#"])
    passwords = list(temp["l.zMBC"])
    data_dict = dict(zip(map(decrypt, accounts), map(decrypt, passwords)))
    return 0


def final():
    global accounts
    global passwords
    temp = pd.DataFrame({"$G^&#": accounts, "l.zMBC": passwords})
    temp.to_csv('.' + present_username + ".csv", index=False)


def display():
    init()
    ul = []
    pl = []
    for x, y in data_dict.items():
        ul.append(x)
        pl.append(y)
    temp = pd.DataFrame({'UserNames': ul, 'Passwords': pl})
    print(temp)


def new():
    init()
    global accounts
    global passwords
    print("ENTER USERRNAME AND PASSWORD")
    print("For previous Menu press x ")
    while True:
        u = input("Account >> ")
        if u == 'x' or u == 'X':
            return 0
        u = encrypt(u)
        if u in accounts:
            print("User Already Exists")
        else:
            break
    p = input("Password >> ")
    if p == 'x' or p == 'X':
        return 0
    p = encrypt(p)
    accounts.append(u)
    passwords.append(p)
    final()
    init()


def edit():
    global accounts
    global passwords
    print("Enter Account Name to Edit")
    print("For previous Menu press x ")
    while True:
        u = input("Account >> ")
        if u == 'x' or u == 'X':
            return 0
        u = encrypt(u)
        if u not in accounts:
            print("User Not Found")
        else:
            break
    hold = '#'
    for i in range(len(accounts)):
        if accounts[i] == u:
            hold = i
            break
    if hold != '#':
        p = encrypt(input("Password >>"))
        passwords[hold] = p
    final()
    init()


def delete():
    global accounts
    global passwords
    print("Enter Account Name to Delete")
    print("For previous Menu press x ")
    while True:
        u = input("Account >> ")
        if u == 'x' or u == 'X':
            return 0
        u = encrypt(u)
        if u not in accounts:
            print("User Not Found")
        else:
            break
    hold = '#'
    for i in range(len(accounts)):
        if accounts[i] == u:
            hold = i
            break
    if hold != '#':
        del accounts[hold]
        del passwords[hold]
        final()
        init()

def one():
    print("=====================================================================")
    print("------------------------Password Manager v1.0------------------------")
    print("----------------------------Vignesh Hegde----------------------------")
    print("=====================================================================")
    time.sleep(2)
    os.system("cls")

def main_user(user):
    init()

    while True:
        os.system("cls")
        print(f"User:{user}")
        print("----------------------------------------------------------")
        print("Select an Option")
        print("1: Display")
        print("2: New")
        print("3: Edit")
        print("4: Delete")
        print("x: Exit")
        print("----------------------------------------------------------")
        ch = input(">>> ")
        if ch == '1':
            os.system("cls")
            display()
            input()
            os.system("cls")

        elif ch == '2':
            os.system("cls")
            new()
            os.system("cls")
        elif ch == '3':
            os.system("cls")
            edit()
            os.system("cls")

        elif ch == '4':
            os.system("cls")
            delete()
            os.system("cls")

        elif ch == 'x' or ch == 'X':
            break
        else:
            os.system("cls")
            print("Invaid Selection")
            input()
            os.system("cls")

os.system("cls")
one()
while True:
    print("==========================================================")
    print("--------------------------Welcome-------------------------")
    print("==========================================================")
    print("----------------------------------------------------------")
    print("Select an Option")
    print("1: New User")
    print("2: Existing Users")
    print("3: Delete User")
    print("4: List users")
    print("x: Exit")
    print("----------------------------------------------------------")
    ch = input(">>> ")
    if ch == '1':
        os.system("cls")
        log_new()
        input()
        os.system("cls")

    elif ch == '2':
        os.system("cls")
        log_user()
        os.system("cls")

    elif ch == '3':
        os.system("cls")
        del_log()
        input()
        os.system("cls")

    elif ch == '4':
        os.system("cls")
        list_log()
        input()
        os.system("cls")

    elif ch == 'x' or ch == 'X':
        os.system("cls")
        print("------------------------------------------------------")
        print("----------------------Thank You-----------------------")
        print("------------------------------------------------------")
        time.sleep(2)
        break
    else:
        os.system("cls")
        print("Invalid Choice")
        input()
        os.system("cls")









