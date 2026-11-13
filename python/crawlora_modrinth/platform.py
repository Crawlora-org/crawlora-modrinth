"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class ModrinthClient(CrawloraClient):
    """Synchronous Modrinth API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-modrinth-python/0.1.0')
        super().__init__(*args, **kwargs)

    def collection(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-collection', params, response_type=response_type, timeout=timeout, headers=headers)

    def collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    def metadata_link_platforms(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-metadata-link-platforms', params, response_type=response_type, timeout=timeout, headers=headers)

    def metadata_loader_fields(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-metadata-loader-fields', params, response_type=response_type, timeout=timeout, headers=headers)

    def metadata_loader_field_values(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-metadata-loader-field-values', params, response_type=response_type, timeout=timeout, headers=headers)

    def metadata_loaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-metadata-loaders', params, response_type=response_type, timeout=timeout, headers=headers)

    def organization(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-organization', params, response_type=response_type, timeout=timeout, headers=headers)

    def organization_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-organization-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    def organizations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-organizations', params, response_type=response_type, timeout=timeout, headers=headers)

    def project(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-project', params, response_type=response_type, timeout=timeout, headers=headers)

    def check_project(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-check-project', params, response_type=response_type, timeout=timeout, headers=headers)

    def dependencies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-dependencies', params, response_type=response_type, timeout=timeout, headers=headers)

    def project_disclosures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-project-disclosures', params, response_type=response_type, timeout=timeout, headers=headers)

    def project_versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-project-versions', params, response_type=response_type, timeout=timeout, headers=headers)

    def project_version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-project-version', params, response_type=response_type, timeout=timeout, headers=headers)

    def projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    def random_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-random-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def license(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-license', params, response_type=response_type, timeout=timeout, headers=headers)

    def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-tags', params, response_type=response_type, timeout=timeout, headers=headers)

    def forge_updates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-forge-updates', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_v3(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-search-v3', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_v3_body(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-search-v3-body', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_v3_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-search-v3-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-version', params, response_type=response_type, timeout=timeout, headers=headers)

    def file_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-file-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    def file_version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-file-version', params, response_type=response_type, timeout=timeout, headers=headers)

    def file_update(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-file-update', params, response_type=response_type, timeout=timeout, headers=headers)

    def file_versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-file-versions', params, response_type=response_type, timeout=timeout, headers=headers)

    def files_update(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-files-update', params, response_type=response_type, timeout=timeout, headers=headers)

    def files_update_individual(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-files-update-individual', params, response_type=response_type, timeout=timeout, headers=headers)

    def files_update_many(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-files-update-many', params, response_type=response_type, timeout=timeout, headers=headers)

    def versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('modrinth-versions', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncModrinthClient(AsyncCrawloraClient):
    """Asynchronous Modrinth API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-modrinth-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def collection(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-collection', params, response_type=response_type, timeout=timeout, headers=headers)

    async def collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    async def metadata_link_platforms(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-metadata-link-platforms', params, response_type=response_type, timeout=timeout, headers=headers)

    async def metadata_loader_fields(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-metadata-loader-fields', params, response_type=response_type, timeout=timeout, headers=headers)

    async def metadata_loader_field_values(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-metadata-loader-field-values', params, response_type=response_type, timeout=timeout, headers=headers)

    async def metadata_loaders(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-metadata-loaders', params, response_type=response_type, timeout=timeout, headers=headers)

    async def organization(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-organization', params, response_type=response_type, timeout=timeout, headers=headers)

    async def organization_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-organization-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def organizations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-organizations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def project(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-project', params, response_type=response_type, timeout=timeout, headers=headers)

    async def check_project(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-check-project', params, response_type=response_type, timeout=timeout, headers=headers)

    async def dependencies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-dependencies', params, response_type=response_type, timeout=timeout, headers=headers)

    async def project_disclosures(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-project-disclosures', params, response_type=response_type, timeout=timeout, headers=headers)

    async def project_versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-project-versions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def project_version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-project-version', params, response_type=response_type, timeout=timeout, headers=headers)

    async def projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def random_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-random-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def license(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-license', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-tags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def forge_updates(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-forge-updates', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_v3(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-search-v3', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_v3_body(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-search-v3-body', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_v3_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-search-v3-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-version', params, response_type=response_type, timeout=timeout, headers=headers)

    async def file_projects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-file-projects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def file_version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-file-version', params, response_type=response_type, timeout=timeout, headers=headers)

    async def file_update(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-file-update', params, response_type=response_type, timeout=timeout, headers=headers)

    async def file_versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-file-versions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def files_update(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-files-update', params, response_type=response_type, timeout=timeout, headers=headers)

    async def files_update_individual(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-files-update-individual', params, response_type=response_type, timeout=timeout, headers=headers)

    async def files_update_many(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-files-update-many', params, response_type=response_type, timeout=timeout, headers=headers)

    async def versions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('modrinth-versions', params, response_type=response_type, timeout=timeout, headers=headers)
