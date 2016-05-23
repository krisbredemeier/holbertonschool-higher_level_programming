// find the first longest word in a text
func longest_word(text: String) -> (String) {
my_text += " "
var word = ""
var length = 0

var max = 0
var longestWord = ""

for character in my_text.characters {
  if character == " " {
      if length > max {
          max = length
          longestWord = word
      }
      word = ""
      length = 0
  } else {
      word += "\(character)"
      length++
  }
}

return (longestWord)
}
