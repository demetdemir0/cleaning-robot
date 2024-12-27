import random

# Oda durumlarını ve eylemleri saklayacak yapılar
rooms = {'A': 0, 'B': 0}
actions = []
history = [rooms.copy()]

# Odaların başlangıç durumunu göster
print("ROOMS: ", str(rooms))

def clean():
    # Oda A'nın durumunu kontrol et ve eylemi kaydet
    if rooms['A'] == 1:
        print("A was dirty/A is cleaning/ A is clean.")
        actions.append("Suck A, Right")
        print("A---->B")
    elif rooms['A'] == 0:
        print("A is clean")
        actions.append("No Op, Right")
        print("A---->B")

    # Oda B'nin durumunu kontrol et ve eylemi kaydet
    if rooms['B'] == 1:
        print("B was dirty/B is cleaning/ B is clean.")
        actions.append("Suck B, Left")
        print("A<----B")
    elif rooms['B'] == 0:
        print("B is clean.")
        actions.append("No Op, Left")
        print("A<----B")

def report():
    # Temizlik süresini hesaplar ve raporu yazdırır
    cleaningTime = len(actions) * 5  # Her bir eylem 5 saniye sürer
    print("Cleaning report:")
    print("Cleaning time: " + str(cleaningTime) + " seconds")

# Ana döngü
while True:
    # İç döngü: Kullanıcı durdurana kadar devam eder
    while True:
        # Geçmişi ve yapılan eylemleri yazdır
        print("HISTORY" + str(history))
        print("ALL ACTIONS" + str(actions))
        print("**************************************************************")
        print("NEXT")

        # Her oda için rastgele kirli/temiz durumu belirle
        for room in rooms:
            rooms[room] = random.randint(0, 1)
            print("Room " + room + ": " + str(rooms[room]))
        history.append(rooms.copy())

        print("**************************************************************")

        # Kullanıcıdan devam etmek isteyip istemediğini sor
        devam_et = input("Do you want to continue? (Yes: 'y', No: 'n'): ")
        if devam_et != 'y':
            break

        # Temizlik işlemini gerçekleştir
        clean()

    # Temizlik raporunu yazdır
    report()

    # Programı sonlandırmak için kullanıcıdan girdi al
    n = input("Press 'n' to end the program: ")
    if n.lower() == 'n':
        break
