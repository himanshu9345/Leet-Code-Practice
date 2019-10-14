def queensAttacktheKing( queens, king):
    ans = []
    seen = set()

    for k in queens:
        seen.add((k[0], k[1]))
    seen1 = set()
    r, c = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    startx, stary = king[0], king[1]
    arr = [king] * 8
    # print(arr)
    for j in range(7):
        for i in range(8):
            if i not in seen1:
                # print(arr[i][0])
                x, y = arr[i][0] + r[i], arr[i][1] + c[i]
                if 0 <= x < 8 and 0 <= y < 8:
                    if (x, y) in seen:
                        ans.append([x, y])
                        seen1.add(i)
                arr[i] = [x, y]
    return ans

# queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
# king = [0,0]
# queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
# king = [3,3]
queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]

print(queensAttacktheKing(queens,king))