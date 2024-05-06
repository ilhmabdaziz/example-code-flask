from app import db

class Employees(db.Model):
    __tablename__ = 'employees'
    emp_no = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum('M', 'F'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    salaries = db.relationship('Salaries', backref='employee', lazy=True)
    departments = db.relationship('Dept_emp', backref='employee', lazy=True)
    
    def __init__(self, birth_date, first_name, last_name, gender, hire_date):
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hire_date = hire_date

    def __repr__(self):
        return '<Employees %r>' % self.first_name
    
class Salaries(db.Model):
    __tablename__ = 'salaries'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True)
    salary = db.Column(db.Integer, nullable=False)
    from_date = db.Column(db.Date, primary_key=True)
    to_date = db.Column(db.Date, nullable=False)
    
    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to_date = to_date

    def __repr__(self):
        return '<Salaries %r>' % self.salary
    
class Dept_emp(db.Model):
    __tablename__ = 'dept_emp'
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True)
    dept_no = db.Column(db.String(20), db.ForeignKey('departments.dept_no'), primary_key=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    def __init__(self, emp_no, dept_no, from_date, to_date):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to_date = to_date

    def __repr__(self):
        return '<Dept_emp %r>' % self.dept_no
    

class Departments(db.Model):
    __tablename__ = 'departments'
    dept_no = db.Column(db.String(20), primary_key=True)
    dept_name = db.Column(db.String(255), nullable=False)

    def __init__(self, dept_no, dept_name):
        self.dept_no = dept_no
        self.dept_name = dept_name

    def __repr__(self):
        return '<Department %r>' % self.dept_name