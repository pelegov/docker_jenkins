import requests
import json
import pymysql


conn = pymysql.connect(host='sql11.freemysqlhosting.net', port=3306, user='sql11506470', passwd='QwjD6b64t9', db='sql11506470')
conn.autocommit(True)
cursor = conn.cursor()


url = "http://localhost:5000/users/2"  #defining url for call
### Creating payload
payload = json.dumps({
  "user_id": 2,
  "user_name": "navetime",
  "creation_date": "17022022"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

###Get method
get = requests.get('http://127.0.0.1:5000/users/2')
if get.ok:
    print(get.json())

###Function for checking realibility of the data.
def get_value_be():
    user_id = "2"
    cursor.execute("SELECT * FROM sql11506470.users WHERE (user_id) = " + user_id + ";")
    user_name = ""
    for row in cursor:
        print(row)
        user_name = row[1]
    cursor.close()
    conn.close()
    return user_name

get_value_be()
