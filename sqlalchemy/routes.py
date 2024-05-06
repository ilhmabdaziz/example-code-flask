from flask import request, jsonify

from models import Employees, Salaries,Dept_emp

def routes_employees(app, db):
    @app.route('/employees/', methods=['GET'])
    def get_employees():
        try:
            page = request.args.get('page', 1, type=int)  
            per_page = request.args.get('per_page', 5, type=int)  

            employees_paginated = Employees.query.paginate(page=page, per_page=per_page)
            print(employees_paginated.items)
            
            arr_employees_data = []

            for employee in employees_paginated.items:
                print(employee.emp_no)
                salary = Salaries.query.filter_by(emp_no=employee.emp_no).first()

                if salary is not None:
                    salary_data = {
                        'salary': salary.salary if salary else None,
                        'from_date': str(salary.from_date) if salary else None,
                        'to_date': str(salary.to_date) if salary else None
                    }
                else:
                    salary_data = {}
                
                employee_data = {
                    'emp_no': employee.emp_no,
                    'first_name': employee.first_name,
                    'last_name': employee.last_name,
                    'birth_date': str(employee.birth_date),
                    'gender': employee.gender,
                    'hire_date': str(employee.hire_date),
                    'salary': salary_data  
                }

                arr_employees_data.append(employee_data)
            
            pagination = {
                'total_pages': employees_paginated.pages,
                'total_items': employees_paginated.total,
                'current_page': employees_paginated.page,
                'items_per_page': employees_paginated.per_page,
                'has_next': employees_paginated.has_next,
                'has_prev': employees_paginated.has_prev,
                'next_page': employees_paginated.next_num if employees_paginated.has_next else None,
                'prev_page': employees_paginated.prev_num if employees_paginated.has_prev else None
            }

            return jsonify({"message": "successfully", 'data': arr_employees_data, 'pagination': pagination, "error": 0}),200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
def search_employee(app,db):
    @app.route('/employees/search/', methods=['GET'])
    def get_by_search_employee():
        try:
            search_query = request.args.get('q', None)  

            base_query = Employees.query

            if search_query:
                base_query = base_query.filter((Employees.first_name.like(f"%{search_query}%")) | (Employees.last_name.like(f"%{search_query}%")))

            search_results = base_query.all()

            arr_employees_data = []

            for employee in search_results:
                salary = Salaries.query.filter_by(emp_no=employee.emp_no).first()

                if salary is not None:
                    salary_data = {
                        'salary': salary.salary if salary else None,
                        'from_date': str(salary.from_date) if salary else None,
                        'to_date': str(salary.to_date) if salary else None
                    }
                else:
                    salary_data = {}

                employee_data = {
                    'emp_no': employee.emp_no,
                    'first_name': employee.first_name,
                    'last_name': employee.last_name,
                    'birth_date': str(employee.birth_date),
                    'gender': employee.gender,
                    'hire_date': str(employee.hire_date),
                    'salary': salary_data  
                }

                arr_employees_data.append(employee_data)

            return jsonify({"message": "successfully", 'data': arr_employees_data, "error": 0}),200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
def update_data(app,db):
    @app.route('/employees/<int:emp_no>', methods=['PUT'])
    def update_employee(emp_no):
        try:
            print(request.json)
            employee = Employees.query.get_or_404(emp_no)

            if 'first_name' in request.json:
                employee.first_name = request.json['first_name']
            if 'last_name' in request.json:
                employee.last_name = request.json['last_name']
            if 'birth_date' in request.json:
                employee.birth_date = request.json['birth_date']
            if 'gender' in request.json:
                employee.gender = request.json['gender']
            if 'hire_date' in request.json:
                employee.hire_date = request.json['hire_date']

            if 'salary' in request.json:
                salary_data = request.json['salary']
                salary = Salaries.query.filter_by(emp_no=emp_no).first()
                if salary:
                    salary.salary = salary_data['salary']
                    salary.from_date = salary_data['from_date']
                    salary.to_date = salary_data['to_date']
                else:
                    # if not exist on salary table, create new row
                    salary = Salaries(emp_no=emp_no,
                                    salary=salary_data['salary'],
                                    from_date=salary_data['from_date'],
                                    to_date=salary_data['to_date'])
                    db.session.add(salary)

            if 'department' in request.json:
                department_data = request.json['department']
                dept_emp = Dept_emp.query.filter_by(emp_no=emp_no).first()
                if dept_emp:
                    dept_emp.dept_no = department_data['dept_no']
                    dept_emp.from_date = department_data['from_date']
                    dept_emp.to_date = department_data['to_date']
                else:
                    # Create a new department record if it doesn't exist
                    dept_emp = Dept_emp(emp_no=emp_no,
                                        dept_no=department_data['dept_no'],
                                        from_date=department_data['from_date'],
                                        to_date=department_data['to_date'])
                    db.session.add(dept_emp)

            db.session.commit()

            employee_data = {
                'emp_no': employee.emp_no,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'birth_date': str(employee.birth_date),
                'gender': employee.gender,
                'hire_date': str(employee.hire_date)
            }

            return jsonify({'message': 'Employee data updated successfully', 'employee': employee_data}),200
        except Exception as e:
            return jsonify({'error': str(e)}), 500