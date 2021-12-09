
def get_at_pos(arr, x, y, fail_return=True):
  try:
    if x < 0 or y < 0:
      raise IndexError()
    return arr[y][x]
  except IndexError as error:
    if fail_return:
      return None
    else:
      raise error


def construct_2d_array(raw_lines):
  return [[int(x) for x in y.strip()] for y in raw_lines]


def get_basin(arr, x, y, basin=None):
  if basin is None:
    basin = [((x, y), get_at_pos(arr, x, y))]
  for adj in find_adjacents(arr, x, y):
    if adj[1] != 9 and adj[0] not in [i[0] for i in basin]:
      basin.append(adj)
      basin += get_basin(arr, adj[0][0], adj[0][1], basin=basin)
      basin = list(set(basin))
  return basin


def get_three_largest_basins(arr, lowpoints):
  basins = [get_basin(arr, lp[0], lp[1]) for lp in lowpoints]
  basins = sorted(basins, key=lambda b: len(b), reverse=True)
  print([len(b) for b in basins])
  return basins[:3]


def find_adjacents(arr, x, y):
  to_find = ((0, 1), (0, -1), (1, 0), (-1, 0))
  out_arr = [((x + search[0], search[1] + y), get_at_pos(arr, x + search[0], y + search[1])) for search in to_find]
  return [i for i in out_arr if i[1] is not None]


def find_lowpoints(arr):
  lowpoints = []
  for y, row in enumerate(arr):
    for x in range(len(row)):
      val = get_at_pos(arr, x, y, fail_return=False)
      adjacents = find_adjacents(arr, x, y)
      lowpoint = True
      for i in adjacents:
        if val >= i[1]:
          lowpoint = False
          break
      if lowpoint:
        lowpoints.append((x, y))
  return lowpoints


def find_lowpoint_sum(raw_input):
  arr = construct_2d_array(raw_input)
  lowpoints = find_lowpoints(arr)
  return sum([get_at_pos(arr, i[0], i[1], fail_return=False) + 1 for i in lowpoints])

def get_basin_data(raw_input):
  arr = construct_2d_array(raw_input)
  lowpoints = find_lowpoints(arr)
  basins = get_three_largest_basins(arr, lowpoints)
  total = 1
  for basin in basins:
    print(len(basin))
    total *= len(basin)
  return total

if __name__ == "__main__":
  raw_lines = []
  with open("9.txt", 'r') as file:
    raw_lines = file.readlines()
  print("Total Risk Level:", find_lowpoint_sum(raw_lines))
  print("Basin Data:", get_basin_data(raw_lines))
  
  