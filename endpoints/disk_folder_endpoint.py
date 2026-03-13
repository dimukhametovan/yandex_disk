from core.base_endpoint import BaseEndpoint

class FolderEndpoint(BaseEndpoint):
    def create(self, path, fields=None):
        params = {"path": path}
        if fields:
            params["fields"] = ",".join(fields)
        return self.request("PUT", "/resources", params=params)
