// find the max number of an array of integer
// without using a function, but a closure
var numbers = [4, 7, 1, 9, 6, 5, 6, 9]

let max = numbers.reduce(numbers[0]) {
    if $0 > $1 {
        return $0
    } else {
        return $1
    }
}

print(max)
