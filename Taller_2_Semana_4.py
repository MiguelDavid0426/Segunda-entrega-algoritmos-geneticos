# ----------------------------------------------------------------------------------------
# PROGRAMA: <<Imagenes de placas>>
# ----------------------------------------------------------------------------------------
# Descripción: <<Este es un programa que genera varios procesos a partir de la placa de un carro en una imagen>>
# ----------------------------------------------------------------------------------------
# Autores:
''' 
# Miguel David Benavides Galindo            md_benavidesg@javeriana.edu.co
# Christian Fernando Rodriguez Rodriguez    rodriguezchristianf@javeriana.edu.co
'''
# Version: 1.0
# [16.08.2021]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULES
import cv2
# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<Mascara_im>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Función que retorna una imagen en blanco y negro (mascara), mostrando en blanco los pixeles pertenecientes
# a la placa y en negro cualquier otro píxel.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# 1. La función genera una mascara de la placa a partir de la ruta donde se encuentra la imagen.
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna un dataframe con la mascara de la imagen. 
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<Rectangulo_im>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Función que retorna una imagen a color (original), mostrando un rectangulo en los pixeles pertenecientes
# a la placa del automovil.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# 1. La función genera un rectangulo de la placa a partir de la ruta donde se encuentra la imagen.
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna un dataframe con la información del rectangulo y la imagen original. 
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<Guardar_ima>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Función que guarda una placa a color, en formato png.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# 1. La función genera un rectangulo de la placa a partir de la ruta donde se encuentra la imagen, luego guarda la placa en la segunda ruta que se ingresa.
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna un ong con la información de la placa en la imagen original. 
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<Rotacion_ima>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<Función que rota la imagen y placa, segun el angulo que se le de.>>
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# 1. La función genera una rotación de la placa y de la imagen.
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# 1. Retorna las imagenes rotadas de acuerdo a los parametros ingresados. 
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Ejecución
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
