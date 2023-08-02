def abc():
    try:
        i=int(input("Enter the number ="))
        if i%2==0:
            print("Even")
    except:
         i=int(input("Enter the number ="))
         if i%2==0:
            print("Even")
    finally:
        print("code ran")

abc()