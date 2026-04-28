# The provided code stub reads an integer,n , from STDIN. For all non-negative integers i < n, print i².
# Constrains 1 <= n <= 20

if __name__ == '__main__':
 n = int(input())
if 1 <= n <= 20:
    for i in range(n):
        print(i * i)
