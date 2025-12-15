package containsdupl


func containsDuplicate(nums []int) bool {
	var prevNums = make(map[int]bool) // or do this instead prevNums := make(map[int]bool), but we want clarity

	for _, i := range nums {
		if prevNums[i] {
			return true
		}
		prevNums[i] = true
	}

	return false
}

// remember prevNums cant be used at package scope
// var prevNums is mostly preferred