from statistics import median

def get_cheapest_fuel(raw_crabs):
  crabs = sorted([int(x) for x in raw_crabs.split(",")])
  target_num = median(crabs)
  cost = sum([abs(target_num - x) for x in crabs])
  return cost

def get_cheapest_fuel_exponential(raw_crabs):
  crabs = [int(x) for x in raw_crabs.split(",")]
  




if __name__ == "__main__":
  lines = []
  with open("7.txt", 'r') as file:
    lines = file.readlines()
  print(get_cheapest_fuel(lines[0]))