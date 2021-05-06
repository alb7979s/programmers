class Solution {
	static final int INF = (int)1e8;
    public int solution(int n, int s, int a, int b, int[][] fares) {
    	int[][] dist = new int[n][n];
    	for(int i = 0; i < n ; i++) {
    		for(int j = 0; j < n; j++) {
    			if(i==j) dist[i][j] = 0;
    			else dist[i][j] = INF;
    		}
    	}
    	s--;a--;b--;
    	for (int[] fare: fares) {
    		int u = fare[0] - 1;
    		int v = fare[1] - 1;
    		int w = fare[2];
    		dist[u][v] = min(dist[u][v], w);
    		dist[v][u] = min(dist[v][u], w);
    	}
    	for(int k = 0; k < n; k++) {
    		for(int i = 0; i < n; i++) {
    			for(int j = 0; j < n; j++){
    				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
    			}
    		}
    	}
    	int res = dist[s][a] + dist[s][b];
    	for(int i = 0; i < n; i++) {
    		res = min(res, dist[s][i] + dist[i][a] + dist[i][b]);
    	}
    	return res;
    }
    static int min(int a, int b) {
    	return a < b ? a : b;
    }
}
