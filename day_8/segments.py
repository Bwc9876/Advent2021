
"""
Test Inputs
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

digits = {
  'abcefg': 0,
  'cf': 1,
  'acdeg': 2,
  'acdfg': 3,
  'bcdf': 4,
  'abdfg': 5,
  'abdefg': 6,
  'acf': 7,
  'abcdefg': 8,
  'abcdfg': 9
}

unique_lengths = {
  2: 1,
  3: 7,
  4: 4,
  7: 8,
}

normal_mapping = 'abcdefg'

def map(mappings, sequence):
  mapped_sequence = ''
  for char in sorted(sequence):
    mapped = mappings.get(char)
    if mapped is None:
      mapped_sequence += '?'
    else:
      mapped_sequence += mapped
  return f"{sequence}->{mapped_sequence}"

def identify(sequence, mappings=None):
  seq_len = len(sequence)
  if mappings is None:
    if seq_len in unique_lengths.keys():
      return unique_lengths.get(seq_len)
  else:
    return None if mappings is None else map(mappings, sequence)

class NoteEntry:

  def __init__(self, raw_entry):
      split = raw_entry.split("|")
      self.codes = [x.strip() for x in split[0].split(" ")]
      self.outputs = [x.strip() for x in split[1].split(" ")]
      self.mappings = {x: None for x in normal_mapping}

  def get_by_target(self, target_wire):
    for k, v in self.mappings.items():
      if v is not None and  v == target_wire:
        return k
      return None

  def determine_f(self, mystery_inputs):
    for code in self.codes + self.outputs:
      if len(code) == 6:
        if mystery_inputs[0] in code and mystery_inputs[1] not in code:
          self.mappings[mystery_inputs[0]] = 'f' 
          self.mappings[mystery_inputs[1]] = 'c' 
        elif mystery_inputs[0] in code and mystery_inputs[1] not in code:
          self.mappings[mystery_inputs[0]] = 'c' 
          self.mappings[mystery_inputs[1]] = 'f' 

  def determine_g_depend_a(self, mystery_inputs):
    if self.get_by_target('a') is not None:
      for code in self.codes + self.outputs:
        if len(code) == 6:
          intermin_output = code
          intermin_output = intermin_output.replace(self.get_by_target('a'), '')
          for x in mystery_inputs:
            intermin_output = intermin_output.replace(x, '')
          if len(intermin_output) == 1:
            self.mappings[intermin_output] = 'g'


  def determine_e_depend_g_and_a(self, mystery_inputs):
    if self.get_by_target('a') is not None and self.get_by_target('g') is not None:
      for code in self.codes + self.outputs:
        if len(code) == 7:
          intermin_output = code.replace(self.get_by_target('a'), '')
          intermin_output = intermin_output.replace(self.get_by_target('g'), '')
          for x in mystery_inputs:
            intermin_output = intermin_output.replace(x, '')
          if len(intermin_output) == 1:
            self.mappings[intermin_output] = 'e'

  def determine_d_depend_g_a_and_e(self, mystery_inputs):
    if self.get_by_target('a') is not None and self.get_by_target('g') is not None and self.get_by_target('e') is not None:
      for code in self.codes + self.outputs:
        if len(code) == 7:
          intermin_output = code.replace(self.get_by_target('a'), '')
          intermin_output = intermin_output.replace(self.get_by_target('g'), '')
          intermin_output = intermin_output.replace(self.get_by_target('e'), '')
          for x in mystery_inputs:
            intermin_output = intermin_output.replace(x, '')
          if len(intermin_output) == 1:
            self.mappings[intermin_output] = 'e'

  def determine_a(self, mystery_inputs):
    for output in self.outputs:
      if identify(output) == 7:
        intermin_output = output
        intermin_output = intermin_output.replace(mystery_inputs[0], '')
        intermin_output = intermin_output.replace(mystery_inputs[1], '')
        self.mappings[intermin_output] = 'a'


  def get_outputs(self):
    out_outputs = []
    for output in sorted(self.outputs, key=lambda l:  len(l)):
      number = identify(output)
      if number is not None:
        if number == 1:
          self.determine_f(output)
          self.determine_a(output)
        elif number == 4:
          self.determine_g_depend_a(output)
          self.determine_e_depend_g_and_a(output)
          self.determine_d_depend_g_a_and_e(output)
    for output in self.outputs[1:]:
      out_outputs.append(identify(output, mappings=self.mappings))
    return out_outputs


def get_output_digits(raw_entries):
  notes = []
  for raw_entry in raw_entries:
    notes.append(NoteEntry(raw_entry))
  out_outputs = []
  for entry in notes:
    outputs = entry.get_outputs()
    out_outputs.append(outputs)
  return out_outputs


if __name__ == "__main__":
  raw_entries = []
  with open("8.txt", 'r') as file:
    raw_entries = file.readlines()
  print(get_output_digits(raw_entries))

  