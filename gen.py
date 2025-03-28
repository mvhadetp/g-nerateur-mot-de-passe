import string
import random

def generer_mot_de_passe(longueur=12):
   
    lowercase = string.ascii_lowercase  
    uppercase = string.ascii_uppercase  
    digits = string.digits  
    symbols = string.punctuation  

  
    all_characters = list(lowercase + uppercase + digits + symbols)
    random.shuffle(all_characters)

    
    mot_de_passe = ''.join(random.choices(all_characters, k=longueur))
    
    return mot_de_passe


print("Votre mot de passe :", generer_mot_de_passe())