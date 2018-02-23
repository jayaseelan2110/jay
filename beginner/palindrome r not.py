def main():
 a=str(input())
 if((str(a))==(str(a[::-1]) )):
   print("this number is palindrome")
 else:
  print("this number is not palindrome")

if __name__ == '__main__':
    main()
