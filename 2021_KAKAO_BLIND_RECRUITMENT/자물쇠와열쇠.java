class Solution {
	static int n, m, lockCnt, board[][];
	static boolean isBoard[][];
    static public boolean solution(int[][] key, int[][] lock) {
    	n = key.length;
    	m = lock.length;
    	int size = m + 2*(n-1);
    	board = new int[size][size];
    	isBoard = new boolean[size][size];
    	// 시작점 n-1, n-1
    	for(int i = 0; i < m; i++) {
    		for(int j = 0; j < m; j++) {
    			board[n-1+i][n-1+j] = lock[i][j];
    			if(lock[i][j]==0) lockCnt++;
    			isBoard[n-1+i][n-1+j] = true;
    		}
    	}
    	for(int i = 0; i <= m + n - 2; i++) {
    		for(int j = 0; j <= m + n - 2; j++) {
    			for(int k = 0; k < 4; k++) {
    				if (check(i, j, key)) return true;
    				rotate(key);
    			}
    		}
    	}
    	return false;
    }
    static void print(int[][] arr) {
    	for(int i = 0; i < n; i++) {
    		for(int j = 0; j < n; j++) {
    			System.out.printf("%d ", arr[i][j]);
    		}
    		System.out.println();
    	}
    	System.out.println();
    }
    static boolean check(int x, int y, int[][] key) {
    	int pairCnt = 0;
    	for(int i = 0; i < n; i++) {
    		for(int j = 0; j < n; j++) {
    			if(!isBoard[x+i][y+j]) continue;
    			if(board[x+i][y+j]==0 && key[i][j]==1) pairCnt++;
    			if(board[x+i][y+j] == key[i][j]) return false;
    		}
    	}
    	if(pairCnt == lockCnt) return true;
    	return false;
    }
    static void rotate(int[][] key) {
    	int[][] temp = new int[n][n];
    	for(int i = 0; i < n; i++) {
    		for(int j = 0; j < n; j++) {
    			temp[i][j] = key[n-j-1][i];
    		}
    	}
    	for(int i = 0; i < n; i++) {
    		for(int j = 0; j < n; j++) {
    			key[i][j] = temp[i][j];
    		}
    	}
    }
    
}
