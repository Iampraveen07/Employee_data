#dictionary to store collections
collections = {}

# Sample employee data
employee_data = [
    {"EmployeeID": "E02001", "Name": "Praveenkumar Iyappan", "Department": "HR", "Gender": "Male"},
    {"EmployeeID": "E02002", "Name": "Myvizhi Kannan", "Department": "Techsuport", "Gender": "Female"},
    {"EmployeeID": "E02003", "Name": "Sreeram Sundhar", "Department": "IT", "Gender": "Male"},
    {"EmployeeID": "E02004", "Name": "Subhashini Mohan", "Department": "Finance", "Gender": "Female"},
    {"EmployeeID": "E02005", "Name": "Rahul Ashok", "Department": "IT", "Gender": "Male"},
    {"EmployeeID": "E02006", "Name": "Vibin Thangavelu", "Department": "Techsuport", "Gender": "Male"},
    {"EmployeeID": "E02007", "Name": "Shalini Balu", "Department": "IT", "Gender": "Female"},
    {"EmployeeID": "E02004", "Name": "Kishore Pranav", "Department": "Techsuport", "Gender": "Male"}
]

# 1. Create Collection
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")

# 2. Index Data (excluding the given column)
def indexData(p_collection_name, p_exclude_column):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' not found.")
        return
    for emp in employee_data:
        indexed_emp = {k: v for k, v in emp.items() if k != p_exclude_column}
        collections[p_collection_name].append(indexed_emp)
    print(f"Data indexed into '{p_collection_name}', excluding '{p_exclude_column}' column.")

# 3. Search By Column
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' not found.")
        return []
    results = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
    print(f"Search results in '{p_collection_name}' for {p_column_name} = {p_column_value}: {results}")
    return results

# 4. Get Employee Count
def getEmpCount(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' not found.")
        return 0
    count = len(collections[p_collection_name])
    print(f"Employee count in '{p_collection_name}': {count}")
    return count

# 5. Delete Employee by ID
def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' not found.")
        return
    initial_count = len(collections[p_collection_name])
    collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get("EmployeeID") != p_employee_id]
    final_count = len(collections[p_collection_name])
    if initial_count == final_count:
        print(f"Employee with ID '{p_employee_id}' not found in '{p_collection_name}'.")
    else:
        print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")

# 6. Get Department Facet (Group by Department)
def getDepFacet(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' not found.")
        return {}
    department_count = {}
    for emp in collections[p_collection_name]:
        department = emp.get("Department", "Unknown")
        department_count[department] = department_count.get(department, 0) + 1
    print(f"Department facet for '{p_collection_name}': {department_count}")
    return department_count


# --- Function Executions ---

# Collection Names
v_nameCollection = 'Hash_Praveenkumar'
v_phoneCollection = 'Hash_3298'

# 1. Create Collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# 2. Index Data
indexData(v_nameCollection,None)
indexData(v_phoneCollection,None)


# 3. Get Employee Count (initial, but now after indexing)
getEmpCount(v_nameCollection)

# 4. Delete Employee by ID
delEmpById(v_nameCollection, 'E02003')

# 5. Get Employee Count (after deletion)
getEmpCount(v_nameCollection)

# 6. Search By Column
searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

# 7. Get Department Facet
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)






















