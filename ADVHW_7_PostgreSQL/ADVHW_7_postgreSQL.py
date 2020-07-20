import psycopg2 as pg
from datetime import datetime
from psycopg2 import sql
from pprint import pprint


class Pgconnect:

    def __init__(self, database_name, user, password, host, port):
        self.conn = pg.connect(database=f'{database_name}', user=f'{user}', password=f'{password}', host=f'{host}',
                               port=f'{port}')

    def db_params_string(self, params: dict):
        request_string = []
        for key, value in params.items():
            column = '%s %s' %(key, value,)
            request_string.append(column)
        request_string = ', '.join(request_string)
        return request_string

    def create_db(self, table_name, table_params: dict):
        with self.conn.cursor() as cur:
            params = self.db_params_string(table_params)
            s_string = ['%s' for i in range (len(params.split(',')))]
            s_string = ', '.join(s_string)
            params = params.split(',')
            params = [i.strip() for i in params]
            params = ', '.join(params)
            request = f'CREATE TABLE %s (%s);' %('{}', params)
            cur.execute(sql.SQL(request).format(sql.Identifier(table_name)))
            self.conn.commit()
        return True

    def drop_table(self):
        cur = self.conn.cursor()
        res = cur.execute('DROP TABLE student_course;')
        self.conn.commit()
        return res

    def add_student(self, student: tuple):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO students(name, gpa, birth) values (%s,%s,%s);', (student))
            self.conn.commit()
            return True

    def add_course(self, course):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO courses(name) VALUES (%s);', [course])
            self.conn.commit()
            return True

    def get_student(self, id):
        cur = self.conn.cursor()
        cur.execute('SELECT name FROM students WHERE id = %s;', ([id]))
        res = cur.fetchall()
        return res

    def get_student_id(self, name):
        cur = self.conn.cursor()
        cur.execute('SELECT id FROM students WHERE name = %s;', ([name]))
        res = cur.fetchall()
        return res

    def check(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public';""")
        res = cur.fetchall()
        print('---- TABLES ----')
        print(res)
        cur.execute('SELECT * FROM students;')
        res2 = cur.fetchall()
        print('---- STUDENTS ----')
        for i in res2:
            print(i)
        print('---- COURSES ----')
        cur.execute('SELECT * FROM courses;')
        res3 = cur.fetchall()
        for i in res3:
            print(i)
        print('---- STUDENT-COURSE ----')
        cur.execute('SELECT * FROM student_course;')
        res3 = cur.fetchall()
        for i in res3:
            print(i)

    def student_course_relation(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE student_course
        (
        id serial PRIMARY KEY,
        student_id INTEGER REFERENCES students(id),
        course_id INTEGER REFERENCES courses(id)
        )
        """)
        self.conn.commit()

    def add_student_to_course(self, student_id, course_id):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO student_course(student_id, course_id) VALUES (%s, %s);', [student_id, course_id])
            self.conn.commit()
            return True

    def get_students(self, course_id):  # возвращает студентов определенного курса
        cur = self.conn.cursor()
        # Здесь должно быть WHERE sc.course_id = %s, я не понимаю, как заставить его работать
        request = '''SELECT s.name, c.name FROM student_course as sc JOIN students as s ON sc.student_id = s.id JOIN courses as c ON sc.course_id = c.id
        ;'''
        cur.execute(request, ([course_id]))
        res = cur.fetchall()
        return res

    def add_students(self, course_id, students):  # создает студентов и записывает их на курс
        for key, value in students.items():
            student_to_add = [key]
            for i in value:
                student_to_add.append(i)
            self.add_student(student_to_add)
        to_course = []
        for key in students.keys():
            to_course.append(base.get_student_id(key))
        print(to_course)
        to_course_clear = []
        for i in to_course:
            for id in i:
                for num in id:
                    to_course_clear.append(num)
        print(to_course_clear)
        for i in to_course_clear:
            self.add_student_to_course(i,course_id)
        return True

if __name__ == '__main__':
    base = Pgconnect(database_name='bogdanov', user='bogdanov', password='bogdanov', host='pg.codecontrol.ru', port=59432)
    base.check()
    print('--- JOINS ---')
    pprint(base.get_students(1))


# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# student_table = {'id': 'serial PRIMARY KEY', 'name': 'character varying(100) not null', 'gpa': 'numeric(10,2)',
#                  'birth': 'timestamp with time zone'}
# base.create_db('students', student_table)
# alex = ('Alex', 4.58, datetime.now())
# base.add_student(alex)
# john = ('John', 3.58, datetime.now())
# base.add_student(john)
# mary = ('Mary', 5.45, datetime.now())
# base.add_student(mary)
# base.drop_table()
# print(base.get_student(2))
# course_table = {'id': 'serial PRIMARY KEY', 'name': 'character varying(100) not null'}
# base.create_db('courses', course_table)
# base.add_course('python')
# base.add_course('java')
# base.add_course('sql')
# base.student_course_relation()
# base.add_student_to_course(1, 2)
# base.add_student_to_course(2, 2)
# base.add_student_to_course(3, 1)
# pprint(base.get_students(1))