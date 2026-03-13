from core.base_endpoint import BaseEndpoint


class DiskEndpoint(BaseEndpoint):

    def get_disk_info(self):
        return self.request("GET", "/v1/disk/resources", params={"path": "disk:/"})
    
    def get_non_existing_resource(self):
        return self.request("GET", "/v1/disk/resources", params={"path": "disk:/non_existing_resource"})