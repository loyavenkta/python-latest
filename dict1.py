"""student = ["sai","Koushik","loya","Venkata"]
House = ["1801","1802","1803","1804"]"""
""""data = {
    "sai":"1801",
    "Koushik":"1802", 
    "Loya":"1803", 
    "LVS":"1804"
        }
print(data["sai"])
print(data["LVS"])
for i in data:
     print(i, ":", data[i])"""

data = [
    {"name" : "SAI", "house" : "1801", "type" :"2bhk"},
    {"name" : "Venkata", "house" : "1802", "type" :"3bhk"},
    {"name" : "Koushik", "house" : "1803", "type" :"4bhk" },
    {"name" : "Loya", "house" : "1804", "type" :"1bhk"}]
for i in data:
    print(i["name"],i["house"],i["type"], sep = " _")

