print("==============================")
print("Introdu parola pe care vrei sa o verifici:")
parola = input()
print("==============================")
print("Parola introdusa este: " + parola)
print("Lungime: " + str(len(parola))+" caractere")
print("Cel putin 8 caractere: " + str(len(parola) >= 8))
litere_mari=False
for i in range(len(parola)):
    if(not parola[i].isalpha()):
        continue
    if(parola[i]==parola[i].upper()):
        litere_mari=True
print("Are litere mari: "+str(litere_mari))    
litere_mici=False
for i in range(len(parola)):
    if(not parola[i].isalpha()):
        continue
    if(parola[i]==parola[i].lower()):
        litere_mici=True
print("Are litere mici: "+str(litere_mici)) 
doar_litere=True
for i in range(len(parola)):
    if(parola[i].isalpha()==False or parola[i]==" "):
        doar_litere=False
        break
print("Are doar litere(vrem False): "+ str(doar_litere))   
doar_spatii=False
for i in range(len(parola)):
    if(parola[i]==" "):
        doar_spatii=True
        break
print("Are spatii(vrem False): "+str(doar_spatii))
print("==============================")