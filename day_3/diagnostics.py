


def bin_to_dec(input_bin: str):
  output_dec = 0
  for index, number in enumerate(reversed(input_bin)):
    mult = 2 ** index
    output_dec += int(number) * mult
  return output_dec

def get_counts(input_bins):
  counts = [[0, 0] for x in range(len(input_bins[0]))]
  for byte in input_bins:
    print("Line: ", input_bins.index(byte))
    for index, bit in enumerate(byte[:-1]):
      counts[index][int(bit)] += 1
  return counts

def contruct_gamma_rate(counts):
  output_bin = ""
  for pair in counts:
    output_bin += "0" if pair[0] > pair[1] else "1"
  return output_bin, bin_to_dec(output_bin)

def construct_epsilon_rate(counts):
  output_bin = ""
  for pair in counts:
    output_bin += "0" if pair[0] < pair[1] else "1"
  return output_bin, bin_to_dec(output_bin)  

def get_rates(input_bytes):
  counts = get_counts(input_bytes)
  bin_gamma, dec_gamma = contruct_gamma_rate(counts)
  bin_epsilon, dec_epsilon = construct_epsilon_rate(counts)
  print("Binary Gamma: ", bin_gamma)
  print("Binary Epsilon: ", bin_epsilon)
  print("Decimal Gamma: ", dec_gamma)
  print("Decimal Epsilon: ", dec_epsilon)
  print("Power Consumption Rate: ", dec_epsilon * dec_gamma)

if __name__ == "__main__":
  input_list = []
  with open("3.txt", 'r') as file:
    input_list = file.readlines()
  get_rates(input_list)