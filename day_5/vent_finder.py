from utils import get_input_list


class LineTypes:
    """
        Static class that contains the different kinds of lines
    """

    VERTICAL = 0
    HORIZONTAL = 1
    DIAGONAL = 2
    POINT = 3


class LineSegment:
    # noinspection GrazieInspection
    """
            A class that represents a line segment

            :ivar x1: The x position of the first point
            :type x1: int
            :ivar x2: The x position of the second point
            :type x2: int
            :ivar y1: The y position of the first point
            :type y1: int
            :ivar y2: The y position of the second point
            :type y2: int
            :ivar type: The type of line (VERTICAL, HORIZONTAL, DIAGONAL, POINT)
            :type type: int
            :ivar slope: If this is a diagonal line, the slope of the line
            :type slope: float
            :ivar intercept: If this is a diagonal line, the y-intercept of the line
            :type intercept: float
    """

    def __init__(self, raw_line: str):
        """
            Instantiates a new line segment

            :param raw_line: The raw line in the format "x1,y1 -> x2,y2"
            :type raw_line: str
        """

        split_line = raw_line.split(" ")
        points = [[int(x) for x in split_line[0].split(",")], [int(x) for x in split_line[2].split(",")]]
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        if self.x1 == self.x2 and self.y1 == self.y2:
            self.type = LineTypes.POINT
        elif self.x1 == self.x2:
            self.type = LineTypes.VERTICAL
        elif self.y1 == self.y2:
            self.type = LineTypes.HORIZONTAL
        else:
            self.slope = (self.x2 - self.x1) / (self.y2 - self.y1)
            self.intercept = self.y2 - (self.slope * self.x2)
            self.type = LineTypes.DIAGONAL

    def in_line(self, point: list[int]) -> bool:
        """
            Determines if a point is in this line

            :param point: The point to check
            :type point: list[int]
            :returns: Whether the point is in the line
            :rtype: bool
        """

        if self.type == LineTypes.POINT:
            return point[0] == self.x1 and point[1] == self.y2
        elif self.type == LineTypes.HORIZONTAL:
            return point[1] == self.y1 and (self.x1 <= point[0] <= self.x2 or self.x2 <= point[0] <= self.x1)
        elif self.type == LineTypes.VERTICAL:
            return point[0] == self.x1 and (self.y1 <= point[1] <= self.y2 or self.y2 <= point[1] <= self.y1)
        elif self.type == LineTypes.DIAGONAL:
            if (self.x1 <= point[0] <= self.x2) or (self.x2 <= point[0] <= self.x1):
                return point[1] == point[0] * self.slope + self.intercept
            else:
                return False
        else:
            raise ValueError("Invalid Line Type!")


def find_dangerous_intersections(raw_lines: list[str], min_intersects: int = 2) -> int:
    """
        Find dangerous intersections given a bunch of lines

        :param raw_lines: The lines as raw strings
        :type raw_lines: list[str]
        :param min_intersects: The number of lines the point has to be on to be considered dangerous
        :type min_intersects: int
        :returns: The number of dangerous points
        :rtype: int
    """

    lines = []
    for raw_line in raw_lines:
        lines.append(LineSegment(raw_line))
    dangerous_intersections = 0
    for y in range(1000):
        for x in range(1000):
            intersect_count = 0
            for line in lines:
                if line.in_line((x, y)):
                    intersect_count += 1
            if intersect_count >= min_intersects:
                dangerous_intersections += 1
    return dangerous_intersections


if __name__ == "__main__":
    raw_input = get_input_list("5.txt")
    print("Danger Zones:", find_dangerous_intersections(raw_input))
