from cProfile import label
from matplotlib.pyplot import legend
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.factory import get_performance_indicator
import numpy as np

problems = ['zdt1', 'zdt2', 'zdt3']
r_points = [[1, 1.02], [1, 1.02], [ 0.86, 1.02]]

for p, r in zip(problems, r_points):
    problem = get_problem(p)

    algorithm = NSGA2(
                    pop_size=100,
                    mutation=PolynomialMutation(prob=0.2, eta=20)
                        )

    res = minimize(problem,
                algorithm,
                ('n_gen', 250),
                seed=1,
                verbose=False)

    plot = Scatter()
    plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
    plot.add(res.F, facecolor="none", edgecolor="red")
    plot.show()
    gd = get_performance_indicator("igd", problem.pareto_front())
    print("IGD :", gd.do(res.F))
    hv = get_performance_indicator("hv", ref_point=np.array(r))
    print("hv", hv.do(res.F))