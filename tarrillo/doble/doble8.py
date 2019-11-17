import os
# BOLETA DE VENTA
# Declarar variables
cliente,kg,p.u ="",0,0.0

# Input
cliente=os.sys.argv[1]
kg=int(os.sys.argv[2])
p.u=float(os.sys.argv[3])

#Procesing
total= (p.u * kg)

#Verificador
comprador_compulsivo=(total>30)

#Output
print("#########################")
print("######Boleta de venta########")
print("#########################")
print("#")
print("# cliente:", cliente)
print("#item:    ",kg,"kg")
print("#P.U:      S/.", p.u)
print("#total:    S/.",total)
print("##########################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total es mayor a 30 obtendran un bono especial
if (comprador_compulsivo == True):
    print ("OBTUVISTE UN BONO ESPECIAL")
else:
    print ("GANASTE UN PREMIO ")

#FIN_IF
