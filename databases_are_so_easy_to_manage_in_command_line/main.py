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
        "print_batch_by_school"
        "print_student_by_batch",
        "print_student_by_school",
        "print_family",
        "age_average",
        "change_batch",
        "print_all",
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
                # print ("\n")
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
            print "New School:", School.get(name = sys.argv[3])
        elif sys.argv[2] == "batch":
            Batch.create(school_id = sys.argv[3], name = sys.argv[4])
            print "New Batch:", Batch.get(school_id = sys.argv[3])
        elif sys.argv[2] == "user":
            User.create(first_name = sys.argv[3], last_name = sys.argv[4], age = sys.argv[5])
            print "New User: User: %s %s (%d)" %(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == "student":
            if len(sys.argv) <=6:
                Student.create(batch_id = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5])
                print "New Student:", Student.get(last_name = sys.argv[5])
            else:
                Student.create(batch_id = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5], first_name = sys.argv[6])
                print "New Student:", Student.get(first_name = sys.argv[6])
        else:
            print "Undefined action", str(sys.argv[2])


''' delete_it function '''
def delete_it():
    if len(sys.argv) < 3:
        pass
    else:
        if sys.argv[2] == "school":
            school = School.get(id = sys.argv[3])
            print "deleting", school
            school.delete_instance()
        elif sys.argv[2] == "batch":
            batch = Batch.get(id = sys.argv[3])
            print "deleting", batch
            batch.delete_instance()
        elif sys.argv[2] == "user":
            ''' user '''
        elif sys.argv[2] == "student":
            try:
                student = Student.get(Student.id == sys.argv[3])
                print "Delete:", student
                student.delete_instance()
            except:
                print "Nothing to delete"
        else:
            print "Undefined action", str(sys.argve[2])

def print_batch_by_school():
    try:
        print Batch.get(id = sys.argv[2])
    except:
        print "School not found"

def print_student_by_school():
    try:
        Batch.get(school_id = sys.argv[2])
        for student in Student.select().join(Batch).where(Batch.school_id == sys.argv[2]):
            print student
    except:
        print "School not found"

def print_student_by_batch():
    try:
        Student.get(batch_id = sys.argv[2])
        for student in Student.select().where(Student.batch_id == sys.argv[2]):
            print student
    except:
        print "Batch not found"

def print_family():
    try:
        for student in Student:
            if (student.last_name == sys.argv[2]):
                print student
    except:
        print "Last name not found"

def age_average():
    age_avg = 0
    i = 0
    for student in Student:
        age_avg = age_avg + student.age
        i += 1
    print age_avg/i

# def print_all():

def change_batch():
    try:
        x = Student.get(Student.id == sys.argv[2])
        y = Batch.get(Batch.id == sys.argv[3])
    except Student.DoesNotExist:
        print "Studnt not found"
    except Batch.DoesNotExist:
        print "Batch not found"

    if Student.select().where(Student.id == sys.argv[2], Student.batch == sys.argv[3]).exists():
        print "%s already in %s" % (x, y)

    print "%s has been moved to %s" % (x, y)
    print x
    # a.batch = sys.argv[3]
    # a.save()

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
    elif sys.argv [1] == "print_batch_by_school":
        print_batch_by_school()
    elif sys.argv[1] == "print_student_by_batch":
        print_student_by_batch()
    elif sys.argv[1] == "print_family":
        print_family()
    elif sys.argv[1] == "age_average":
        age_average()
    elif sys.argv[1] == "print_all":
        print_all()
    elif sys.argv[1] == "print_student_by_school":
        print_student_by_school()
    elif sys.argv[1] == "change_batch":
        change_batch()
    else:
        print "Undefined action", str(sys.argv[1])
