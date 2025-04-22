/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let ans = 0;
  let mp = {};
  let j = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] in mp) {
      j = Math.max(j, mp[s[i]] + 1);
    }
    mp[s[i]] = i;
    ans = Math.max(ans, i - j + 1);
  }
  return ans;
};
