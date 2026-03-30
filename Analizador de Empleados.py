import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import janitor

df = pd.read_csv("Analizador CSV.csv")
df = df.clean_names()

df["rendimiento"] = df["ventas"] / df ["salario"]
df["eficiencia en ventas"] = df["ventas"] / df["horas_trabajadas"]
df["categoria"] = df["rendimiento"].apply(lambda x: "Alto" if x > df["rendimiento"].median() else "Bajo")

promedio_ventas = df["ventas"].mean()

top_5_empleados = df.sort_values(by="ventas", ascending=False).head(5)

peores_empleados = df.sort_values(by="ventas").head(5)

ventas_departamento = df.groupby("departamento")["ventas"].sum().reset_index()

categorias = df["categoria"].value_counts().reset_index()

dataset_completo = df.copy()

orden_por_rendimiento = df.sort_values(by="rendimiento", ascending=False)

orden_por_eficiencia = df.sort_values(by="eficiencia en ventas", ascending=False)

print("Bienvenido al Analizador de Empleados")

while True:
    print("\nMENU:")
    print("1.Mostrar promedio de ventas")
    print("2.Mostrar top 5 empleados")    
    print("3.Mostrar peores empleados")
    print("4.Mostrar ventas por departamento")
    print("5.Mostrar categorias de rendimiento")
    print("6.Mostrar dataset completo")
    print("7.Ordenar por rendimiento")
    print("8.Ordenar por eficiencia en ventas")
    print("9.Menu de visualizaciones")
    print("10.Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(promedio_ventas)

    elif opcion == "2":
        print(top_5_empleados)

    elif opcion == "3":
        print(peores_empleados)

    elif opcion == "4":
        print(ventas_departamento)
    
    elif opcion == "5":
        print(categorias)

    elif opcion == "6":
        print(dataset_completo)
    
    elif opcion == "7":
        print(orden_por_rendimiento)
    
    elif opcion == "8":
        print(orden_por_eficiencia)
    
    elif opcion == "9":
        print("\nVisualizaciones:")
        print("1. Ventas por departamento")
        print("2. Distribución de categorías de rendimiento")
        print("3. Relación entre salario y ventas")

        sub_opcion = input("Seleccione una opción de visualización: ")

        if sub_opcion == "1":
            sns.set_style("whitegrid")
            plt.figure(figsize=(10, 6))
            sns.barplot(x="departamento", y="ventas", data=ventas_departamento, palette="Set2")
            plt.title("Ventas por Departamento")
            plt.xlabel("Departamento")
            plt.ylabel("Ventas Totales")
            plt.xticks(rotation=45)
            plt.show()

        elif sub_opcion == "2":
            sns.set_style("whitegrid")
            plt.figure(figsize=(8, 5))
            sns.countplot(x="categoria", data=df, palette="Set1")
            plt.title("Distribución de Categorías de Rendimiento")
            plt.xlabel("Categoría de Rendimiento")
            plt.ylabel("Cantidad de Empleados")
            plt.show()
        
        elif sub_opcion == "3":
            sns.set_style("whitegrid")
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x="salario", y="ventas", data=df, color="green")
            plt.title("Relación entre Salario y Ventas")
            plt.xlabel("Salario")
            plt.ylabel("Ventas")
            plt.show()

        elif opcion == "10":
         print("Gracias por usar el Analizador de Empleados. ¡Hasta luego!")
         break

    
  

