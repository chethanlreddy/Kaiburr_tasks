# Task API Documentation

This document provides an overview and documentation for the FastAPI Task API. The API allows you to perform CRUD operations on tasks stored in a MongoDB database.

## API Endpoints

### Create Task

**Endpoint:** `/task/create-task`  
**Method:** `POST`  
**Description:** Create a new task with the provided data.

#### Request Body (JSON):

```json
{
  "id": 1,
  "name": "Task Name",
  "assignee": "Assignee Name",
  "project": "Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "ChethanLReddyProperty": "Randomly Generated String"
}
```

#### Response (JSON):

```json
{
  "id": 1,
  "name": "Task Name",
  "assignee": "Assignee Name",
  "project": "Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "ChethanLReddyProperty": "Randomly Generated String"
}
```

### Get All Tasks

**Endpoint:** `/task/task`  
**Method:** `GET`  
**Description:** Retrieve a list of all tasks.

#### Response (JSON):

```json
[
  {
    "id": 1,
    "name": "Task Name 1",
    "assignee": "Assignee Name 1",
    "project": "Project Name 1",
    "start_time": "YYYY-MM-DDTHH:MM:SS",
    "ChethanLReddyProperty": "Randomly Generated String"
  },
  {
    "id": 2,
    "name": "Task Name 2",
    "assignee": "Assignee Name 2",
    "project": "Project Name 2",
    "start_time": "YYYY-MM-DDTHH:MM:SS",
    "ChethanLReddyProperty": "Randomly Generated String"
  },
  ...
]
```

### Get Task by ID

**Endpoint:** `/task/task/{id}`  
**Method:** `GET`  
**Description:** Retrieve a specific task by its ID.

#### Path Parameters:

- `id` (int): Task ID

#### Response (JSON):

```json
{
  "id": 1,
  "name": "Task Name",
  "assignee": "Assignee Name",
  "project": "Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "ChethanLReddyProperty": "Randomly Generated String"
}
```

### Update Task

**Endpoint:** `/task/updatetask/{id}`  
**Method:** `PUT`  
**Description:** Update a specific task by its ID.

#### Path Parameters:

- `id` (int): Task ID

#### Request Body (JSON):

```json
{
  "id": 1,
  "name": "Updated Task Name",
  "assignee": "Updated Assignee Name",
  "project": "Updated Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS"
}
```

#### Response (JSON):

```json
{
  "id": 1,
  "name": "Updated Task Name",
  "assignee": "Updated Assignee Name",
  "project": "Updated Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "ChethanLReddyProperty": "Randomly Generated String"
}
```

### Delete Task

**Endpoint:** `/task/deletetask/{id}`  
**Method:** `DELETE`  
**Description:** Delete a specific task by its ID.

#### Path Parameters:

- `id` (int): Task ID

#### Response (No Content):

- Status Code: `204 No Content`

## Task Schema

### createTask

```json
{
  "id": 1,
  "name": "Task Name",
  "assignee": "Assignee Name",
  "project": "Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "ChethanLReddyProperty": "Randomly Generated String (Optional)"
}
```

### updateTask

```json
{
  "id": 1,
  "name": "Updated Task Name",
  "assignee": "Updated Assignee Name",
  "project": "Updated Project Name",
  "start_time": "YYYY-MM-DDTHH:MM:SS"
}
```

The `createTask` and `updateTask` schemas define the structure of the request and response bodies for creating and updating tasks, respectively. The `ChethanLReddyProperty` field in the `createTask` schema is optional and is populated with a randomly generated string if not provided.

## Usage

1. **Create Task:**

   - Send a `POST` request to `/task/create-task` with the task details in the request body.

2. **Get All Tasks:**

   - Send a `GET` request to `/task/task` to retrieve a list of all tasks.

3. **Get Task by ID:**

   - Send a `GET` request to `/task/task/{id}` to retrieve a specific task by its ID.

4. **Update Task:**

   - Send a `PUT` request to `/task/updatetask/{id}` with the updated task details in the request body.

5. **Delete Task:**
   - Send a `DELETE` request to `/task/deletetask/{id}` to delete a specific task by its ID.

**Note:** Replace `{id}` in the endpoints with the actual task ID.
