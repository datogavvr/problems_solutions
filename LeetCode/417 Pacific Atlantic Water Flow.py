class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pac = set()
        atl = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def up(r, c, visited, prev_height):
            if (r < 0 or r >= n or c < 0 or c >= m or
                    (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in directions:
                up(r + dr, c + dc, visited, heights[r][c])

        for c in range(m):
            up(0, c, pac, heights[0][c])
            up(n - 1, c, atl, heights[n - 1][c])
        for r in range(n):
            up(r, 0, pac, heights[r][0])
            up(r, m - 1, atl, heights[r][m - 1])

        result = [[r, c] for (r, c) in pac & atl]
        return result
