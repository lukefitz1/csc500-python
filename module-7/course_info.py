'''
Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The dictionary should have the following key-value pairs:

Key-Value Pairs: Room Number
Course Number (key)

Room Number (value)
CSC101    3004
CSC102    4501
CSC103    6755
NET110    1244
COM241    1411

The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. The dictionary should have the following key-value pairs:

Key-Value Pairs: Instructors
Course Number (key)

Instructor (value)
CSC101    Haynes
CSC102    Alvarado
CSC103    Rich
NET110    Burke
COM241    Lee

The program should also create a dictionary containing course numbers and the meeting times of each course. The dictionary should have the following key-value pairs:

Key-Value Pairs: Meeting Time
Course Number (key)

Meeting Time (value)
CSC101    8:00 a.m.
CSC102    9:00 a.m.
CSC103    10:00 a.m.
NET110    11:00 a.m.
COM241    1:00 p.m.

The program should let the user enter a course number and then it should display the course's room number, instructor, and meeting time.
'''

room_numbers = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
meeting_times = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.", "NET110": "11:00 a.m.", "COM241": "1:00 p.m."}

print('Enter a course number: ', end = '')
course_number = str(input())

print('Room number: ', room_numbers[course_number])
print('Instructor: ', instructors[course_number])
print('Meeting time: ', meeting_times[course_number])