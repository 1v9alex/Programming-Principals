carCompany = ['Audi','BMW','Lamborghini']

print(*carCompany)
print(carCompany)

myDict = {'Audi': 'A4', 'BMW': 'M3', 'Lamborghini': 'Aventador'}

myDict2 = {'toyota': 'camry', 'honda': 'civic', 'ford': 'focus'}

mergedDict = {**myDict, **myDict2}

print(mergedDict)

#1 star to unpack list 2 for dictionary


def whatTechTheyUse(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} uses {value}")


whatTechTheyUse(Audi='Python', BMW='Java', Lamborghini='C++')