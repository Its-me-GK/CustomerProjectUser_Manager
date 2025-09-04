# As per the requirements, the task has been completed. ✅

---

## ⚙️ 1. How to Run the Project

1. **Download/Clone the Repository**
2. **Create Database** with the name `CPU_relManager` in MySQL.
3. **Install dependencies** (compatible with the latest Python version):
   * `django`
   * `mysqlclient`
4. Navigate to the project root directory (where `manage.py` is located) and run database migrations.
5. Run the following commands in order:
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   py manage.py createsuperuser   # Create admin user
   py manage.py runserver
   ```
6. Server will start at `http://127.0.0.1:8000/` and APIs can now be tested.

---

## 🗄️ 2. Database Design

Django uses the **MVT pattern (Model–View–Template)** and comes with a built-in ORM.

By defining **models** (Python classes), Django automatically creates the required database tables after migrations.

* **Requirement:**
  * A **Client** can have multiple  **Projects** .
  * A **Project** can have multiple  **Users** .
  * A **User** can be assigned to multiple  **Projects** .

Relationship schema:

```
Client  --->  Projects  <-->  Users
```

* **One-to-Many** : Implemented using `ForeignKey`
* **Many-to-Many** : Implemented using `ManyToManyField`

---

## 🧪 3. Testing APIs with Postman

### 1. **List Clients**

**GET** `http://127.0.0.1:8000/clients/`

> Returns all registered clients.

---

### 2. **Create Client**

**POST** `http://127.0.0.1:8000/clients/`

Request body:

```json
{
  "client_name": "Alphabet",
  "client_phone": 1234567890,
  "client_email": "alphabet@info.org"
}
```

---

### 3. **Create Project under Client**

**POST** `http://127.0.0.1:8000/clients/<id>/projects/`

Request body:

```json
{
  "project_name": "First Project",
  "project_description": "This is the first project by Realme client 4",
  "users": [{"id": 2}, {"id": 3}, {"id": 7}]
}
```

---

### 4. **Update Client**

**PUT** `http://127.0.0.1:8000/clients/<id>/`

Request body:

```json
{
  "client_name": "Nimap"
}
```

---

### 5. **Delete Client**

**DELETE** `http://127.0.0.1:8000/clients/<id>/`

> Deletes the client with the given ID.

---

### 6. **Projects for Logged-In User**

**GET** `http://127.0.0.1:8000/projects/`

* Returns all projects assigned to the logged-in user.
* If not logged in → returns `"Login required"` message.

---

## 🔍 Suggested Improvements

1. Fix small typo: `runsever` → `runserver`.
2. Clarify in **Update Client** that `PUT` requires an `id` in the URL.
3. (Optional) Add **expected JSON responses** in examples — helps testers see the output format.

---

👉 This is a clean, beginner-friendly README.

Do you want me to also add a **table of endpoints** at the end (like Swagger-style summary), so you can quickly refer during testing/interview?

---

## ⚙️ 1. How to Run the Project

1. **Download/Clone the Repository**
2. **Create Database** with the name `CPU_relManager` in MySQL.
3. **Install dependencies** (compatible with the latest Python version):
   * `django`
   * `mysqlclient`
4. Navigate to the project root directory (where `manage.py` is located) and run database migrations.
5. Run the following commands in order:
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   py manage.py createsuperuser   # Create admin user
   py manage.py runserver
   ```
6. Server will start at `http://127.0.0.1:8000/` and APIs can now be tested.

---

## 🗄️ 2. Database Design

Django uses the **MVT pattern (Model–View–Template)** and comes with a built-in ORM.

By defining **models** (Python classes), Django automatically creates the required database tables after migrations.

* **Requirement:**
  * A **Client** can have multiple  **Projects** .
  * A **Project** can have multiple  **Users** .
  * A **User** can be assigned to multiple  **Projects** .

Relationship schema:

```
Client  --->  Projects  <-->  Users
```

* **One-to-Many** : Implemented using `ForeignKey`
* **Many-to-Many** : Implemented using `ManyToManyField`

---

## 🧪 3. Testing APIs with Postman

### 1. **List Clients**

**GET** `http://127.0.0.1:8000/clients/`

> Returns all registered clients.

---

### 2. **Create Client**

**POST** `http://127.0.0.1:8000/clients/`

Request body:

```json
{
  "client_name": "Alphabet",
  "client_phone": 1234567890,
  "client_email": "alphabet@info.org"
}
```

---

### 3. **Create Project under Client & Assign Users to Project using IDs**

**POST** `http://127.0.0.1:8000/clients/<id>/projects/`

Request body:

```json
{
  "project_name": "Realme 6 Pro",
  "project_description": "This is the first project by Realme client 4",
  "users": [{"id": 2}, {"id": 3}, {"id": 7}]
}
```

---

### 4. **Update Client**

**PUT**  `http://127.0.0.1:8000/clients/<id>/`

Request body:

```json
{
  "client_name": "Nimap"
}
```

---

### 5. **Delete Client**

**DELETE** `http://127.0.0.1:8000/clients/<id>/`

> Deletes the client with the given ID.

---

### 6. **Projects for Logged-In User**

**GET** `http://127.0.0.1:8000/projects/`

* Returns all projects assigned to the logged-in user.
* If not logged in → returns `"Login required"` message.


---

#### Thank You!

*GK*
