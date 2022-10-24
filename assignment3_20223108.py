import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split()

        if parse[0] == 'add' and len(parse) == 4:
            try:
                age = int(parse[2])
                score = int(parse[3])
            except ValueError:
                print("put number!")
            else:
                record = {'Name':parse[1], 'Age':age, 'Score':score}
                scdb += [record]

        elif parse[0] == 'del' and len(parse) == 2:
            findls = findScoreDB(scdb, parse[1])
            for p in findls:
                scdb.remove(p)

        elif parse[0] == 'show' and len(parse) == 1:
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        elif parse[0] == "find" and len(parse) == 2:
            findls = findScoreDB(scdb, parse[1])
            for p in findls:
                for attr in sorted(p):
                    print(attr + "=" + str(p[attr]), end=' ')
                print()

        elif parse[0] == "inc" and len(parse) == 3:
            try:
                num = int(parse[2])
            except ValueError:
                print("put number!")
            else:
                findls = findScoreDB(scdb, parse[1])
                for p in findls:
                    p['Score'] += num

        elif parse[0] == "add" or parse[0] == "del" or parse[0] == "show" or parse[0] == "find" or parse[0] == "inc":
            print("Input correct attribute")

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()

def findScoreDB(scdb, name):
    ls = []
    for p in sorted(scdb, key=lambda person: person['Name']):
        if p['Name'] == name:
            ls.append(p)
    return ls

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
