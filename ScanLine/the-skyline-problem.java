/**
 The Skyline Problem
 @ Scan line + heap
 @ Note: The way to sort(handle) all edges is really important though tricky.
         1. sort first by pos is common for scan line usage
         For edges in the same pos, the following sort way can ensure the right height in this pos.
         2. start before end is mainly
 **/
class Edge {
    public int pos;
    public int height;
    public boolean isStart;
    Edge(int pos, int height, boolean isStart) {
        this.pos = pos;
        this.height = height;
        this.isStart = isStart;
    }
}

class EdgeCompartor implements Comparator<Edge> {
    public int compare(Edge o1, Edge o2) {
        // why sort like this? --> try to catch the variation correctly!
        // The sort way is really important though tricky!
        if (o1.pos == o2.pos && o1.height == o2.height && o1.isStart == o2.isStart) return 0;
        // first compare pos
        if (o2.pos != o1.pos) {
            return o1.pos > o2.pos ? 1 : -1;
        }
        // start edge always before end edge
        if (o1.isStart != o2.isStart) {
            return o2.isStart ? 1 : -1;
        }
        // for both start edge, put the larger one before
        if (o1.isStart) {
            return o2.height > o1.height ? 1 : -1;
        }
        // for both end edge, put the smaller one first
        return o2.height > o1.height ? -1 : 1;
    }
}

public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        ArrayList<int[]> results = new ArrayList<>();
        if (buildings == null) {
            return results;
        }
        // 1. construct edges & sort it
        // the sort comparator is very important!!! U must consider the situation that there are multi
        // start(end) edges in the same pos.
        ArrayList<Edge> edges = new ArrayList<>();
        for (int[] points: buildings) {
            edges.add(new Edge(points[0], points[2], true));
            edges.add(new Edge(points[1], points[2], false));
        }
        edges.sort(new EdgeCompartor());

        // 2. use heap to construct answer
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (Edge edge: edges) {
            if (edge.isStart) {
                pq.add(-edge.height);
            } else {
                pq.remove(-edge.height);

            }
            // Attention here: Pay attention to the boundary cases!
            if (pq.size() == 0) {
                results.add(new int[]{edge.pos, 0});
            } else if(results.size() == 0 || -pq.peek() != results.get(results.size() - 1)[1]) {
                results.add(new int[]{edge.pos, -pq.peek()});
            }
        }
        return results;
    }
}

