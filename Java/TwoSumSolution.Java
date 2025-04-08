import java.util.*;

class TwoSumSolution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> prevMap = new HashMap<>(); // value-index

        for(int i = 0; i < nums.length; i++) { // iterate
            int diff = target - nums[i]; // find the difference
            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }
            prevMap.put(nums[i], i)
        }
        return new int[] {}; //java's version of python list return
    }
}

/**
 * Map: is an interface in java representing a collection of key-value pairs
 * Integer, Integer: specifies the types
 *  The Key is an Integer
 *  The Value is an Integer
 * 
 * prevMap is the variable name I'm assining the map
 * 
 *  = new HashMap<>();
 * new creates an object
 * HashMap<> is a class that implements the Map interface - it stores key-value pairs with fast-access
 * The <> uses 
 */