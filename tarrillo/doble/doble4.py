import os
# BOLETA DE VENTA
# Declarar variables
cliente,nro_juguetes,p_u= "",0,0.0

# Input
cliente=os.sys.argv[1]
nro_juguetes=int(os.sys.argv[2])
p_u=float(os.sys.argv[3])

#Procesing
total= (p_u * nro_juguetes)

#Verificador
comprador_compulsivo=( total > 80 )

#Output
print("#######################")
print("####Boleta de venta####")
print("#")
print("# cliente:", cliente)
print("#item:    ",nro_juguetes,"nro_juguetes")
print("#p.u:       S/.", p_u)
print("#total:     S/.",total)
print("#######################")
print("comprador compulsivo", comprador_compulsivo)

# Si el total supera 80 gana un pase para el cine
if (comprador_compulsivo == True):
    print ("GANASTE UN PASE AL CINE")
else:
    print ("GANASTE UN DESCUENTO")
#FIN_IF
