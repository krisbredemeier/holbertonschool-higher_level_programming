func divides(a: Int, _ b: Int) -> Bool {
    return a % b == 0
}

func countDivisors(number: Int) -> Int {
    var cnt = 0
    for i in 1...number {
        if divides(number, i) {
            ++cnt
        }
    }
    return cnt
}

func is_prime(number: Int) -> (Bool) {
  return countDivisors(number) == 2
}
