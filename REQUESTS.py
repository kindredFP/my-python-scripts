import requests

req = requests.get('http://example.com/')
# 200 OK
print(req.status_code)
print("Print value of text " + req.text)

# non existent file, it stops when error occurs, you can try/catch
badRequest = requests.get('https://google.ca/security.txt')
try:
    badRequest.raise_for_status()

except:
    print()
    print('Exception occured here is status code: ' + str(badRequest.status_code))
