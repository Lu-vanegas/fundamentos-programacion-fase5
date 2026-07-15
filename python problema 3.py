# Programa para calcular reabastesimiento de stock.

# Nombre del estudiante: Laura Marcela Vanegas Moreno
# Grupo: 213022_113
# Programa: Ingeniería de sistemas
# Código fuente: Autoría Propia

#INGRESO DE INVENTARIO

# Matriz con la información del inventarío de la papelería.
# Cada fila contiene:
# [Código, nombre del artículo, stock actual y stock minimo]

inventario = [
    ["P001", "Cuaderno", 15, 20],
    ["P002", "Lápiz", 50, 40],
    ["P003", "Borrador", 8, 10],
    ["P004", "Resma de papel", 5, 10],
    ["P005", "Marcador", 12, 12]
]

#CALCULAR REABASTECIMIENTO

def calcular_reabastecimiento(stock_actual, stock_minimo):
    """
    Calcula la cantidad de unidades que se deben solicitarse para un artículo del inventarío.
    """
    
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
        
    return cantidad

# GENERAR EL INFORME

def mostrar_informe(inventario):
    """
    Recorre el inventario y muetra la cantidad de unidades que deben solicitarse para cada artículo.
    """
    
    print("\n==============================================")
    print("     INFORME DE REABASTECIMIENTO")
    print("==============================================")
    print("{:<8} {:<20} {:>10}".format("código", "Artículo", "Cantidad"))
    print("----------------------------------------------")
    
    for articulo in inventario:
        
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        cantidad = calcular_reabastecimiento(stock_actual, stock_minimo)
        
        print("{:<8} {:<20} {:<10}".format(codigo, nombre, cantidad))
        
        print("==============================================")
        
        
#INFORME
        
def main():
    """
    Función principal del programa.
    """
    
    mostrar_informe(inventario)
    

#INICIO DEL PROGRAMA
    
if __name__ == "__main__":
    main()