import requests

info = {"name": "Ujjwal Seth","regNo": "0827AL221139","email": "ujjwalseth2412@gmail.com"} #info with Body format
response = requests.post("https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON", json=info)
response_data = response.json()
webhook_url = response_data.get("webhook")
access_token = response_data.get("accessToken")

# sql query
sql_query = """
SELECT p.amount AS SALARY,
e.first_name || ' ' || e.last_name AS NAME,
CAST((JULIANDAY('now') - JULIANDAY(e.dob)) / 365 AS INTEGER) AS AGE,
d.department_name AS DEPARTMENT_NAME
FROM payments p
JOIN employee e ON p.emp_id = e.emp_id
JOIN department d ON e.department = d.department_id
WHERE STRFTIME('%d', p.payment_time) != '01'
ORDER BY SALARY DESC
LIMIT 1;
"""

header = {"Authorization": access_token, "Content-Type": "application/json"}
query_payload = {"finalQuery": sql_query.strip()}
result = requests.post(webhook_url, headers=header, json=query_payload)
print(result.text)
