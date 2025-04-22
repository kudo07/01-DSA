var containsNearbyDuplicate = function(nums, k) {
    found={}
    for(let i=0;i<nums.length;i++){
        if(nums[i] in found && i-found[nums[i]]<=k){
            return true
        }
        found[nums[i]]=i
    }
    return false
    
};