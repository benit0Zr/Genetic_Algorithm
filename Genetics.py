#importar modulo random para generar numeros aleatorios
import random
#importar libreria numpy
import numpy as np


class DNA(object):

    """
        Esta clase nos permite guardar los genes de cada individuo en un arreglo
    """

    genes = np.array([]) #Inicializar arreglo vacio
    fitness = 0
    def __init__(self, size, genSet):
        # Genera un arreglo de caracteres aleatorios
        self.genes = np.array(random.sample(genSet, size))
        
    def mutate(self, parentA, parentB, genSet, mutation_rate):

        """
            Esta funcion se encarga de recolectar los genes del padreA y padreB,
            la probabilidad de mutacion, posteriormente se realiza el cruze para alcanzar el objetivo
        """

        #Nuevo arreglo que continen los nuevos genes del cruze 
        newGenes = np.zeros(parentA.genes.shape[0])
        midPoint = random.randint(0, parentA.genes.shape[0])
        for ix in range(len(self.genes)):
            if random.random() < mutation_rate:
                newGenes[ix] = random.sample(genSet, 1)[0]
            else:
                newGenes[ix] = parentA.genes[ix] if ix < midPoint \
                                                else parentB.genes[ix]
                
        self.genes = newGenes
            
class Population(object):

    """ 
        Esta clase sirve para administrar todos los DNA de cada individuo,
        asi como hacer las nuevas generaciones o mandar a llamar las mutaciones necesarias
    """
    pop = np.array([])
    def __init__(self, target, maxPop, genSet, mutation):
        #Conjunto de genes posibles para la poblacion
        self.genSet = np.array(map(lambda x: ord(x), genSet))
        #Frase objetivo
        self.target = np.array(map(lambda x: ord(x), target)) 
        #Poblacion maxima       
        self.maxPop = maxPop
        #Mejor puntuacion de fitness
        self.biggest = 0
        #Fitness promedio de la poblacion
        self.avg_fitness = 0
        #Porcentaje de mutacion
        self.mutation_rate = mutation
        
        #Creacion aleatoria de la poblacion inicial
        while self.pop.shape[0] < maxPop:
            self.pop = np.append(self.pop, DNA(self.target.shape[0], self.genSet))
            
    def calculateFitness(self):
        """
            Determina el mejor fitness de cada generacion
            La mejor puntuacion es la suma de las letras correctas
        """
        #Posicion del mayor fitness
        self.biggest = 0
        #Posicion del segundo mayor fitness
        self.second = 0
        #Fitness promedio
        self.avg_fitness = 0
        for ix in range(self.pop.shape[0]):
        
            self.pop[ix].fitness = (self.pop[ix].genes == self.target).sum()
            self.avg_fitness+= float(self.pop[ix].fitness) / self.target.shape[0]            
            #Guarda los 2 mejores resultados para reproducirlos
            if self.pop[ix].fitness > self.pop[self.biggest].fitness:
                self.biggest = ix
            elif self.pop[ix].fitness > self.pop[self.second].fitness:
                self.second = ix
        #Calcula el prodemio del fitness
        self.avg_fitness = (self.avg_fitness / self.pop.shape[0]) * 100.0
                
    def nextGeneration(self):
        """
            Teniendo los fitness mas altos, esta funcion se encarga de cruzar los padres agregando un 10%
            de mutacion.
        """        
        #Genes de los mejores 
        parentA =  self.pop[self.biggest]
        parentB =  self.pop[self.second]
        #Por cada nuevo individuo
        for ix in range(self.pop.shape[0]):
            child = DNA(parentA.genes.shape[0], self.genSet)
            #Cruza de los genes de los 2 padres
            child.mutate(parentA, parentB, self.genSet, self.mutation_rate)
            #Nuevo individuo de la poblacion
            self.pop[ix] = child
            
    def __str__(self):
        """
            Imprimir todos los genes de la poblacion
        """
        st= ""
        for i in self.pop:
            st += ''.join([chr(int(el)) for el in i.genes]) + "\n"
        return st
    
    def evaluate(self):
        #Retorna verdadero si cumple con el objetivo
        return not (self.pop[self.biggest].genes == self.target).all()

