import json
import pickle

#-------Inserting-------
server = []
name = []
email = []
psswd = []

#-------Showing-------
s = open('server_name.json')
server = json.load(s)

n = open('name.json')
name = json.load(n)

e = open('e-mail.json')
email = json.load(e)

p = open('psswd.json')
psswd = json.load(p)



circle = "t"

while circle == "t":

    print("Add box: 1")
    print("Show all boxes: 2")
    print("Delete all (extra situations) : 9")
    print("Exit: 0")

    inpt = int(input())
    if inpt == 1:
        print("Type server name: ")
        server_inpt = input()
        server.append(server_inpt)
        with open('server_name.json', 'w') as i:
            json.dump(server, i)
        with open('file_server_name', 'wb') as fi:
            pickle.dump(server, fi)
        
        print("Type name (if there is not type -) : ")
        name_inpt = input()
        name.append(name_inpt)
        with open('name.json', 'w') as i:
            json.dump(name, i)
        with open('file_name', 'wb') as fi:
            pickle.dump(name, fi)

        print("Type e-mail: ")
        email_inpt = input()
        email.append(email_inpt)
        with open('e-mail.json', 'w') as i:
            json.dump(email, i)
        with open('file_e-mail', 'wb') as fi:
            pickle.dump(email, fi)

        print("Type password: ")
        psswd_inpt = input()
        psswd.append(psswd_inpt)
        with open('psswd.json', 'w') as i:
            json.dump(psswd, i)
        with open('file_psswd', 'wb') as fi:
            pickle.dump(psswd, fi)

    if inpt == 2:
        print(server)
        print(name)
        print(email)
        print(psswd)

    if inpt == 9:
#Server------------
        server_list = [server]
        with open('server_name.json', 'w') as h:
            json.dump(server_list, h)

        with open('server_name.json') as server_data:
            ServerData = json.load(server_data)
            ServerData.remove(server)

        with open('server_name.json', 'w') as q:
            json.dump(ServerData, q)
            m = open('server_name.json')

#Name--------------
        name_list = [name]
        with open('name.json', 'w') as h:
            json.dump(name_list, h)

        with open('name.json') as name_data:
            NameData = json.load(name_data)
            NameData.remove(name)

        with open('name.json', 'w') as q:
            json.dump(NameData, q)
            m = open('name.json')

#E-mail------------
        email_list = [email]
        with open('e-mail.json', 'w') as h:
            json.dump(email_list, h)

        with open('e-mail.json') as email_data:
            EmailData = json.load(email_data)
            EmailData.remove(email)

        with open('e-mail.json', 'w') as q:
            json.dump(EmailData, q)
            m = open('e-mail.json')

#Password----------
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

    