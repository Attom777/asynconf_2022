# ASTRO - EXERCICE 1

# ================== FUNCTIONS ==================

def getData():
    
    return input("Entrez le nom de l'étape : ")

# ================== MAIN ================== 

#Initialisazion of variables
stepsPlanet = []
planetSeen = []
missionsCode = ""

#Get user's data
while (1):
    
    userValue = getData()
    
    if userValue != "": 
        stepsPlanet.append(userValue)
    else: 
        break
    
#Transform missionsCode
for i in range(len(stepsPlanet)):
    
    #TODO: duplicate planet case
    
    letter = stepsPlanet[i][0]
    
    missionsCode += letter + str(len(stepsPlanet[i]) - 1)
    
    planetSeen.append(stepsPlanet[i]) #Add planet in marked list

#Display results
print("\nLe code mission : {}".format(missionsCode))











