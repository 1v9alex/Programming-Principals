carComapny = ['Audi','BMW','Ferrari']

print(*carComapny)

techStackOne = {"React":"Facebook","Angular":"google","dotNet":"Microsoft"}
techStackTwo = {"dotNet": "Microsoft","Java":"Minecraft"}

mergedStack = {**techStackOne, **techStackTwo}

print(mergedStack)

print(*techStackOne)


carComapny2 = [["Audi","R8"],["BMW","Car"]]

carCompany3 = ["Lamborgini","porsche"]
print(*carComapny2)


techStackOne.update(techStackTwo)

print(techStackOne)

v = techStackOne["Angular"]

techStackOne["Angular"] = "Not google"

print(techStackOne)

def makeSentence(**words):
    sentence = ''
    for word in words.values():
        sentence += word
    return sentence

print('Sentence:',makeSentence(a='kwargs ',b="are ",c="awesome"))

def whatTechTheyUse(**kwargs):
    result = []
    for key,value in kwargs.items():
        result.append(f"{key} uses {value}")
    return result

print(whatTechTheyUse(Google="Angular",Facebook='react',Microsoft=".NET"))


def my_func(*args, **kwargs):
    return args, kwargs

print(my_func(1, 2, a=3, b=4))