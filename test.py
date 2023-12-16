import tkinter as tk
import cv2
import os
from tkinter import filedialog
from PIL import Image, ImageTk

# # Chemin du dossier d'entrée et de sortie
# chemin_entree = 'C:\\Users\\kvong\\OneDrive\\Documents\\Projects\\projetPython\\photo\\images_entree'
# chemin_sortie = 'C:\\Users\\kvong\\OneDrive\\Documents\\Projects\\projetPython\\photo\\images_sortie'  # À remplacer par ton chemin de sortie

def charger_image():
    chemin_image = filedialog.askopenfilename()
    if chemin_image:
        image_entree = cv2.imread(chemin_image)
        cv2.imshow("Image d'entrée", image_entree)
        
        # Trouver une correspondance dans le dossier de sortie
        correspondance_trouvee = False
        for fichier_sortie in fichiers_sortie:
            chemin_fichier_sortie = os.path.join(chemin_sortie, fichier_sortie)
            image_sortie = cv2.imread(chemin_fichier_sortie)
            
            # Afficher l'image du dossier de sortie correspondante à l'image sélectionnée
            if image_entree.shape == image_sortie.shape and \
               cv2.bitwise_xor(image_entree, image_sortie).sum() == 0:
                correspondance_trouvee = True
                cv2.imshow("Image de sortie correspondante", image_sortie)
                break
        
        if not correspondance_trouvee:
            print("Aucune correspondance trouvée pour cette image dans le dossier de sortie.")

root = tk.Tk()
root.withdraw()  # Pour masquer la fenêtre principale de tkinter

chemin_entree = 'C:\\Users\\kvong\\OneDrive\\Documents\\Projects\\projetPython\\photo\\images_entree'  # Remplace avec ton chemin
chemin_sortie = 'C:\\Users\\kvong\\OneDrive\\Documents\\Projects\\projetPython\\photo\\images_sortie'  # Remplace avec ton chemin

fichiers_sortie = os.listdir(chemin_sortie)

btn_charger = tk.Button(root, text="Choisir une image d'entrée", command=charger_image)
btn_charger.pack()

root.mainloop()