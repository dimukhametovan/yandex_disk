import allure


@allure.title("GET v1/disk/resources Happy Path")
def test_get_disk_info(disk_api):
    response = disk_api.get_disk_info()
    response.assert_status(200)
    response.assert_field('type', "dir")


@allure.title("GET v1/disk/resources 404 Not Found")
def test_get_non_existing_resource(disk_api):
    response = disk_api.get_non_existing_resource()
    response.assert_status(404)


@allure.title("GET v1/disk/resources 401 Unauthorized")
def test_get_resource_unauthorized(unauthorized_disk_api):
	response = unauthorized_disk_api.get_disk_info()
	response.assert_status(401)
