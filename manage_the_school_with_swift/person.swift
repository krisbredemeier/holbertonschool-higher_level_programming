var str = "Hello, playground"

class Person{

    var first_name: String
    var last_name: String
    var age: Int

    init(_ first_name: String, _ last_name: String, _ age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }

    func fullName() -> String {
        return first_name + " " + last_name
    }

}

protocol Classify {
    func isStudent() -> Bool
}

class Mentor: Person, Classify {

    init(first_name: String, last_name: String, age: Int) {
        super.init(first_name, last_name, age)
    }

    func isStudent() -> Bool
    {
        return false
    }

}


class Student: Person, Classify {

    init(first_name: String, last_name: String, age: Int) {
        super.init(first_name, last_name, age)
    }

    func isStudent() -> Bool
    {
        return true
    }


}
