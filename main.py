#importar el script Genetics
import Genetics
#Importar modulo string, para generar lista de genes
import string
# Importar liberia numpy como np
import numpy as np
        
def main():
    """
        Esta funcion realiza lo siguiente:
        - Inicializa la poblacion inicial
        - Evalua cada individuo de la poblacion
        - Selecciona los mejores individuos
        - Cruza los genes
        - Aplica la mutacion
        - Muestra en pantalla el numero de generacion con la frase objetivo
        
    """
    #Lsta de caracteres para los genes
    genSet = string.letters + string.punctuation + " " + string.digits        
    #Frase objetivo
    target = "Genetics Algorithms"  
    #Poblacion maxima
    maxPop = 500
    #Porcentaje de mutacion del 10%
    mutation = 0.1
    
    #Generar la poblacion
    population = Genetics.Population(target, maxPop, genSet, mutation)
    #Arreglo vacio para guardar las generaciones
    generations = np.array([])
    #Contador de generaciones
    generation = 1
    #Mientras no se alcanze el objetivo
    while population.evaluate():
        #Evaluar fitness
        population.calculateFitness()  
        #Seleccion, cruce de genes y mutacion      
        population.nextGeneration()        
        #Guardar las generaciones
        generations = np.append(generations,np.array([population.avg_fitness]))
        #Imprimir en pantalla el numero de generaciones
        print("Generaciones:", generation)
        #Imprimir en pantalla el promedio de cada generacion
        print("fitness:", "%.2f" % population.avg_fitness + "%")
        #Imprime en pantalla la frase encontrada en cada generacion
        print("Genes:", ''.join(map(lambda x: chr(int(x)),
                                 population.pop[population.biggest].genes)))
        #Siguiente generacion                         
        generation+=1
    
   
    
    print("="*20)
    #Imprime en pantalla el numero de generacion, quien alcanzo el objetivo
    print("Generacion final:", generation)
    #Imprime frase objetivo
    print("Genes: ", ''.join(map(lambda x: chr(int(x)),
                                 population.pop[population.biggest].genes)))

if __name__ == '__main__':
    #Ejecuta la funcion main()
    main()
