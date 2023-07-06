import joblib
from category_encoders import BinaryEncoder
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the saved model
loaded_model_classfication = joblib.load('test.joblib')
loaded_model_regression = joblib.load('svm_trained_model.joblib')
loaded_encoder = joblib.load('encoder.joblib')
loaded_scaler = joblib.load('scaler.joblib')


# expectations are 5,3,6,5,1,4,8,2,7,3,6,2

def classification_prediction(data):
    y = loaded_encoder.transform(data)
    predictions = loaded_model_classfication.predict(y)
    for data, prediction in zip(data, predictions):
        print(f"Predicted class: {prediction}")

    return prediction


def regression_prediction(data):
    y = loaded_encoder.transform(data)
    y = loaded_scaler.transform(y)
    predictions = loaded_model_regression.predict(y)
    for data, prediction in zip(data, predictions):
        print(f"Predicted class: {prediction}")

    return prediction


test = [
    ["Aatrox", "null", "null", "null", 3,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null", ]
]

test1 = [
    ["Lux", "null", "null", "null", 1,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null", ]
]


data1 = [
    ["Samira", "null", "null", "null", 3,
     "Warwick", "null", "null", "null", 1,
     "Kled", "null", "null", "null", 2,
     "Swain", "RedBuff", "TitanicHydra", "NegatronCloak", 2,
     "Darius", "null", "null", "null", 2,
     "Ekko", "null", "null", "null", 1,
     "Katarina", "IonicSpark", "UnstableConcoction", "JeweledGauntlet", 3,
     "Sion", "Bloodthirster", "GiantSlayer", "TitansResolve", 2,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data2 = [
    ["Soraka", "null", "null", "null", 2,
     "Ashe", "null", "null", "null", 2,
     "Taric", "FreljordEmblem", "null", "null", 2,
     "Sejuani", "WarmogsArmor", "null", "null", 2,
     "JarvanIV", "FrozenHeart", "SpearOfShojin", "UnstableConcoction", 2,
     "Shen", "GargoyleStoneplate", "WarmogsArmor", "DragonsClaw", 2,
     "Aphelios", "HorizonFocus", "Deathblade", "GuinsoosRageblade", 2,
     "Sion", "FreljordEmblem", "null", "null", 1,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data3 = [
    ["Irelia", "null", "null", "null", 2,
     "Warwick", "null", "null", "null", 2,
     "Kalista", "IoniaEmblem", "UnstableConcoction", "ArchangelsStaff", 2,
     "KaiSa", "IoniaEmblem", "null", "null", 1,
     "Shen", "WarmogsArmor", "RedBuff", "null", 1,
     "Yasuo", "TitansResolve", "PowerGauntlet", "GuardianAngel", 2,
     "Ahri", "SpearOfShojin", "null", "null", 1,
     "Heimerdinger", "null", "null", "null", 1,
     "HeimerdingerTurret", "null", "null", "null", 1,
     "null", "null", "null", "null", "null"]
]

data4 = [
    ["Orianna", "null", "null", "null", 2,
     "Swain", "InfinityEdge", "TitansResolve", "null", 3,
     "Taric", "null", "null", "null", 2,
     "VelKoz", "null", "null", "null", 2,
     "JarvanIV", "Redemption", "WarmogsArmor", "null", 2,
     "Lux", "SeraphsEmbrace", "GiantSlayer", "JeweledGauntlet", 2,
     "Heimerdinger", "SorcererEmblem", "null", "null", 1,
     "HeimerdingerTurret", "TFT9HeimerUpgradeShrinkRay", "TFT9HeimerUpgradeGoldification",
     "TFT9HeimerUpgradeMicroRockets", 1,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data5 = [
    ["Vi", "null", "null", "null", 2,
     "Ashe", "null", "null", "null", 2,
     "Lissandra", "null", "null", "null", 2,
     "Jayce", "ZekesHerald", "null", "null", 3,
     "Ekko", "null", "null", "null", 3,
     "Sejuani", "RedBuff", "GargoyleStoneplate", "WarmogsArmor", 2,
     "Urgot", "ThiefsGloves", "RedBuff", "UnstableConcoction", 2,
     "Zeri", "RunaansHurricane", "GuinsoosRageblade", "HextechGunblade", 2,
     "Senna", "GuinsoosRageblade", "null", "null", 1,
     "null", "null", "null", "null", "null"]
]

data6 = [
    ["Irelia", "null", "null", "null", 1,
     "Warwick", "null", "null", "null", 2,
     "Sejuani", "GargoyleStoneplate", "GargoyleStoneplate", "null", 2,
     "KaiSa", "HextechGunblade", "HorizonFocus", "GuinsoosRageblade", 2,
     "Shen", "null", "null", "null", 1,
     "Yasuo", "UnstableConcoction", "TitansResolve", "GuardianAngel", 2,
     "Sion", "NegatronCloak", "InfinityEdge", "null", 1,
     "Heimerdinger", "null", "null", "null", 1,
     "HeimerdingerTurret", "TFT9HeimerUpgradeShrinkRay", "TFT9HeimerUpgradeGoldification", "null", 1,
     "null", "null", "null", "null", "null"]
]

data7 = [
    ["Teemo", "null", "null", "null", 3,
     "Taliyah", "SeraphsEmbrace", "JeweledGauntlet", "InfinityEdge", 2,
     "Sett", "GargoyleStoneplate", "WarmogsArmor", "IonicSpark", 2,
     "Swain", "TitansResolve", "null", "null", 2,
     "Sona", "Chalice", "NeedlesslyLargeRod", "null", 3,
     "VelKoz", "null", "null", "null", 2,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data8 = [
    ["Jinx", "null", "null", "null", 2,
     "Jayce", "Zephyr", "null", "null", 2,
     "Ekko", "Redemption", "null", "null", 2,
     "Urgot", "TrickshotEmblem", "Bloodthirster", "GuardianAngel", 2,
     "JarvanIV", "null", "null", "null", 1,
     "JarvanIV", "RedBuff", "ZaunEmblem", "WarmogsArmor", 2,
     "Zeri", "PowerGauntlet", "LastWhisper", "RunaansHurricane", 2,
     "Sion", "ZaunEmblem", "Redemption", "null", 2,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data9 = [
    ["Jinx", "null", "null", "null", 2,
     "Vi", "null", "null", "null", 2,
     "Jayce", "ZekesHerald", "null", "null", 2,
     "Ekko", "ForceOfNature", "null", "null", 2,
     "Urgot", "TitansResolve", "null", "null", 1,
     "Zeri", "GuinsoosRageblade", "LastWhisper", "null", 1,
     "Shen", "FrozenHeart", "RedBuff", "null", 2,
     "KSante", "null", "null", "null", 1,
     "THex", "PiltoverProgress", "PiltoverCharges", "null", 1,
     "null", "null", "null", "null", "null"]
]

data10 = [
    ["Irelia", "null", "null", "null", 2,
     "Warwick", "null", "null", "null", 2,
     "Sett", "TitanicHydra", "null", "null", 2,
     "Karma", "null", "null", "null", 2,
     "KaiSa", "ArchangelsStaff", "IoniaEmblem", "PowerGauntlet", 2,
     "KaiSa", "HextechGunblade", "RabadonsDeathcap", "RapidFireCannon", 2,
     "Shen", "IonicSpark", "DragonsClaw", "RedBuff", 2,
     "Yasuo", "null", "null", "null", 2,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data11 = [
    ["Irelia", "Zephyr", "BrambleVest", "null", 2,
     "Warwick", "null", "null", "null", 2,
     "Sett", "ChallengerEmblem", "null", "null", 2,
     "Kalista", "RapidFireCannon", "UnstableConcoction", "null", 2,
     "Zephyr", "null", "null", "null", 3,
     "Gwen", "null", "null", "null", 1,
     "KaiSa", "GuinsoosRageblade", "SpearOfShojin", "StatikkShiv", 2,
     "Yasuo", "RapidFireCannon", "InfinityEdge", "null", 1,
     "null", "null", "null", "null", "null",
     "null", "null", "null", "null", "null"]
]

data12 = [
    ["Swain", "null", "null", "null", 2,
     "Darius", "GuardianAngel", "Bloodthirster", "InfinityEdge", 3,
     "Ekko", "UnstableConcoction", "ArchangelsStaff", "GiantSlayer", 3,
     "Garen", "null", "null", "null", 2,
     "Katarina", "IonicSpark", "null", "null", 3,
     "JarvanIV", "LocketOfTheIronSolari", "Shroud", "null", 2,
     "Lux", "null", "null", "null", 2,
     "Ahri", "RunaansHurricane", "null", "null", 2,
     "Heimerdinger", "null", "null", "null", 2,
     "HeimerdingerTurret", "TFT9HeimerUpgradeShrinkRay", "TFT9HeimerUpgradeMicroRockets", "TFT9HeimerUpgradeShrinkRay",
     2]
]
print(data1)
print("classification results:")
here = classification_prediction(test)
classification_prediction(test1)

regression_prediction(test)
regression_prediction(test1)
"""""
haha = classification_prediction(data2)
classification_prediction(data3)
classification_prediction(data4)
classification_prediction(data5)
classification_prediction(data6)
classification_prediction(data7)
classification_prediction(data8)
classification_prediction(data9)
classification_prediction(data10)
classification_prediction(data11)
classification_prediction(data12)


if here > haha:
    print("greater")
else:
    print("lesser")

print()
print("regression results:")

regression_prediction(data2)
regression_prediction(data3)
regression_prediction(data4)
regression_prediction(data5)
regression_prediction(data6)
regression_prediction(data7)
regression_prediction(data8)
regression_prediction(data9)
regression_prediction(data10)
regression_prediction(data11)
regression_prediction(data12)
"""
