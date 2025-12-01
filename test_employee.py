from employee import employee_info
def test_employee_info():
    expected_output=(
      "name" = "Rahul\n"
      "emp_id" = "EMP1024\n"
      "department" = "Finance\n"
      "salary" = 45000
       )
  assert employee_info("Rahul","EMP1024","Finance",45000)==expected_output
