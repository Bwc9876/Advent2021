from typing import Optional

from utils import get_input_list

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

normal_mapping = 'abcdefg'


class NoteEntry:
    """
        An entry in the notebook

        :ivar codes: The codes to map from
        :type codes: list[str]
        :ivar outputs: The outputs to use the map to process
        :type outputs: list[str]
        :ivar mappings: The mappings of the entry, what letter goes to what other letter
        :type mappings: dict[str, str]
    """

    def __init__(self, raw_entry: str):
        """
            Instantiates a new NoteBook entry

            :param raw_entry: The entry as raw data
            :type raw_entry: str
        """

        split = raw_entry.split("|")
        self.codes = [x.strip() for x in split[0].split(" ")][:-1]
        self.outputs = [x.strip() for x in split[1].split(" ")][1:]
        self.mappings = {x: None for x in normal_mapping}
        self.create_map()

    def map(self, sequence: str) -> int:
        """
            Using the map, map a sequence of letters to another sequence of letters

            :param sequence: The sequence to convert
            :type sequence: str
            :returns: The sequence as a integer as displayed on a seven-segment display
            :rtype: int
        """

        mapped_sequence = ''
        for char in sorted(sequence):
            mapped = self.mappings.get(char)
            if mapped is None:
                mapped_sequence += '?'
            else:
                mapped_sequence += mapped
        return digits.get(''.join(sorted(mapped_sequence)))

    def get_by_target(self, target_wire: str) -> Optional[str]:
        """
            Gets a map entry by the target letter

            :param target_wire: The wire to reverse teh dictionary for
            :type target_wire: str
            :returns: The wire the target_wire has been mapped to
            :rtype: Optional[str]
        """

        for k, v in self.mappings.items():
            if v is not None and v == target_wire:
                return k
        return None

    def determine_f_and_c(self, mystery_inputs: str) -> None:
        """
            Determines the f and c wire given the code for 1

            :param mystery_inputs: The code for 1 on the display
            :type mystery_inputs: str
        """

        for code in self.codes:
            if len(code) == 6:
                if mystery_inputs[0] in code and mystery_inputs[1] not in code:
                    self.mappings[mystery_inputs[0]] = 'f'
                    self.mappings[mystery_inputs[1]] = 'c'
                elif mystery_inputs[1] in code and mystery_inputs[0] not in code:
                    self.mappings[mystery_inputs[0]] = 'c'
                    self.mappings[mystery_inputs[1]] = 'f'

    def determine_a(self, mystery_inputs: str) -> None:
        """
            Determines the a wire given the code for 7

            :param mystery_inputs: The code for 7 on the display
            :type mystery_inputs: str
        """

        f = self.get_by_target('f')
        c = self.get_by_target('c')
        a = mystery_inputs.replace(f, '').replace(c, '')
        self.mappings[a] = 'a'

    def determine_b(self, mystery_inputs: str) -> None:
        """
            Determines the b wire given the code for 3

            :param mystery_inputs: The code for 3 on the display
            :type mystery_inputs: str
        """

        for code in self.codes:
            if len(code) == 6 and False not in [x in code for x in mystery_inputs]:
                b = code
                for x in mystery_inputs:
                    b = b.replace(x, '')
                self.mappings[b] = 'b'

    def determine_d(self, mystery_inputs: str) -> None:
        """
            Determines the d wire given the code for 4

            :param mystery_inputs: The code for 4 on the display
            :type mystery_inputs: str
        """

        f = self.get_by_target('f')
        c = self.get_by_target('c')
        b = self.get_by_target('b')
        d = mystery_inputs.replace(f, '').replace(c, '').replace(b, '')
        self.mappings[d] = 'd'

    def determine_g(self, mystery_inputs: str) -> None:
        """
            Determines the g wire given the code for 9

            :param mystery_inputs: The code for 9 on the display
            :type mystery_inputs: str
        """

        f = self.get_by_target('f')
        c = self.get_by_target('c')
        b = self.get_by_target('b')
        a = self.get_by_target('a')
        d = self.get_by_target('d')
        g = mystery_inputs.replace(f, '').replace(c, '').replace(b, '').replace(a, '').replace(d, '')
        self.mappings[g] = 'g'

    def determine_e(self) -> None:
        """
            Determines the e wire from every other wire
        """

        f = self.get_by_target('f')
        c = self.get_by_target('c')
        b = self.get_by_target('b')
        a = self.get_by_target('a')
        d = self.get_by_target('d')
        g = self.get_by_target('g')
        e = 'abcdefg'.replace(f, '').replace(c, '').replace(b, '').replace(a, '').replace(d, '').replace(g, '')
        self.mappings[e] = 'e'

    def create_map(self) -> None:
        """
            Creates the map for the given codes
        """

        fc_code = next((code for code in self.codes if len(code) == 2), None)
        self.determine_f_and_c(fc_code)
        a_code = next((code for code in self.codes if len(code) == 3), None)
        self.determine_a(a_code)
        b_code = next((code for code in self.codes if len(code) == 5 and self.get_by_target('c') in code and self.get_by_target('f') in code), None)
        self.determine_b(b_code)
        d_code = next((code for code in self.codes if len(code) == 4), None)
        self.determine_d(d_code)
        g_code = next((code for code in self.codes if len(code) == 6 and self.get_by_target('c') in code and self.get_by_target('d') in code), None)
        self.determine_g(g_code)
        self.determine_e()

    def get_outputs(self) -> int:
        """
            Gets the sum of all output number

            :returns: The sum of outputs for this entry
            :rtype: int
        """

        out_str = ""
        for output in self.outputs:
            out_str += str(self.map(output))
        return int(out_str)


def get_output(raw_entries: list[str]) -> int:
    """
        Gets the total output for a given list of entries

        :param raw_entries: The entries as raw lines
        :type raw_entries: list[str]
        :returns: The total output of all entries
        :rtype: int
    """

    notes = []
    for raw_entry in raw_entries:
        notes.append(NoteEntry(raw_entry))
    out_outputs = []
    for entry in notes:
        outputs = entry.get_outputs()
        out_outputs.append(outputs)
    return sum(out_outputs)


if __name__ == "__main__":
    print(get_output(get_input_list('8.txt')))
