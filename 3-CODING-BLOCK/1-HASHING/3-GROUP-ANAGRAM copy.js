//  tc:o(n*klogk)
// let a = 'ef';
// let b = a.split();
// console.log(b);
var groupAnagrams = function (strs) {
  ans = [];
  mp = new Map();
  for (let i of strs) {
    sorted_str = i.split('').sort().join('');
    if (mp.has(sorted_str)) {
      ans[mp.get(sorted_str)].push(i);
    } else {
      mp.set(sorted_str, ans.length);
      ans.push([i]);
    }
  }
  return ans;
};
