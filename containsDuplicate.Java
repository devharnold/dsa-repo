class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        // loop through with the specific integer n
        for (int n : nums) {
            // if the set contains the number return true : add the number to the set
            if (set.contains(n)) {
                return true;
            }
            set.add(n);
        }
        // no duplicates
        return false;
    }
}