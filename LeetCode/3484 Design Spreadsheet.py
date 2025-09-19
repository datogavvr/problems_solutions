class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = {chr(i): [0 for j in range(rows)] for i in range(65, 91)}

    def getCell(self, cell: str) -> int:
        return self.spreadsheet[cell[0]][int(cell[1:])-1]

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell[0]][int(cell[1:])-1] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell[0]][int(cell[1:])-1] = 0

    def getValue(self, formula: str) -> int:
        a, b = map(str, formula[1:].split('+'))
        if not a.isdigit():
            a = self.getCell(a)
        if not b.isdigit():
            b = self.getCell(b)
        return int(a)+int(b)
