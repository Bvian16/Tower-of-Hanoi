def TowerOfHanoi(n , first_rod, last_rod, aux_rod): 
	if n == 1: 
		print("Move disk 1 from rod",first_rod,"to rod",last_rod)
		return
	TowerOfHanoi(n-1, first_rod, aux_rod, last_rod) 
	print("Move disk",n,"from rod",first_rod,"to rod",last_rod) 
	TowerOfHanoi(n-1, aux_rod, last_rod, first_rod) 
		
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')