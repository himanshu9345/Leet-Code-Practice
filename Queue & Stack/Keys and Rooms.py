rooms=[[1,3],[3,0,1],[2],[0]]
def dfs(rooms,seen,curr_room):
    if curr_room not in seen:
        seen.add(curr_room)
        for room in rooms[curr_room]:
            dfs(rooms,seen,room)

def canVisitAllRooms(rooms):
    total_rooms=len(rooms)
    seen=set()
    dfs(rooms,seen,curr_room=0)
    for i in range(total_rooms):
        if i not in seen:
            return False
    return True
print(canVisitAllRooms(rooms))