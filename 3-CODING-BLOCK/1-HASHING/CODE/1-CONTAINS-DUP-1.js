const duplicate = (nums) => {
  let x = {};
  for (let i = 0; i < nums.length; i++) {
    if (x[nums[i]]) {
      return true;
    } else {
      x[nums[i]] = true;
    }
  }

  return false;
};

nums = [1, 2, 3, 4];
console.log(duplicate(nums));
