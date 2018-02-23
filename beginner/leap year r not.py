def main():
 a=int(input())
 if((a%400==0)or(a%100==0)or(a%4==0)):
    print("it is leap year")
 else:
    print("it is not leap year")


if __name__ == '__main__':
    main()
