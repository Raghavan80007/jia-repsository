'''
class dic(dict):

    def __init__(self):
        self = dict()

    def add(self,key,value):
        self[key] = value


d = dic()
d.key = int(input('enter the number'))
d.value = int(input('enter the number'))

d.add(d.key,d.value)
print(d)


d = dict()

d = dict(firstname='rohit',lastname = 'challa')
d1 = dict((('firstname','rohit'),('second','rohit')))
print(d1)



dic = dict().fromkeys(('eng','math','social'),19)
print(dic)



keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : (value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
a=value.append(2)
print(a)
print(vowels)
li=[]
states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat"]
dic = {'state':li.append(state) for state in states}
print(li)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dic = dict(zip(keys,values))
print(dic)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)


sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict['class']['student']['marks']['history'])

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
li = []
sd = sampleDict.keys()
for i in sd:
    if(i =='name'):
        li.append(i)
    elif(i=='salary'):
        li.append('salary')
print(li)
for i in li:
    dict1 = {i:sampleDict[i]}
    print(dict1,end='')

sampleDict = {'a': 100, 'b': 200, 'c': 300}
if(200 in sampleDict.values()):
    print(True)
 '''

a_b_c = 1,655,00
print(a_b_c)


