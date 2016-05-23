//  compute the Fibonacci number
func fibonacci(number: Int) -> Int {
    if number <= 2 {
        return 1
    } else {
        return fibonacci(number - 1) + fibonacci(number - 2)
    }
}
