def draw_state(puzzle):
    print("puzzle state:")
    for row in puzzle:
            print("".join(row))

    print()


def find_blank(puzzle):
     for i in range(3):
          for j in range(3):
               if puzzle[i][j] == '0':
                    return i,j
			   
def find_tile(puzzle,tile):
     for i in range(3):
          for j in range(3):
               if puzzle[i][j] == tile:
                    return i,j
               
               
def generate_neighbors(puzzle):
     neighbors=[]
     i,j=find_blank(puzzle)
     moves = [(1,0),(-1,0),(0,1),(0,-1)]
     for di,dj in moves:
        ni,nj = i+di,j+dj
        if 0<=ni<3 and 0<=nj<3:
            new_puzzle = [row[:]for row in puzzle]
            new_puzzle[i][j],new_puzzle[ni][nj] = new_puzzle[ni][nj],new_puzzle[i][j]

            neighbors.append(new_puzzle)
     return neighbors

def manhattan(puzzle,goal):
	total_dist=0
	for i in range(3):
		for j in range(3):
			if puzzle[i][j] != '0':
				goal_i,goal_j=find_tile(goal,puzzle[i][j])
				total_dist+-abs(i-goal_i)+abs(j-goal_j)
	return total_dist
	

def hill_climb(ini,goal):
	curr=ini
	curr_c=manhattan(curr,goal)
	while True:
		neighbors=generate_neighbors(curr)
		best_n=min(neighbors,key=lambda x:manhattan(x,goal))
		best_n_cost=manhattan(best_n,goal)

		if best_n_cost>=curr_c:
			break

		curr=best_n
		curr_c=best_n_cost
	if curr==goal:
		return curr
	else:
		return None


def main():
	initial=[['1','2','3'],['4','5','0'],['7','8','6']]
	goal=[['1','2','3'],['4','5','6'],['7','8','0']]
	draw_state(initial)
	soln=hill_climb(initial,goal)

	if soln:
		print("solution found!!")
		draw_state(soln)
	else:
		print("No solution Found TT")	

if __name__=="__main__":
	main()	