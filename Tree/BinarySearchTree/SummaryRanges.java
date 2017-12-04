/**
 * Data Stream as Disjoint Intervals
 * @ Explanation: Very simple and typical BST problem. Each node contains an interval, intervals between nodes are disjoint.
 */
class SummaryRanges {
    TreeSet<Interval> treeSet;

    /** Initialize your data structure here. */
    public SummaryRanges() {
        treeSet = new TreeSet<>(new Comparator<Interval>() {
            @Override
            public int compare(Interval o1, Interval o2) {
                if (o1.start == o2.start) {
                    if (o1.end == o2.end) return 0;
                    return o1.end > o2.end ? 1 : -1;
                }
                return o1.start > o2.start ? 1 : -1;
            }
        });
    }

    public void addNum(int val) {
        Interval interval = new Interval(val, val);
        Interval ceil = treeSet.ceiling(interval);
        Interval floor = treeSet.floor(interval);
        int start = val;
        int end = val;
        if (floor != null) {
            if (floor.end == val - 1) {
                treeSet.remove(floor);
                start = floor.start;
            }
            else if (val <= floor.end) return;
        }
        if (ceil != null) {
            if (ceil.start == val + 1) {
                treeSet.remove(ceil);
                end = ceil.end;
            }
            else if (val >= ceil.start) return;
        }
        treeSet.add(new Interval(start, end));
    }

    public List<Interval> getIntervals() {
        return new ArrayList<Interval>(treeSet);
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */