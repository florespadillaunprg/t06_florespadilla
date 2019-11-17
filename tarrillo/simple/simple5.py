import os
# BOLETA DE VENTA
# Declarar variables
empresa,nro_computadoras,p_u= "",0,0.0

# Input
empresa=os.sys.argv[1]
nro_computadoras=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

# processing
total=(nro_computadoras*p_u)

#Verificador
comprador_compulsivo=(total>267000)
#Output
print("#######################")
print("######Boleta de venta######")
print("#")
print("#item:    ",nro_computadoras,"nro_computadoras")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera a 267 000 obtiene una tarjeta black
if (comprador_compulsivo == True):
    print ("GANASTE LA TARJETA BLACK")

#FIN_IF
