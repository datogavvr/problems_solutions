class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        for i in range(len(version1)-1, 0, -1):
            if version1[i] == 0:
                version1.pop(-1)
            else:
                break
        for i in range(len(version2)-1, 0, -1):
            if version2[i] == 0:
                version2.pop(-1)
            else:
                break
        l = min(len(version1), len(version2))
        for i in range(l):
            if version1[i] > version2[i]:
                return 1
            elif version2[i] > version1[i]:
                return -1
        if len(version1) > len(version2):
            return 1
        elif len(version1) < len(version2):
            return -1
        else:
            return 0