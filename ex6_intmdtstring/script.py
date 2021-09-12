# Exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475 '

start = str.find(':')
result = str[start+1:]
stripped = float(result.strip())

print(result, type(stripped))