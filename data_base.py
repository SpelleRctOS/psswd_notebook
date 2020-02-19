import json
import pickle

# -------Inserting-------
domain = []
nickname = []
email = []
psswd = []
num = 1

# -------Showing-------
s = open('domain_name.json')
domain = json.load(s)

n = open('nickname.json')
nickname = json.load(n)

e = open('e-mail.json')
email = json.load(e)

p = open('psswd.json')
psswd = json.load(p)

num_show = len(psswd)

circle = "t"

while circle == "t":

    print("Add box: 1")
    print("Show all boxes: 2")
    print("Delete all (extra situations) : 9")
    print("Exit: 0")

    inpt = int(input())
    if inpt == 1:
        for i in range(num):
            domain_name = input("Domain: ")
            nickname_name = input("Nickname (if do not exist type '-') : ")
            email_name = input("E-mail: ")
            psswd_name = input("Password: ")

            domain.append(domain_name)
            with open('domain.json', 'w') as i:
                json.dump(domain, i)
            with open('file_domain', 'wb') as fi:
                pickle.dump(domain, fi)

            nickname.append(nickname_name)
            with open('nickname.json', 'w') as i:
                json.dump(nickname, i)
            with open('file_nickname', 'wb') as fi:
                pickle.dump(nickname, fi)

            email.append(email_name)
            with open('e-mail.json', 'w') as i:
                json.dump(email, i)
            with open('file_e-mail', 'wb') as fi:
                pickle.dump(email, fi)

            psswd.append(psswd_name)
            with open('psswd.json', 'w') as i:
                json.dump(psswd, i)
            with open('file_psswd', 'wb') as fi:
                pickle.dump(psswd, fi)

    if inpt == 2:
        print("\n---Domain---\t\t\t---Nickname---\n")

        for i in range(num_show):
            print("{}\t\t\t{}".format(domain[i], nickname[i]))

        print("\n---E-mail---\t\t\t---Password---\n")

        for i in range(num_show):
            print("{}\t\t\t{}".format(email[i], psswd[i]))

        print("\n")
    if inpt == 9:
        # Server------------
        domain_list = [domain]
        with open('domain.json', 'w') as h:
            json.dump(domain_list, h)

        with open('domain.json') as domain_data:
            DomainData = json.load(domain_data)
            DomainData.remove(domain)

        with open('domain.json', 'w') as q:
            json.dump(DomainData, q)
            m = open('domain.json')

# Name--------------
        nickname_list = [nickname]
        with open('nickname.json', 'w') as h:
            json.dump(nickname_list, h)

        with open('nickname.json') as nickname_data:
            NicknameData = json.load(nickname_data)
            NicknameData.remove(nickname)

        with open('nickname.json', 'w') as q:
            json.dump(NicknameData, q)
            m = open('nickname.json')

# E-mail------------
        email_list = [email]
        with open('e-mail.json', 'w') as h:
            json.dump(email_list, h)

        with open('e-mail.json') as email_data:
            EmailData = json.load(email_data)
            EmailData.remove(email)

        with open('e-mail.json', 'w') as q:
            json.dump(EmailData, q)
            m = open('e-mail.json')

# Password----------
        psswd_list = [psswd]
        with open('psswd.json', 'w') as h:
            json.dump(psswd_list, h)

        with open('psswd.json') as psswd_data:
            PsswdData = json.load(psswd_data)
            PsswdData.remove(psswd)

        with open('psswd.json', 'w') as q:
            json.dump(PsswdData, q)
            m = open('psswd.json')

    if inpt == 0:
        print("Exiting...")
        circle = "f"
