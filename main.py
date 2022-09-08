import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import math
import numpy as np


class Exercise1(object):

    def __init__(self):
        pass

    def execute(self, n):
        pass

# Cumulative ponderated function


class Exercise2(object):

    def __init__(self):
        pass

    # Receives a probability mass function
    def execute(self, pmf):
        pass

# Project rentability


class Exercise3(object):

    def __init__(self):
        pass

    # returns a random number from a normal distribution
    def normal(self, mean, std):
        return np.random.normal(mean, std)

    # returns a random number from a uniform distribution
    def uniform(self, a, b):
        return random.uniform(a, b)

    # npv function for each time
    def npv_i(self, k, f, i):
        return f / (1 + k) ** i

    # if npv > 0 then the project is profitable, otherwise it is not
    def decision(self, npv):
        if npv > 0:
            return 1
        else:
            return 0

    def compare_results(self, projects_results):
        # Get the project with most cases of positive npv
        project = max(projects_results, key=lambda x: x['positive_rate'])
        # Check if another project has the same positive rate
        if len(list(filter(lambda x: x['positive_rate'] == project['positive_rate'], projects_results))) > 1:
            # If so, get the project with the highest mean
            project = max(projects_results, key=lambda x: x['mean'])
        # If project is not profitable, then it is not recommended
        if project['positive_rate'] == 0:
            print(f"No se recomienda invertir en el proyecto {project['name']} ni en ninguno de los otros proyectos")
        else:
            print(f"El proyecto más rentable es: {project['name']}")
            print(f"La probabilidad de que el proyecto sea rentable es: {project['positive_rate'] / project['iterations']}")
            print(f"La media del valor actual neto es: {project['mean']} en {project['iterations']} simulaciones")
            print(f"La inversión inicial es: {project['investment']}")

    def execute(self):
        k = 0.1  # discount rate
        project1 = {"name": "Hotel", "data": [(None, -800, None), ('normal', -800, 50), ('normal', -800, 100), (
            'normal', -700, 150), ('normal', 300, 200), ('normal', 400, 200), ('normal', 500, 200), ('uniform', 200, 8440)]}
        project2 = {"name": "Centro Comercial", "data": [(None, -900, None), ('normal', -600, 50), ('normal', -200, 100), (
            'normal', -600, 100), ('normal', 250, 150), ('normal', 350, 150), ('normal', 400, 150), ('uniform', 1600, 6000)]}
        simulation_iterations = [100, 1000, 10000] # n of simulations
        for n in simulation_iterations:
            print(f"\nResultados de la simulación con {n} iteraciones")
            projects_results = []
            for project in [project1, project2]:
                npvs = []
                # n siulations
                for _ in range(n):
                    npv = 0
                    time_i = 0
                    for time in project['data']:
                        if time[0] == 'normal':
                            f_random = self.normal(time[1], time[2])
                            npv += self.npv_i(k, f_random, time_i)
                        elif time[0] == 'uniform':
                            f_random = self.uniform(time[1], time[2])
                            npv += self.npv_i(k, f_random, time_i)
                        else:
                            # always be the first one (investment)
                            npv += time[1]
                        time_i += 1
                    npvs.append(npv)
                project_results = {
                    "name": project['name'],
                    "npvs": npvs,
                    "positive_rate": sum([ self.decision(npv) for npv in npvs]),
                    "mean": np.mean(npvs),
                    "investment": project['data'][0][1],
                    "iterations": n
                }
                projects_results.append(project_results)
            # print results.
            self.compare_results(projects_results)


class Exercise4(object):

    def __init__(self):
        pass

    def execute(self):
        pass


exercise1 = Exercise1()
exercise2 = Exercise2()
exercise3 = Exercise3()
exercise4 = Exercise4()
# exercise1.execute()
# exercise2.execute()
exercise3.execute()
# exercise4.execute()
