import pyvrp
from pyvrp import read
from pyvrp.stop import MaxIterations  # or another stopping condition

# print(dir(pyvrp))
# Example distance matrix (symmetric)

# Create a VRP model
model = pyvrp.Model()

# Process the file data vrp no time windows
INSTANCE = read("data/vrpsmall.vrp", round_func="round")
model = model.from_data(INSTANCE)

# Define the stopping criterion (e.g., max 1000 iterations)
stop_criterion = MaxIterations(1000)

# Solve the VRP
solution = model.solve(stop=stop_criterion)
with open("output_vrp.txt", "w") as f:
    feasible = str(solution.best.is_feasible())
    f.write(feasible)
    f.write("\n")
    distance = str(solution.best.distance())
    f.write(distance)
    f.write("\n")
    string = str(solution.best)
    # print(solution.best.routes())
    f.write(string)

# Display the solution
print(solution)
