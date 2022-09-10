from statistics import mean
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import math
import numpy as np


class Exercise1(object):
    

    def __init__(self):
        
        self.x_arr = []
        self.y_arr = []
        self.p = 1/3
        self.x = 0
        self.y = 0

    def half_func(self,x, y):
        x, y = x/2, y/2
        return x, y

    def half_func_dotFive(self, x, y):
        x, y = ((x+1)/2), y/2
        return x, y

    def half_func_dot_quarter_five(self, x, y):
        x, y = (((2*x)+1)/4), ((y+1)/2)
        return x, y

    def execute(self):

        self.x, self.y = 0.5, 0.5
        random_ = 0
        for i in range(1000000):
            random_ = random.random()
            self.x_arr.append(self.x)
            self.y_arr.append(self.y)

            if (random_ < self.p):
                func = self.half_func
            elif (self.p <= random_ and random_ < (1-self.p)):
                func = self.half_func_dotFive
            else:
                func = self.half_func_dot_quarter_five

            self.x, self.y = func(self.x, self.y)

        plt.scatter(self.x_arr, self.y_arr, color='blue', marker='8', edgecolors='purple')
        plt.show()  

# Cumulative ponderated function


class Exercise2(object):

    def __init__(self):
        
        self.probs = [0.80, 0.07, 0.13]
        self.x_arr = []
        self.y_arr = []
        self.x = 0
        self.y = 0

    def dist_1(self,x, y):
        x, y = (x/5 + (13/50)*y), (((23*x)/100) + (11/50)*y + (3/5))
        return x, y

    def dist_2(self, x, y):
        x, y = 0, ((4*y)/25)
        return x, y

    def dist_3(self, x, y):
        x, y = ((x*3)/20 + (7/25)*y), (((13*x)/50) + (6/25)*y + (11/25))
        return x, y

    def execute(self):

        self.x, self.y = 1/2, 1/2
        random_ = 0
        for i in range(1000000):
            random_ = random.random()
            self.x_arr.append(self.x)
            self.y_arr.append(self.y)
    
            if (random_ < self.probs[0]):
                func = self.dist_1
            elif (self.probs[0] <= random_ and random_ < (self.probs[0] + self.probs[1])):
                func = self.dist_2
            else:
                func = self.dist_3

            self.x, self.y = func(self.x, self.y)

        plt.hist(self.x_arr, color='blue')
        plt.xlabel('Probs')
        plt.ylabel('Frequency')
        plt.title('Histogram of repetitions')
        plt.show() 
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

    def validate(self, results):
        for product in results:
            print(f"Resultados para el caso de {product[0]['quantity']} periodicos")
            gains_list = [x['gains'] for x in product]
            #solds_list = [x['sold'] for x in product]
            not_solds_list = [x['not_sold'] for x in product]
            could_sell_list = [x['could_sell'] for x in product]
            print(f" - La ganancia es: {sum(gains_list)} y el promedio por dia es: {mean(gains_list)}")
            print(f" - El promedio de periodicos no vendidos es: {mean(not_solds_list)}")
            print(f" - El promedio de periodicos que pude haber vendido es: {mean(could_sell_list)}")
        print("-------")
        # Get the product with the highest gains mean
        product = max(results, key=lambda x: mean([y['gains'] for y in x]))
        # Check if another product has the same gains mean
        if len(list(filter(lambda x: mean([y['gains'] for y in x]) == mean([y['gains'] for y in product]), results))) > 1:
            # Get the product with the lowest not sold mean
            product = min(results, key=lambda x: mean([y['not_sold'] for y in x]))
            # Check if another product has the same not sold mean
            if len(list(filter(lambda x: mean([y['not_sold'] for y in x]) == mean([y['not_sold'] for y in product]), results))) > 1:
                # Get the product with the lowest could sell mean
                product = min(results, key=lambda x: mean([y['could_sell'] for y in x]))
        print(f"La cantidad de periodicos a comprar es: {product[0]['quantity']}")

    def execute(self):
        product_quantity = [9, 10, 11]
        product_price = 1.5
        product_selling_price = 2.5
        product_not_sell_refund = 0.5
        simulation_days = [30, 365, 3650]
        for days in simulation_days:
            if days == 30:
                print("\nResultados para 30 días:")
            elif days == 365:
                print("\nResultados para 1 año:")
            else:
                print("\nResultados para 10 años:")
            products_results = []
            for quantity in product_quantity:
                simulation_results = []
                # simulation for each day
                for day in range(days):
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
                    day_results = {
                        "quantity": quantity,
                        "gains": gains,
                        "days_n": days,
                        "day_i": day,
                        "sold": quantity - products_not_sold,
                        "not_sold": products_not_sold,
                        "could_sell": products_I_could_sell,
                    }
                    simulation_results.append(day_results)
                products_results.append(simulation_results)
            self.validate(products_results)

exercise1 = Exercise1()
exercise2 = Exercise2()
exercise3 = Exercise3()
exercise4 = Exercise4()
#exercise1.execute()
exercise2.execute()
# exercise3.execute()
#exercise4.execute()
