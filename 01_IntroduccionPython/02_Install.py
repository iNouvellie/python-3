'''

#Primero debemos corregir la version default de python

update-alternatives --install /usr/bin/python python /usr/bin/python3 1

#Revisamos que este por default version 3

python --version

#Instalamos pip

sudo apt install python3-pip -y

#Revisamos la version y correcta instalacion

pip --version

#Instalamos django en su ultima version, el numero lo podemos revisar en la pag oficial

pip install Django=2.0.7

#Revisamos django

django-admin --version

#En caso de no resultar, usar el siguiente codigo

sudo apt install python3-django

#Y revisamos nuevamente 

django-admin --version
'''