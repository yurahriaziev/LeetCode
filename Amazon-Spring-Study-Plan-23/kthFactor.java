// first solution
class kthFactor {
    public int kthFactor(int n, int k) {
        int counter = 0;
        ArrayList<Integer> factors = new ArrayList<Integer>();
        while (counter < n) {
            counter++;
            if (n % counter == 0) {
                factors.add(counter);
            }
            if (factors.size() == k) {
                return factors.get(k-1);
            }
        }
        return -1;
    }
}

// second solution
class Solution {
    public int kthFactor(int n, int k) {
        int counter = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                counter++;
            }
            if (counter == k) {
                return i;
            }
        }
        return -1;
    }
}