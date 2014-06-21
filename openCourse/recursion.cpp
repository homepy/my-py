bool Solve(configuration conf)
{
	if (no more choices)
		return (conf is goal state);

	for (all available choices) {
		try one choice c;
		// solve form here, it works out. you're done
		if (Solve(conf with choice c made))
			return true;
		else 
			unmake choice c
	}
	return false;
}



bool SolveSoduKu(Grid<int> &grid){
	if ()

	for now = ? {
		try now=....
	if(SolveSudoKu(grid))
		return true
	else
		
}

}
