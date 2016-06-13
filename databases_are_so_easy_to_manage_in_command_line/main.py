import peewee
import sys
from models import *


''' create_it function '''
def main():
    my_models_db.connect()
    if len (sys.argv) < 2:
        print "Please enter an action"

    actions = (
        "create",
        "print",
        "insert",
        "delete"
    )

def create_it():
    try:
        my_models_db.create_tables([School, Batch, User, Student], safe=True)
    except peewee.OperationalError:
        pass

''' print_it function '''
def print_it():
    if len(sys.argv) < 3:
        pass
        print "needs one more argument"
    else:
        if sys.argv[2] == "school":
            for school in School.select():
                print school
        elif sys.argv[2] == "batch":
            for batch in Batch.select():
                print batch
        elif sys.argv[2] == "user":
            for users in Users.select():
                print "User: %s %s (%d)" %(users.first_name, users.last_name, users.id)
        elif sys.argv[2] == "student":
            for student in Student.select():
                print student,
                # print Batch.get(school_id = 1)
        else:
            print "Undefined action", str(sys.argv[2])

''' insert_it function '''
def insert_it():
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            School.create(name = sys.argv[3])
            print "New School: "
            print School.get(name = sys.argv[3])
        elif sys.argv[2] == "batch":
            Batch.create(school_id = sys.argv[3], name = sys.argv[4])
            print "New Batch: ",
            print Batch.get(school_id = sys.argv[3])
        elif sys.argv[2] == "user":
            User.create(first_name = sys.argv[3], last_name = sys.argv[4], age = sys.argv[5])
            print "New User: User: %s %s (%d)" %(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == "student":
            if len(sys.argv) <=6:
                Student.create(batch_id = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5])
                print ("New Student:"),
                print Student.get(last_name = sys.argv[5])
            else:
                Student.create(batch_id = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5], first_name = sys.argv[6])
                print ("New Student:"),
                print Student.get(first_name = sys.argv[6])
        else:
            print "Undefined action", str(sys.argv[2])


''' delete_it function '''
def delete_it():
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            School.delete(id = sys.argv[3])
        elif sys.argv[2] == "batch":
            Batch.delete(id = sys.argv[3])
        elif sys.argv[2] == "user":
            ''' user '''
        elif sys.argv[2] == "student":
            student = Student.get(Student.id == sys.argv[3])
            print"Delete:",
            print student
            student.delete_instance()
        else:
            print "Undefined action", str(sys.argve[2])

if len(sys.argv) < 2:
    print "please enter an action"
else:
    if sys.argv[1] == "create":
        create_it()
    elif sys.argv[1] == "print":
        print_it()
    elif sys.argv[1] == "insert":
        insert_it()
    elif sys.argv[1] == "delete":
        delete_it()
    else:
        print "Undefined action", str(sys.argv[1])
