print("==============================")
print("Introdu parola pe care vrei sa o verifici:")
parola = input()
print("==============================")
print("Parola introdusa este: " + parola)
print("Lungime: " + str(len(parola))+" caractere")
print("Cel putin 8 caractere: " + str(len(parola) >= 8))
litere_mari=False
for conditie1 in range(len(parola)):
    if(not parola[conditie1].isalpha()):
        continue
    if(parola[conditie1]==parola[conditie1].upper()):
        litere_mari=True
print("Are litere mari: "+str(litere_mari))    
litere_mici=False
for conditie1 in range(len(parola)):
    if(not parola[conditie1].isalpha()):
        continue
    if(parola[conditie1]==parola[conditie1].lower()):
        litere_mici=True
print("Are litere mici: "+str(litere_mici)) 
doar_litere=True
for conditie1 in range(len(parola)):
    if(parola[conditie1].isalpha()==False or parola[conditie1]==" "):
        doar_litere=False
        break
print("Are doar litere(vrem False): "+ str(doar_litere))   
doar_spatii=False
for conditie1 in range(len(parola)):
    if(parola[conditie1]==" "):
        doar_spatii=True
        break
print("Are spatii(vrem False): "+str(doar_spatii))
print("==============================")