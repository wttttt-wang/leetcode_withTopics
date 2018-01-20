/**
 * LFU Cache
 * @ Design + Hash: Usage of 'LinkedHashSet'
 */
class LFUCache {
    int cap;
    HashMap<Integer, Integer> cnts;   // map key to occur cnt
    HashMap<Integer, LinkedHashSet<Integer>> lists;  // map cnt to an linkedHashSet of keys
    HashMap<Integer, Integer> vals;   // map key to value
    int minCnt = 0;   // for evict when reaches capacity, remember to update
    public LFUCache(int capacity) {
        cap = capacity;
        cnts = new HashMap<>();
        lists = new HashMap<>();
        vals = new HashMap<>();
    }

    public int get(int key) {
        if (!vals.containsKey(key)) {
            return -1;
        }
        // 1. update cnts
        int cnt = cnts.get(key);
        cnts.put(key, cnt + 1);
        // 2. update lists
        lists.get(cnt).remove(key);
        // 3. update minCnt
        if (cnt == minCnt && lists.get(cnt).size() == 0) minCnt++;
        if (!lists.containsKey(cnt + 1)) {
            lists.put(cnt + 1, new LinkedHashSet<>());
        }
        lists.get(cnt + 1).add(key);
        return vals.get(key);
    }

    public void put(int key, int value) {
        if (cap <= 0) return;
        if (vals.containsKey(key)) {
            vals.put(key, value);
            get(key);  // tricky
            return;
        }
        // if reach capacity
        if (vals.size() >= cap) {
            int evit = lists.get(minCnt).iterator().next();
            lists.get(minCnt).remove(evit);
            vals.remove(evit);
        }
        vals.put(key, value);
        cnts.put(key, 1);
        minCnt = 1;
        if (!lists.containsKey(1)) {
            lists.put(1, new LinkedHashSet<>());
        }
        lists.get(1).add(key);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */