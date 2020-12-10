##REQUIREMENTS:
##1. pip install --upgrade firebase-admin
##2. pythonleader-firebase... .json is in the same folder (certificate)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('pythonleader-firebase-adminsdk-uvfgz-ff429c601d.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'leaderboard')

def update_leaderboard():
    docs = users_ref.stream()

    leaderboard = {}

    for doc in docs:
        #print(f'{doc.id} => {doc.to_dict()}')
        user_dic = doc.to_dict()
        leaderboard[doc.id] = user_dic["score"]

    return leaderboard

leaderboard = update_leaderboard()
    
running = True
while running:
    option = input('''Options: 
1. Print Leaderboard 
2. Add To/Update Leaderboard
3. Delete User From Leaderboard
4. Exit
>''')

    if option.isdigit() and 1 <= int(option) <= 4:

        leaderboard = update_leaderboard()
        
        option = int(option)
        print("")

        if option == 1:
            sorted_leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)}
            print("LEADERBOARD:\n")
            count = 0
            for i in sorted_leaderboard:
                count += 1
                print(i+": "+str(sorted_leaderboard[i]))

        elif option == 2:    
            name = input('Name: ').lower()
            try:
                score = int(input('Score: '))
            except:
                print("Invalid Input.")

            if not name in leaderboard or leaderboard[name] < score:
                doc_ref = db.collection(u'leaderboard').document(name)
                doc_ref.set({
                    u'score': score,
                })

        elif option == 3:    
            name = input('Name: ').lower()
            if name in leaderboard:
                db.collection(u'leaderboard').document(name).delete()

        elif option == 4:
            running = False
            
    print("")



