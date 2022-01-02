import requests

base_url = 'http://127.0.0.1:8000/api/'

username = 'anurag'
password = '12345'

# retrieve all courses 
r = requests.get(f'{base_url}courses/')
courses = r.json()
available_courses =  ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll_course/', auth=(username, password))
    print(r.json())

    if r.status_code == 200:
        # successful request
        print(f'Successfully enrolled in {course_title}')