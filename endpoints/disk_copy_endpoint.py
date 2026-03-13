from core.base_endpoint import BaseEndpoint

class ResourcesCopyEndpoint(BaseEndpoint):
    
    def copy(self, from_path, dst_path, force_async=False, overwrite=False, fields=None):
        params = {
            "from": from_path,
            "path": dst_path,
            "force_async": str(force_async).lower(),
            "overwrite": str(overwrite).lower(),
        }
        if fields:
            params["fields"] = ",".join(fields)

        return self.request("POST", "/v1/disk/resources/copy", params=params)
