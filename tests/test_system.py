import pytest


@pytest.mark.asyncio
async def test_query_hello(async_client):

    # create subdivision
    mutation = """
    mutation
    {
      createSubdivision(subdivision:{
        name:"workers"
      })
      {
        id
        name
      }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation},
    )
    assert response.status_code == 200
    assert response.json()["data"]["createSubdivision"]["name"] == "workers"
    subdivision_id = response.json()["data"]["createSubdivision"]["id"]

    variables = {"subdivision_id": subdivision_id}

    # -------------------------------------#

    # create leader
    mutation = """
        mutation CreateEmployee($subdivision_id: Int!) {
        createEmployee(employee: {
            login: "log"
            password: "pass"
            firstName: "Ivan"
            lastName: "Ivanov"
            telegramName: "tiktok_maxim"
            subdivisionId: $subdivision_id
            email: "sa@vrn.tv"
            leader: true
        }) {
            id
            chatId
            subdivisionId
            login
            password
        }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation, "variables": variables},
    )
    assert response.status_code == 200
    assert response.json()["data"]["createEmployee"]["subdivisionId"] == subdivision_id

    variables["leader_id"] = response.json()["data"]["createEmployee"]["id"]
    variables["login"] = response.json()["data"]["createEmployee"]["login"]
    variables["password"] = response.json()["data"]["createEmployee"]["password"]

    # -------------------------------------#

    # create employee
    mutation = """
        mutation CreateEmployee($subdivision_id: Int!) {
        createEmployee(employee: {
            login: "log"
            password: "pass"
            firstName: "Max"
            lastName: "Pirko"
            telegramName: "pausebreak11"
            subdivisionId: $subdivision_id
            email: "sa@vrn.tv"
        }) {
            id
            subdivisionId
        }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation, "variables": variables},
    )
    assert response.status_code == 200
    assert response.json()["data"]["createEmployee"]["subdivisionId"] == subdivision_id

    variables["employee_id"] = response.json()["data"]["createEmployee"]["id"]

    # --------------------------------------------------------

    # login
    mutation = """
            mutation login($login: String!, $password: String!){
                login(login: $login
                     password: $password){
                        accessToken
                     }
            }
        """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation, "variables": variables},
    )
    assert response.status_code == 200
    assert response.json()["data"]["login"]["accessToken"] is not None

    variables["access_token"] = response.json()["data"]["login"]["accessToken"]

    # ----------------------------------------------

    # create project
    mutation = """
        mutation {
        createProject(project: {
            name:"Project-1"
            description:"Aboooout Project-1"
        }) {
            id
            name
        }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation, "variables": variables},
        headers={"Authorization": f"Bearer {variables["access_token"]}"},
    )

    assert response.status_code == 200
    assert response.json()["data"]["createProject"]["id"] is not None
    assert response.json()["data"]["createProject"]["name"] == "Project-1"

    variables["project_id"] = response.json()["data"]["createProject"]["id"]

    # --------------------------------------------------------

    # create task and assign for employee
    mutation = """
        mutation CreateTask($employee_id: Int!, $project_id: Int!) {
        createTask(task: {
            projectId:$project_id
            name:"Task-9669"
            description:"Aboooout Task-100"
            employeeId:$employee_id
            estimatedDaysToComplete:1
        }) {
            id
            name
        }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation, "variables": variables},
        headers={"Authorization": f"Bearer {variables["access_token"]}"},
    )

    assert response.status_code == 200
    assert response.json()["data"]["createTask"]["id"] is not None
    assert response.json()["data"]["createTask"]["name"] == "Task-9669"

    # -----------------------------------------------------

    # output of employee tasks

    query = """
    query FilterTasks($employee_id: Int!) {
        filterTasks(filterParam: {
            employeeId:$employee_id
        }) {
            id
            name
        }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": query, "variables": variables},
        headers={"Authorization": f"Bearer {variables["access_token"]}"},
    )
    assert response.status_code == 200
    assert len(response.json()["data"]["filterTasks"]) > 0


@pytest.mark.asyncio
async def test_mutation_say_hello(async_client):
    mutation = """
    mutation
    {
      createSubdivision(subdivision:{
        name:"workers"
      })
      {
        id
        name
      }
    }
    """
    response = await async_client.post(
        "/graphql",
        json={"query": mutation},
    )
    assert response.status_code == 200
    assert response.json()["data"]["createSubdivision"]["name"] == "workers"
