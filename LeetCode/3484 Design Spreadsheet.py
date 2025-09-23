class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = {chr(i): {} for i in range(65, 91)}

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell[0]][int(cell[1:])] = value

    def resetCell(self, cell: str) -> None:
        if int(cell[1:]) in self.spreadsheet[cell[0]]:
            del self.spreadsheet[cell[0]][int(cell[1:])]

    def getValue(self, formula: str) -> int:
        a, b = map(str, formula[1:].split('+'))
        if not a.isdigit():
            if int(a[1:]) in self.spreadsheet[a[0]]:
                a = self.spreadsheet[a[0]][int(a[1:])]
            else:
                a = 0
        if not b.isdigit():
            if int(b[1:]) in self.spreadsheet[b[0]]:
                b = self.spreadsheet[b[0]][int(b[1:])]
            else:
                b = 0
        return int(a)+int(b)
