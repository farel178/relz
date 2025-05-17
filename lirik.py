import sys
import time


def jalanin_lirik():
    #
    lirik = [
        ("Tante.....", 0.1),
        ("sudah terbiasa terjadi tante", 0.04),
        ("teman datang ketika lagi butuh  saja", 0.04),
        ("coba kalo lagi susah", 0.04),
        ("mereka semua menghilangggggggggggggggggggggggg", 0.04),
        ("tante.....", 0.04),
        
    ]

    # 
    delay = [0.3, 2.6, 2.1, 1.2, 3.9, 0.6]
    # 
    print("\n== Sudah terbiasa ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    #
    print("// Code by farellz")


jalanin_lirik()