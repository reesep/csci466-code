
import requests



r = requests.get("http://v2.jokeapi.dev/joke/Any?safe-mode")

print(r.status_code)
print(r.headers)
print(r.content)

print(r.text)   

r = requests.get("http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html")


print(r.text)
output = open("output.html","w")
output.write(r.text)
output.close()
