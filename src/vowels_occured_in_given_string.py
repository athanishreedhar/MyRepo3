#program to find number of occurrences of each vowel present in the given string

vowels={'a','e','i','o','u'}
s=input("Enter the String :")
d={}
for i in s:
    if i in vowels:
        d[i]=d.get(i,0)+1
for k,v in sorted(d.items()):
    print(k,"----",v)
     