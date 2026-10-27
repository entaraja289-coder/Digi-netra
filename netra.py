import os, sys
sys.path.append(os.path.dirname(__file__))
from main.phone import check_phone
from main.nik import check_nik
from main.email import check_email

def main():
  while True:
    print("\n=== Digi-netra FIXED ===")
    print("1. Phone (FIXED)")
    print("2. NIK (NEW)")
    print("3. Email (NEW)")
    print("4. Exit")
    c=input("Pilih: ").strip()
    if c=="1": check_phone()
    elif c=="2": check_nik()
    elif c=="3": check_email()
    elif c=="4": 
        print("Bye!")
        break
    else: print("Pilihan salah")

if __name__=="__main__": main()
