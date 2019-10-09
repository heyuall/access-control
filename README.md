### access-control
   Ce code est basé sur la bibliothèque face_recognition de python  qui nécessite l’installation de dlib.
Néanmoins, la configuration s’avère pénible et peut causer des problèmes au cours de l’installation de dlib(bibliothèque de deep learning).Pour cela je veux parler en détaille de cette partie. 
Pour tester le code il faut suivre les étapes :
#1-installer la version anaconda de python 
#2- Création de l’environnement virtuel (nécessaire pour interpréter le code python) :
Conda create – name opencv–env python3.7
#3- installer opencv:
    3.1-Activation de l’environnement virtuel :
    Activate opencv –env
    3.2. Install OpenCV and other important packages:
     conda install numpy scipy matplotlib scikit-learn jupyter
     conda install opencv-contrib-python
     conda install dlib
4-tester l’intallation:
import cv2
cv2.__version__
import dlib
dlib.__version__
5- installer face_recognition :
Pip install face_recognition
*) Si face_recognition n’est pas reconnu par l’interpréteur python essayez :
pip install --no-dependencies face_recognition
*)Rq: assurez-vous d’avoir changer l’interpréteur (exemple en utilisant pycharme).
Stages du programme :

face_train : permet de preparer les données et les trier
 face_rec : nécessaire pour la comparaison et l’identification
Autre Modules utilisés :

OS :	to use operating system functions to load, read, write in files
Pickle : implements binary protocols for serializing and de- serializing a
Python object structure.
Xlsxwriter : to create, write and read a excel file

Tkinter : to design the user interface
