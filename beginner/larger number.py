def main():
 a=int(input())
 b=int(input())
 c=int(input())
 if((a>b)and(a>c)):
    print("a is larger")
 if((b>a)and(b>c)):
    print("b is larger")
 if((c>b)and(c>a)):
    print("c is larger")

if __name__ == '__main__':
    main()
