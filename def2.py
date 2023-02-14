def postTaxPrice(price):
    ans = price * 1.08
    return ans

print(postTaxPrice(100),"元")
print(postTaxPrice(128),"元")
print(postTaxPrice(980),"元")