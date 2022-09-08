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
            print(
                f"No se recomienda invertir en el proyecto {project['name']} ni en ninguno de los otros proyectos")
        else:
            print(f"El proyecto más rentable es: {project['name']}")
            print(
                f"La probabilidad de que el proyecto sea rentable es: {project['positive_rate'] / project['iterations']}")
            print(
                f"La media del valor actual neto es: {project['mean']} en {project['iterations']} simulaciones")
            print(f"La inversión inicial es: {project['investment']}")

    def execute(self):
        k = 0.1  # discount rate
        project1 = {"name": "Hotel", "data": [(None, -800, None), ('normal', -800, 50), ('normal', -800, 100), (
            'normal', -700, 150), ('normal', 300, 200), ('normal', 400, 200), ('normal', 500, 200), ('uniform', 200, 8440)]}
        project2 = {"name": "Centro Comercial", "data": [(None, -900, None), ('normal', -600, 50), ('normal', -200, 100), (
            'normal', -600, 100), ('normal', 250, 150), ('normal', 350, 150), ('normal', 400, 150), ('uniform', 1600, 6000)]}
        simulation_iterations = [100, 1000, 10000]  # n of simulations
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
                    "positive_rate": sum([self.decision(npv) for npv in npvs]),
                    "mean": np.mean(npvs),
                    "investment": project['data'][0][1],
                    "iterations": n
                }
                projects_results.append(project_results)
            # print results.
            self.compare_results(projects_results)

# Find the best quantity to buy
class Exercise4(object):

    def __init__(self):
        pass

    def execute(self):
        product_quantity = [9, 10, 11]
        product_price = 1.5
        product_selling_price = 2.5
        product_not_sell_refund = 0.5
        simulation_days = [3]
        for days in simulation_days:
            if days == 30:
                print("\nResultados para 30 días")
            elif days == 365:
                print("\nResultados para 1 año")
            else:
                print("\nResultados para 10 años")
            for quantity in product_quantity:
                # simulation for each day
                for _ in range(days):
                    gains = 0
                    # purchase of products to sell
                    gains -= (quantity * product_price)
                    products_not_sold = quantity
                    products_I_could_sell = 0
                    # random number of products sold
                    random_probability = random.random()
                    # 30% when quantity requested is 9
                    if random_probability < 0.3:
                        gains += (9 * product_selling_price)
                        products_not_sold -= 9
                    # 40% when quantity requested is 10
                    elif 0.3 <= random_probability < 0.7:
                        if quantity < 10:
                            gains += (quantity * product_selling_price)
                            products_not_sold -= quantity
                            products_I_could_sell = 10 - quantity
                        else:
                            gains += (10 * product_selling_price)
                            products_not_sold -= 10
                    # 30% when quantity requested is 11
                    elif 0.7 <= random_probability <= 1:
                        if quantity < 11:
                            gains += (quantity * product_selling_price)
                            products_not_sold -= quantity
                            products_I_could_sell = 11 - quantity
                        else:
                            gains += (11 * product_selling_price)
                            products_not_sold -= 11
                    # refund of products not sold
                    gains += (products_not_sold * product_not_sell_refund)
                    print(f"Productos comprados: {quantity}")
                    print(f"Productos vendidos: {quantity - products_not_sold}")
                    print(f"Productos no vendidos: {products_not_sold}")
                    print(f"Productos que pude vender: {products_I_could_sell}")
                    print(gains)

exercise1 = Exercise1()
exercise2 = Exercise2()
exercise3 = Exercise3()
exercise4 = Exercise4()
# exercise1.execute()
# exercise2.execute()
# exercise3.execute()
exercise4.execute()
