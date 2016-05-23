
func is_palindrome(s: String) -> (Bool) {
  let sArr = Array( s.characters )
  for var i = 0, j = sArr.count - 1; i < j; i += 1, j -= 1 {
    if sArr[ i ] != sArr[ j ] {
      return false
    }
  }
    return true
}
