import os

# BOLETA DE VENTA
# declarar variables
cliente,RUC,mesas,sillas,carpetas,precio_de_una_mesa,precio_de_una_silla,precio_de_una_carpeta="",0,0,0,0,0.0,0.0,0.0

# INPUT
cliente=os.sys.argv[1]
RUC=int(os.sys.argv[2])
mesas=int(os.sys.argv[3])
sillas=int(os.sys.argv[4])
carpetas=int(os.sys.argv[5])
precio_de_una_mesa=float(os.sys.argv[6])
precio_de_una_silla=float(os.sys.argv[7])
precio_de_una_carpeta=float(os.sys.argv[8])

# PROCESSING
total=((mesas*precio_de_una_mesa)+(sillas*precio_de_una_silla)+(carpetas*precio_de_una_carpeta))

# VERIFICADOR
precio_de_venta=(total>total or 50<total)

#OUTPUT
print("#########################")
print("# Maderas:    EL CAJAMARQUINO")
print("#########################")
print("# cliente:", cliente)
print("# RUC:", RUC)
print("# mesas:", mesas,"                            precio:  S/.", precio_de_una_mesa)
print("# sillas:", sillas,"                          precio:  S/.", precio_de_una_silla)
print("# carpetas:", carpetas,"                      precio:  S/.", precio_de_una_carpeta)
print("# total:    S/.", total)
print("#########################")
print("# precio de  venta:", precio_de_venta)
print("#########################")

# CONDICIONAL SIMPLE
# si el total es mayor a S/. 850.00, entonces obtuve buena ganancia
if( total>850):
    print("Ud ha obtenido una buena ganancia")
# fin_if
