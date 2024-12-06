from math import prod

strPow = lambda r: prod(len(r) for x in r)
print(strPow('25' * 2),'' ,sep=';')