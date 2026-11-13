from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelModrinthArrayResponseDoc = TypedDict('ModelModrinthArrayResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelModrinthObjectResponseDoc = TypedDict('ModelModrinthObjectResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
}, total=False)

ModelModrinthHashUpdatesRequest = TypedDict('ModelModrinthHashUpdatesRequest', {
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'game_versions': NotRequired[list[str]],
    'hashes': Required[list[str]],
    'loaders': NotRequired[list[str]],
}, total=False)

ModelModrinthIndividualUpdatesRequest = TypedDict('ModelModrinthIndividualUpdatesRequest', {
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'hashes': Required[list[ModelModrinthHashFilter]],
}, total=False)

ModelModrinthHashFilter = TypedDict('ModelModrinthHashFilter', {
    'game_versions': NotRequired[list[str]],
    'hash': Required[str],
    'loaders': NotRequired[list[str]],
}, total=False)

ModelModrinthHashesRequest = TypedDict('ModelModrinthHashesRequest', {
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'hashes': Required[list[str]],
}, total=False)

ModelModrinthFiltersRequest = TypedDict('ModelModrinthFiltersRequest', {
    'game_versions': NotRequired[list[str]],
    'loaders': NotRequired[list[str]],
}, total=False)

ModelModrinthSearchV3BodyRequest = TypedDict('ModelModrinthSearchV3BodyRequest', {
    'facets': NotRequired[str],
    'filters': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated', 'date_created', 'date_modified', 'minecraft_java_server.verified_plays_2w', 'minecraft_java_server.ping.data.players_online']],
    'limit': NotRequired[str],
    'new_filters': NotRequired[str],
    'offset': NotRequired[str],
    'query': NotRequired[str],
    'show_metadata': NotRequired[bool],
    'version': NotRequired[str],
}, total=False)

ModelModrinthStringListResponseDoc = TypedDict('ModelModrinthStringListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[str]],
    'msg': NotRequired[str],
}, total=False)

ModrinthCollectionResponse = ModelModrinthObjectResponseDoc
ModrinthCollectionParams = TypedDict('ModrinthCollectionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthCollectionsResponse = ModelModrinthArrayResponseDoc
ModrinthCollectionsParams = TypedDict('ModrinthCollectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

ModrinthMetadataLinkPlatformsResponse = ModelModrinthArrayResponseDoc
ModrinthMetadataLinkPlatformsParams = TypedDict('ModrinthMetadataLinkPlatformsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ModrinthMetadataLoaderFieldsResponse = ModelModrinthStringListResponseDoc
ModrinthMetadataLoaderFieldsParams = TypedDict('ModrinthMetadataLoaderFieldsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ModrinthMetadataLoaderFieldValuesResponse = ModelModrinthArrayResponseDoc
ModrinthMetadataLoaderFieldValuesParams = TypedDict('ModrinthMetadataLoaderFieldValuesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'field': Required[str],
}, total=False)

ModrinthMetadataLoadersResponse = ModelModrinthArrayResponseDoc
ModrinthMetadataLoadersParams = TypedDict('ModrinthMetadataLoadersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ModrinthOrganizationResponse = ModelModrinthObjectResponseDoc
ModrinthOrganizationParams = TypedDict('ModrinthOrganizationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationProjectsResponse = ModelModrinthArrayResponseDoc
ModrinthOrganizationProjectsParams = TypedDict('ModrinthOrganizationProjectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationsResponse = ModelModrinthArrayResponseDoc
ModrinthOrganizationsParams = TypedDict('ModrinthOrganizationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

ModrinthProjectResponse = ModelModrinthObjectResponseDoc
ModrinthProjectParams = TypedDict('ModrinthProjectParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthCheckProjectResponse = ModelModrinthObjectResponseDoc
ModrinthCheckProjectParams = TypedDict('ModrinthCheckProjectParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthDependenciesResponse = ModelModrinthObjectResponseDoc
ModrinthDependenciesParams = TypedDict('ModrinthDependenciesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthProjectDisclosuresResponse = ModelModrinthObjectResponseDoc
ModrinthProjectDisclosuresParams = TypedDict('ModrinthProjectDisclosuresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthProjectVersionsResponse = ModelModrinthArrayResponseDoc
ModrinthProjectVersionsParams = TypedDict('ModrinthProjectVersionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'loaders': NotRequired[str],
    'game_versions': NotRequired[str],
    'featured': NotRequired[bool],
    'include_changelog': NotRequired[bool],
}, total=False)

ModrinthProjectVersionResponse = ModelModrinthObjectResponseDoc
ModrinthProjectVersionParams = TypedDict('ModrinthProjectVersionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'number': Required[str],
}, total=False)

ModrinthProjectsResponse = ModelModrinthArrayResponseDoc
ModrinthProjectsParams = TypedDict('ModrinthProjectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

ModrinthRandomProjectsResponse = ModelModrinthArrayResponseDoc
ModrinthRandomProjectsParams = TypedDict('ModrinthRandomProjectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': Required[int],
}, total=False)

ModrinthSearchResponse = ModelModrinthObjectResponseDoc
ModrinthSearchParams = TypedDict('ModrinthSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'facets': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ModrinthStatisticsResponse = ModelModrinthObjectResponseDoc
ModrinthStatisticsParams = TypedDict('ModrinthStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ModrinthLicenseResponse = ModelModrinthObjectResponseDoc
ModrinthLicenseParams = TypedDict('ModrinthLicenseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthTagsResponse = ModelModrinthArrayResponseDoc
ModrinthTagsParams = TypedDict('ModrinthTagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'type': Required[Literal['category', 'loader', 'game_version', 'license', 'donation_platform', 'report_type', 'project_type', 'side_type']],
}, total=False)

ModrinthForgeUpdatesResponse = ModelModrinthObjectResponseDoc
ModrinthForgeUpdatesParams = TypedDict('ModrinthForgeUpdatesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'neoforge': NotRequired[Literal['include', 'only']],
}, total=False)

ModrinthSearchV3Response = ModelModrinthObjectResponseDoc
ModrinthSearchV3Params = TypedDict('ModrinthSearchV3Params', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated', 'date_created', 'date_modified', 'minecraft_java_server.verified_plays_2w', 'minecraft_java_server.ping.data.players_online']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'new_filters': NotRequired[str],
    'facets': NotRequired[str],
    'filters': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModrinthSearchV3BodyBody = ModelModrinthSearchV3BodyRequest
ModrinthSearchV3BodyResponse = ModelModrinthObjectResponseDoc
ModrinthSearchV3BodyParams = TypedDict('ModrinthSearchV3BodyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthSearchV3BodyBody],
}, total=False)

ModrinthSearchV3OptionsResponse = ModelModrinthObjectResponseDoc
ModrinthSearchV3OptionsParams = TypedDict('ModrinthSearchV3OptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ModrinthVersionResponse = ModelModrinthObjectResponseDoc
ModrinthVersionParams = TypedDict('ModrinthVersionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ModrinthFileProjectsBody = ModelModrinthHashesRequest
ModrinthFileProjectsResponse = ModelModrinthObjectResponseDoc
ModrinthFileProjectsParams = TypedDict('ModrinthFileProjectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthFileProjectsBody],
}, total=False)

ModrinthFileVersionResponse = ModelModrinthObjectResponseDoc
ModrinthFileVersionParams = TypedDict('ModrinthFileVersionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
}, total=False)

ModrinthFileUpdateBody = ModelModrinthFiltersRequest
ModrinthFileUpdateResponse = ModelModrinthObjectResponseDoc
ModrinthFileUpdateParams = TypedDict('ModrinthFileUpdateParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'body': Required[ModrinthFileUpdateBody],
}, total=False)

ModrinthFileVersionsBody = ModelModrinthHashesRequest
ModrinthFileVersionsResponse = ModelModrinthObjectResponseDoc
ModrinthFileVersionsParams = TypedDict('ModrinthFileVersionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthFileVersionsBody],
}, total=False)

ModrinthFilesUpdateBody = ModelModrinthHashUpdatesRequest
ModrinthFilesUpdateResponse = ModelModrinthObjectResponseDoc
ModrinthFilesUpdateParams = TypedDict('ModrinthFilesUpdateParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthFilesUpdateBody],
}, total=False)

ModrinthFilesUpdateIndividualBody = ModelModrinthIndividualUpdatesRequest
ModrinthFilesUpdateIndividualResponse = ModelModrinthObjectResponseDoc
ModrinthFilesUpdateIndividualParams = TypedDict('ModrinthFilesUpdateIndividualParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthFilesUpdateIndividualBody],
}, total=False)

ModrinthFilesUpdateManyBody = ModelModrinthHashUpdatesRequest
ModrinthFilesUpdateManyResponse = ModelModrinthObjectResponseDoc
ModrinthFilesUpdateManyParams = TypedDict('ModrinthFilesUpdateManyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'body': Required[ModrinthFilesUpdateManyBody],
}, total=False)

ModrinthVersionsResponse = ModelModrinthArrayResponseDoc
ModrinthVersionsParams = TypedDict('ModrinthVersionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

class ModrinthGroup:
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionStreamParams]) -> BinaryIO: ...
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionTextResponseParams]) -> str: ...
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionDefaultParams]) -> ModrinthCollectionResponse: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsTextResponseParams]) -> str: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsDefaultParams]) -> ModrinthCollectionsResponse: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsTextResponseParams]) -> str: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsDefaultParams]) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsTextResponseParams]) -> str: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsDefaultParams]) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesTextResponseParams]) -> str: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesDefaultParams]) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersTextResponseParams]) -> str: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersDefaultParams]) -> ModrinthMetadataLoadersResponse: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationStreamParams]) -> BinaryIO: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationTextResponseParams]) -> str: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationDefaultParams]) -> ModrinthOrganizationResponse: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsTextResponseParams]) -> str: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsDefaultParams]) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsStreamParams]) -> BinaryIO: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsTextResponseParams]) -> str: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsDefaultParams]) -> ModrinthOrganizationsResponse: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectStreamParams]) -> BinaryIO: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectTextResponseParams]) -> str: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectDefaultParams]) -> ModrinthProjectResponse: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectStreamParams]) -> BinaryIO: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectTextResponseParams]) -> str: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectDefaultParams]) -> ModrinthCheckProjectResponse: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesStreamParams]) -> BinaryIO: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesTextResponseParams]) -> str: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesDefaultParams]) -> ModrinthDependenciesResponse: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresStreamParams]) -> BinaryIO: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresTextResponseParams]) -> str: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresDefaultParams]) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsTextResponseParams]) -> str: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsDefaultParams]) -> ModrinthProjectVersionsResponse: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionStreamParams]) -> BinaryIO: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionTextResponseParams]) -> str: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionDefaultParams]) -> ModrinthProjectVersionResponse: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsTextResponseParams]) -> str: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsDefaultParams]) -> ModrinthProjectsResponse: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsTextResponseParams]) -> str: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsDefaultParams]) -> ModrinthRandomProjectsResponse: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchDefaultParams]) -> ModrinthSearchResponse: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsTextResponseParams]) -> str: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsDefaultParams]) -> ModrinthStatisticsResponse: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseStreamParams]) -> BinaryIO: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseTextResponseParams]) -> str: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseDefaultParams]) -> ModrinthLicenseResponse: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsDefaultParams]) -> ModrinthTagsResponse: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesStreamParams]) -> BinaryIO: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesTextResponseParams]) -> str: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesDefaultParams]) -> ModrinthForgeUpdatesResponse: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3StreamParams]) -> BinaryIO: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3TextResponseParams]) -> str: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3DefaultParams]) -> ModrinthSearchV3Response: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyStreamParams]) -> BinaryIO: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyTextResponseParams]) -> str: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyDefaultParams]) -> ModrinthSearchV3BodyResponse: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsStreamParams]) -> BinaryIO: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsTextResponseParams]) -> str: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsDefaultParams]) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionStreamParams]) -> BinaryIO: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionTextResponseParams]) -> str: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionDefaultParams]) -> ModrinthVersionResponse: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsTextResponseParams]) -> str: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsDefaultParams]) -> ModrinthFileProjectsResponse: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionStreamParams]) -> BinaryIO: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionTextResponseParams]) -> str: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionDefaultParams]) -> ModrinthFileVersionResponse: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateStreamParams]) -> BinaryIO: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateTextResponseParams]) -> str: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateDefaultParams]) -> ModrinthFileUpdateResponse: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsTextResponseParams]) -> str: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsDefaultParams]) -> ModrinthFileVersionsResponse: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateStreamParams]) -> BinaryIO: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateTextResponseParams]) -> str: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateDefaultParams]) -> ModrinthFilesUpdateResponse: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualStreamParams]) -> BinaryIO: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualTextResponseParams]) -> str: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualDefaultParams]) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyStreamParams]) -> BinaryIO: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyTextResponseParams]) -> str: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyDefaultParams]) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsTextResponseParams]) -> str: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsDefaultParams]) -> ModrinthVersionsResponse: ...

OperationId = Literal[
    'modrinth-collection',
    'modrinth-collections',
    'modrinth-metadata-link-platforms',
    'modrinth-metadata-loader-fields',
    'modrinth-metadata-loader-field-values',
    'modrinth-metadata-loaders',
    'modrinth-organization',
    'modrinth-organization-projects',
    'modrinth-organizations',
    'modrinth-project',
    'modrinth-check-project',
    'modrinth-dependencies',
    'modrinth-project-disclosures',
    'modrinth-project-versions',
    'modrinth-project-version',
    'modrinth-projects',
    'modrinth-random-projects',
    'modrinth-search',
    'modrinth-statistics',
    'modrinth-license',
    'modrinth-tags',
    'modrinth-forge-updates',
    'modrinth-search-v3',
    'modrinth-search-v3-body',
    'modrinth-search-v3-options',
    'modrinth-version',
    'modrinth-file-projects',
    'modrinth-file-version',
    'modrinth-file-update',
    'modrinth-file-versions',
    'modrinth-files-update',
    'modrinth-files-update-individual',
    'modrinth-files-update-many',
    'modrinth-versions',
]

class CrawloraClient:
    modrinth: ModrinthGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-collection'],
        params: ModrinthCollectionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCollectionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-collections'],
        params: ModrinthCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCollectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-metadata-link-platforms'],
        params: ModrinthMetadataLinkPlatformsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-metadata-loader-fields'],
        params: ModrinthMetadataLoaderFieldsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-metadata-loader-field-values'],
        params: ModrinthMetadataLoaderFieldValuesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-metadata-loaders'],
        params: ModrinthMetadataLoadersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoadersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-organization'],
        params: ModrinthOrganizationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-organization-projects'],
        params: ModrinthOrganizationProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-organizations'],
        params: ModrinthOrganizationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-project'],
        params: ModrinthProjectParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-check-project'],
        params: ModrinthCheckProjectParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCheckProjectResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-dependencies'],
        params: ModrinthDependenciesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthDependenciesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-project-disclosures'],
        params: ModrinthProjectDisclosuresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-project-versions'],
        params: ModrinthProjectVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectVersionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-project-version'],
        params: ModrinthProjectVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectVersionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-projects'],
        params: ModrinthProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-random-projects'],
        params: ModrinthRandomProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthRandomProjectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-search'],
        params: ModrinthSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-statistics'],
        params: ModrinthStatisticsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-license'],
        params: ModrinthLicenseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthLicenseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-tags'],
        params: ModrinthTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthTagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-forge-updates'],
        params: ModrinthForgeUpdatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthForgeUpdatesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-search-v3'],
        params: ModrinthSearchV3Params = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3Response: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-search-v3-body'],
        params: ModrinthSearchV3BodyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3BodyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-search-v3-options'],
        params: ModrinthSearchV3OptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-version'],
        params: ModrinthVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthVersionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-file-projects'],
        params: ModrinthFileProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileProjectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-file-version'],
        params: ModrinthFileVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileVersionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-file-update'],
        params: ModrinthFileUpdateParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileUpdateResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-file-versions'],
        params: ModrinthFileVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileVersionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-files-update'],
        params: ModrinthFilesUpdateParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-files-update-individual'],
        params: ModrinthFilesUpdateIndividualParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-files-update-many'],
        params: ModrinthFilesUpdateManyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['modrinth-versions'],
        params: ModrinthVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthVersionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-collection'],
        params: ModrinthCollectionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCollectionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-collections'],
        params: ModrinthCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCollectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-metadata-link-platforms'],
        params: ModrinthMetadataLinkPlatformsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-metadata-loader-fields'],
        params: ModrinthMetadataLoaderFieldsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-metadata-loader-field-values'],
        params: ModrinthMetadataLoaderFieldValuesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-metadata-loaders'],
        params: ModrinthMetadataLoadersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthMetadataLoadersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-organization'],
        params: ModrinthOrganizationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-organization-projects'],
        params: ModrinthOrganizationProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-organizations'],
        params: ModrinthOrganizationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthOrganizationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-project'],
        params: ModrinthProjectParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-check-project'],
        params: ModrinthCheckProjectParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthCheckProjectResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-dependencies'],
        params: ModrinthDependenciesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthDependenciesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-project-disclosures'],
        params: ModrinthProjectDisclosuresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-project-versions'],
        params: ModrinthProjectVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectVersionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-project-version'],
        params: ModrinthProjectVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectVersionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-projects'],
        params: ModrinthProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthProjectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-random-projects'],
        params: ModrinthRandomProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthRandomProjectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-search'],
        params: ModrinthSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-statistics'],
        params: ModrinthStatisticsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-license'],
        params: ModrinthLicenseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthLicenseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-tags'],
        params: ModrinthTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthTagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-forge-updates'],
        params: ModrinthForgeUpdatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthForgeUpdatesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-search-v3'],
        params: ModrinthSearchV3Params = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3Response: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-search-v3-body'],
        params: ModrinthSearchV3BodyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3BodyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-search-v3-options'],
        params: ModrinthSearchV3OptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-version'],
        params: ModrinthVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthVersionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-file-projects'],
        params: ModrinthFileProjectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileProjectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-file-version'],
        params: ModrinthFileVersionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileVersionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-file-update'],
        params: ModrinthFileUpdateParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileUpdateResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-file-versions'],
        params: ModrinthFileVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFileVersionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-files-update'],
        params: ModrinthFilesUpdateParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-files-update-individual'],
        params: ModrinthFilesUpdateIndividualParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-files-update-many'],
        params: ModrinthFilesUpdateManyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['modrinth-versions'],
        params: ModrinthVersionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ModrinthVersionsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class ModrinthClient(CrawloraClient):
    def __enter__(self) -> ModrinthClient: ...
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionStreamParams]) -> BinaryIO: ...
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionTextResponseParams]) -> str: ...
    @overload
    def collection(self, **params: Unpack[ModrinthCollectionDefaultParams]) -> ModrinthCollectionResponse: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsTextResponseParams]) -> str: ...
    @overload
    def collections(self, **params: Unpack[ModrinthCollectionsDefaultParams]) -> ModrinthCollectionsResponse: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsTextResponseParams]) -> str: ...
    @overload
    def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsDefaultParams]) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsTextResponseParams]) -> str: ...
    @overload
    def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsDefaultParams]) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesTextResponseParams]) -> str: ...
    @overload
    def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesDefaultParams]) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersStreamParams]) -> BinaryIO: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersTextResponseParams]) -> str: ...
    @overload
    def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersDefaultParams]) -> ModrinthMetadataLoadersResponse: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationStreamParams]) -> BinaryIO: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationTextResponseParams]) -> str: ...
    @overload
    def organization(self, **params: Unpack[ModrinthOrganizationDefaultParams]) -> ModrinthOrganizationResponse: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsTextResponseParams]) -> str: ...
    @overload
    def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsDefaultParams]) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsStreamParams]) -> BinaryIO: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsTextResponseParams]) -> str: ...
    @overload
    def organizations(self, **params: Unpack[ModrinthOrganizationsDefaultParams]) -> ModrinthOrganizationsResponse: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectStreamParams]) -> BinaryIO: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectTextResponseParams]) -> str: ...
    @overload
    def project(self, **params: Unpack[ModrinthProjectDefaultParams]) -> ModrinthProjectResponse: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectStreamParams]) -> BinaryIO: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectTextResponseParams]) -> str: ...
    @overload
    def check_project(self, **params: Unpack[ModrinthCheckProjectDefaultParams]) -> ModrinthCheckProjectResponse: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesStreamParams]) -> BinaryIO: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesTextResponseParams]) -> str: ...
    @overload
    def dependencies(self, **params: Unpack[ModrinthDependenciesDefaultParams]) -> ModrinthDependenciesResponse: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresStreamParams]) -> BinaryIO: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresTextResponseParams]) -> str: ...
    @overload
    def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresDefaultParams]) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsTextResponseParams]) -> str: ...
    @overload
    def project_versions(self, **params: Unpack[ModrinthProjectVersionsDefaultParams]) -> ModrinthProjectVersionsResponse: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionStreamParams]) -> BinaryIO: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionTextResponseParams]) -> str: ...
    @overload
    def project_version(self, **params: Unpack[ModrinthProjectVersionDefaultParams]) -> ModrinthProjectVersionResponse: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsTextResponseParams]) -> str: ...
    @overload
    def projects(self, **params: Unpack[ModrinthProjectsDefaultParams]) -> ModrinthProjectsResponse: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsTextResponseParams]) -> str: ...
    @overload
    def random_projects(self, **params: Unpack[ModrinthRandomProjectsDefaultParams]) -> ModrinthRandomProjectsResponse: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ModrinthSearchDefaultParams]) -> ModrinthSearchResponse: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsTextResponseParams]) -> str: ...
    @overload
    def statistics(self, **params: Unpack[ModrinthStatisticsDefaultParams]) -> ModrinthStatisticsResponse: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseStreamParams]) -> BinaryIO: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseTextResponseParams]) -> str: ...
    @overload
    def license(self, **params: Unpack[ModrinthLicenseDefaultParams]) -> ModrinthLicenseResponse: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[ModrinthTagsDefaultParams]) -> ModrinthTagsResponse: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesStreamParams]) -> BinaryIO: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesTextResponseParams]) -> str: ...
    @overload
    def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesDefaultParams]) -> ModrinthForgeUpdatesResponse: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3StreamParams]) -> BinaryIO: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3TextResponseParams]) -> str: ...
    @overload
    def search_v3(self, **params: Unpack[ModrinthSearchV3DefaultParams]) -> ModrinthSearchV3Response: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyStreamParams]) -> BinaryIO: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyTextResponseParams]) -> str: ...
    @overload
    def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyDefaultParams]) -> ModrinthSearchV3BodyResponse: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsStreamParams]) -> BinaryIO: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsTextResponseParams]) -> str: ...
    @overload
    def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsDefaultParams]) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionStreamParams]) -> BinaryIO: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionTextResponseParams]) -> str: ...
    @overload
    def version(self, **params: Unpack[ModrinthVersionDefaultParams]) -> ModrinthVersionResponse: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsStreamParams]) -> BinaryIO: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsTextResponseParams]) -> str: ...
    @overload
    def file_projects(self, **params: Unpack[ModrinthFileProjectsDefaultParams]) -> ModrinthFileProjectsResponse: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionStreamParams]) -> BinaryIO: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionTextResponseParams]) -> str: ...
    @overload
    def file_version(self, **params: Unpack[ModrinthFileVersionDefaultParams]) -> ModrinthFileVersionResponse: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateStreamParams]) -> BinaryIO: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateTextResponseParams]) -> str: ...
    @overload
    def file_update(self, **params: Unpack[ModrinthFileUpdateDefaultParams]) -> ModrinthFileUpdateResponse: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsTextResponseParams]) -> str: ...
    @overload
    def file_versions(self, **params: Unpack[ModrinthFileVersionsDefaultParams]) -> ModrinthFileVersionsResponse: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateStreamParams]) -> BinaryIO: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateTextResponseParams]) -> str: ...
    @overload
    def files_update(self, **params: Unpack[ModrinthFilesUpdateDefaultParams]) -> ModrinthFilesUpdateResponse: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualStreamParams]) -> BinaryIO: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualTextResponseParams]) -> str: ...
    @overload
    def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualDefaultParams]) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyStreamParams]) -> BinaryIO: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyTextResponseParams]) -> str: ...
    @overload
    def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyDefaultParams]) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsStreamParams]) -> BinaryIO: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsTextResponseParams]) -> str: ...
    @overload
    def versions(self, **params: Unpack[ModrinthVersionsDefaultParams]) -> ModrinthVersionsResponse: ...

class AsyncModrinthClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncModrinthClient: ...
    modrinth: _AsyncModrinthGroup
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionStreamParams]) -> BinaryIO: ...
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionTextResponseParams]) -> str: ...
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionDefaultParams]) -> ModrinthCollectionResponse: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsTextResponseParams]) -> str: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsDefaultParams]) -> ModrinthCollectionsResponse: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsTextResponseParams]) -> str: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsDefaultParams]) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsTextResponseParams]) -> str: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsDefaultParams]) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesTextResponseParams]) -> str: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesDefaultParams]) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersTextResponseParams]) -> str: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersDefaultParams]) -> ModrinthMetadataLoadersResponse: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationStreamParams]) -> BinaryIO: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationTextResponseParams]) -> str: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationDefaultParams]) -> ModrinthOrganizationResponse: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsTextResponseParams]) -> str: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsDefaultParams]) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsStreamParams]) -> BinaryIO: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsTextResponseParams]) -> str: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsDefaultParams]) -> ModrinthOrganizationsResponse: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectStreamParams]) -> BinaryIO: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectTextResponseParams]) -> str: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectDefaultParams]) -> ModrinthProjectResponse: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectStreamParams]) -> BinaryIO: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectTextResponseParams]) -> str: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectDefaultParams]) -> ModrinthCheckProjectResponse: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesStreamParams]) -> BinaryIO: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesTextResponseParams]) -> str: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesDefaultParams]) -> ModrinthDependenciesResponse: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresStreamParams]) -> BinaryIO: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresTextResponseParams]) -> str: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresDefaultParams]) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsTextResponseParams]) -> str: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsDefaultParams]) -> ModrinthProjectVersionsResponse: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionTextResponseParams]) -> str: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionDefaultParams]) -> ModrinthProjectVersionResponse: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsTextResponseParams]) -> str: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsDefaultParams]) -> ModrinthProjectsResponse: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsTextResponseParams]) -> str: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsDefaultParams]) -> ModrinthRandomProjectsResponse: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchDefaultParams]) -> ModrinthSearchResponse: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsTextResponseParams]) -> str: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsDefaultParams]) -> ModrinthStatisticsResponse: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseStreamParams]) -> BinaryIO: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseTextResponseParams]) -> str: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseDefaultParams]) -> ModrinthLicenseResponse: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsDefaultParams]) -> ModrinthTagsResponse: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesStreamParams]) -> BinaryIO: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesTextResponseParams]) -> str: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesDefaultParams]) -> ModrinthForgeUpdatesResponse: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3StreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3TextResponseParams]) -> str: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3DefaultParams]) -> ModrinthSearchV3Response: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyStreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyTextResponseParams]) -> str: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyDefaultParams]) -> ModrinthSearchV3BodyResponse: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsTextResponseParams]) -> str: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsDefaultParams]) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionTextResponseParams]) -> str: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionDefaultParams]) -> ModrinthVersionResponse: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsTextResponseParams]) -> str: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsDefaultParams]) -> ModrinthFileProjectsResponse: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionTextResponseParams]) -> str: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionDefaultParams]) -> ModrinthFileVersionResponse: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateStreamParams]) -> BinaryIO: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateTextResponseParams]) -> str: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateDefaultParams]) -> ModrinthFileUpdateResponse: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsTextResponseParams]) -> str: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsDefaultParams]) -> ModrinthFileVersionsResponse: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateTextResponseParams]) -> str: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateDefaultParams]) -> ModrinthFilesUpdateResponse: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualTextResponseParams]) -> str: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualDefaultParams]) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyTextResponseParams]) -> str: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyDefaultParams]) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsTextResponseParams]) -> str: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsDefaultParams]) -> ModrinthVersionsResponse: ...

class _AsyncModrinthGroup:
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionStreamParams]) -> BinaryIO: ...
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionTextResponseParams]) -> str: ...
    @overload
    async def collection(self, **params: Unpack[ModrinthCollectionDefaultParams]) -> ModrinthCollectionResponse: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsTextResponseParams]) -> str: ...
    @overload
    async def collections(self, **params: Unpack[ModrinthCollectionsDefaultParams]) -> ModrinthCollectionsResponse: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsTextResponseParams]) -> str: ...
    @overload
    async def metadata_link_platforms(self, **params: Unpack[ModrinthMetadataLinkPlatformsDefaultParams]) -> ModrinthMetadataLinkPlatformsResponse: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsTextResponseParams]) -> str: ...
    @overload
    async def metadata_loader_fields(self, **params: Unpack[ModrinthMetadataLoaderFieldsDefaultParams]) -> ModrinthMetadataLoaderFieldsResponse: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesTextResponseParams]) -> str: ...
    @overload
    async def metadata_loader_field_values(self, **params: Unpack[ModrinthMetadataLoaderFieldValuesDefaultParams]) -> ModrinthMetadataLoaderFieldValuesResponse: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersStreamParams]) -> BinaryIO: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersTextResponseParams]) -> str: ...
    @overload
    async def metadata_loaders(self, **params: Unpack[ModrinthMetadataLoadersDefaultParams]) -> ModrinthMetadataLoadersResponse: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationStreamParams]) -> BinaryIO: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationTextResponseParams]) -> str: ...
    @overload
    async def organization(self, **params: Unpack[ModrinthOrganizationDefaultParams]) -> ModrinthOrganizationResponse: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsTextResponseParams]) -> str: ...
    @overload
    async def organization_projects(self, **params: Unpack[ModrinthOrganizationProjectsDefaultParams]) -> ModrinthOrganizationProjectsResponse: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsStreamParams]) -> BinaryIO: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsTextResponseParams]) -> str: ...
    @overload
    async def organizations(self, **params: Unpack[ModrinthOrganizationsDefaultParams]) -> ModrinthOrganizationsResponse: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectStreamParams]) -> BinaryIO: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectTextResponseParams]) -> str: ...
    @overload
    async def project(self, **params: Unpack[ModrinthProjectDefaultParams]) -> ModrinthProjectResponse: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectStreamParams]) -> BinaryIO: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectTextResponseParams]) -> str: ...
    @overload
    async def check_project(self, **params: Unpack[ModrinthCheckProjectDefaultParams]) -> ModrinthCheckProjectResponse: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesStreamParams]) -> BinaryIO: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesTextResponseParams]) -> str: ...
    @overload
    async def dependencies(self, **params: Unpack[ModrinthDependenciesDefaultParams]) -> ModrinthDependenciesResponse: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresStreamParams]) -> BinaryIO: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresTextResponseParams]) -> str: ...
    @overload
    async def project_disclosures(self, **params: Unpack[ModrinthProjectDisclosuresDefaultParams]) -> ModrinthProjectDisclosuresResponse: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsTextResponseParams]) -> str: ...
    @overload
    async def project_versions(self, **params: Unpack[ModrinthProjectVersionsDefaultParams]) -> ModrinthProjectVersionsResponse: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionTextResponseParams]) -> str: ...
    @overload
    async def project_version(self, **params: Unpack[ModrinthProjectVersionDefaultParams]) -> ModrinthProjectVersionResponse: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsTextResponseParams]) -> str: ...
    @overload
    async def projects(self, **params: Unpack[ModrinthProjectsDefaultParams]) -> ModrinthProjectsResponse: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsTextResponseParams]) -> str: ...
    @overload
    async def random_projects(self, **params: Unpack[ModrinthRandomProjectsDefaultParams]) -> ModrinthRandomProjectsResponse: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ModrinthSearchDefaultParams]) -> ModrinthSearchResponse: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsTextResponseParams]) -> str: ...
    @overload
    async def statistics(self, **params: Unpack[ModrinthStatisticsDefaultParams]) -> ModrinthStatisticsResponse: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseStreamParams]) -> BinaryIO: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseTextResponseParams]) -> str: ...
    @overload
    async def license(self, **params: Unpack[ModrinthLicenseDefaultParams]) -> ModrinthLicenseResponse: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[ModrinthTagsDefaultParams]) -> ModrinthTagsResponse: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesStreamParams]) -> BinaryIO: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesTextResponseParams]) -> str: ...
    @overload
    async def forge_updates(self, **params: Unpack[ModrinthForgeUpdatesDefaultParams]) -> ModrinthForgeUpdatesResponse: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3StreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3TextResponseParams]) -> str: ...
    @overload
    async def search_v3(self, **params: Unpack[ModrinthSearchV3DefaultParams]) -> ModrinthSearchV3Response: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyStreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyTextResponseParams]) -> str: ...
    @overload
    async def search_v3_body(self, **params: Unpack[ModrinthSearchV3BodyDefaultParams]) -> ModrinthSearchV3BodyResponse: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsTextResponseParams]) -> str: ...
    @overload
    async def search_v3_options(self, **params: Unpack[ModrinthSearchV3OptionsDefaultParams]) -> ModrinthSearchV3OptionsResponse: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionTextResponseParams]) -> str: ...
    @overload
    async def version(self, **params: Unpack[ModrinthVersionDefaultParams]) -> ModrinthVersionResponse: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsStreamParams]) -> BinaryIO: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsTextResponseParams]) -> str: ...
    @overload
    async def file_projects(self, **params: Unpack[ModrinthFileProjectsDefaultParams]) -> ModrinthFileProjectsResponse: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionTextResponseParams]) -> str: ...
    @overload
    async def file_version(self, **params: Unpack[ModrinthFileVersionDefaultParams]) -> ModrinthFileVersionResponse: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateStreamParams]) -> BinaryIO: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateTextResponseParams]) -> str: ...
    @overload
    async def file_update(self, **params: Unpack[ModrinthFileUpdateDefaultParams]) -> ModrinthFileUpdateResponse: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsTextResponseParams]) -> str: ...
    @overload
    async def file_versions(self, **params: Unpack[ModrinthFileVersionsDefaultParams]) -> ModrinthFileVersionsResponse: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateTextResponseParams]) -> str: ...
    @overload
    async def files_update(self, **params: Unpack[ModrinthFilesUpdateDefaultParams]) -> ModrinthFilesUpdateResponse: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualTextResponseParams]) -> str: ...
    @overload
    async def files_update_individual(self, **params: Unpack[ModrinthFilesUpdateIndividualDefaultParams]) -> ModrinthFilesUpdateIndividualResponse: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyStreamParams]) -> BinaryIO: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyTextResponseParams]) -> str: ...
    @overload
    async def files_update_many(self, **params: Unpack[ModrinthFilesUpdateManyDefaultParams]) -> ModrinthFilesUpdateManyResponse: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsStreamParams]) -> BinaryIO: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsTextResponseParams]) -> str: ...
    @overload
    async def versions(self, **params: Unpack[ModrinthVersionsDefaultParams]) -> ModrinthVersionsResponse: ...

ModrinthCollectionDefaultParams = TypedDict('ModrinthCollectionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthCollectionTextResponseParams = TypedDict('ModrinthCollectionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthCollectionStreamParams = TypedDict('ModrinthCollectionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthCollectionsDefaultParams = TypedDict('ModrinthCollectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

ModrinthCollectionsTextResponseParams = TypedDict('ModrinthCollectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

ModrinthCollectionsStreamParams = TypedDict('ModrinthCollectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

ModrinthMetadataLinkPlatformsDefaultParams = TypedDict('ModrinthMetadataLinkPlatformsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ModrinthMetadataLinkPlatformsTextResponseParams = TypedDict('ModrinthMetadataLinkPlatformsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ModrinthMetadataLinkPlatformsStreamParams = TypedDict('ModrinthMetadataLinkPlatformsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ModrinthMetadataLoaderFieldsDefaultParams = TypedDict('ModrinthMetadataLoaderFieldsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ModrinthMetadataLoaderFieldsTextResponseParams = TypedDict('ModrinthMetadataLoaderFieldsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ModrinthMetadataLoaderFieldsStreamParams = TypedDict('ModrinthMetadataLoaderFieldsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ModrinthMetadataLoaderFieldValuesDefaultParams = TypedDict('ModrinthMetadataLoaderFieldValuesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'field': Required[str],
}, total=False)

ModrinthMetadataLoaderFieldValuesTextResponseParams = TypedDict('ModrinthMetadataLoaderFieldValuesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'field': Required[str],
}, total=False)

ModrinthMetadataLoaderFieldValuesStreamParams = TypedDict('ModrinthMetadataLoaderFieldValuesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'field': Required[str],
}, total=False)

ModrinthMetadataLoadersDefaultParams = TypedDict('ModrinthMetadataLoadersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ModrinthMetadataLoadersTextResponseParams = TypedDict('ModrinthMetadataLoadersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ModrinthMetadataLoadersStreamParams = TypedDict('ModrinthMetadataLoadersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ModrinthOrganizationDefaultParams = TypedDict('ModrinthOrganizationDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationTextResponseParams = TypedDict('ModrinthOrganizationTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationStreamParams = TypedDict('ModrinthOrganizationStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationProjectsDefaultParams = TypedDict('ModrinthOrganizationProjectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationProjectsTextResponseParams = TypedDict('ModrinthOrganizationProjectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationProjectsStreamParams = TypedDict('ModrinthOrganizationProjectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthOrganizationsDefaultParams = TypedDict('ModrinthOrganizationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

ModrinthOrganizationsTextResponseParams = TypedDict('ModrinthOrganizationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

ModrinthOrganizationsStreamParams = TypedDict('ModrinthOrganizationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

ModrinthProjectDefaultParams = TypedDict('ModrinthProjectDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthProjectTextResponseParams = TypedDict('ModrinthProjectTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthProjectStreamParams = TypedDict('ModrinthProjectStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthCheckProjectDefaultParams = TypedDict('ModrinthCheckProjectDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthCheckProjectTextResponseParams = TypedDict('ModrinthCheckProjectTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthCheckProjectStreamParams = TypedDict('ModrinthCheckProjectStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthDependenciesDefaultParams = TypedDict('ModrinthDependenciesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthDependenciesTextResponseParams = TypedDict('ModrinthDependenciesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthDependenciesStreamParams = TypedDict('ModrinthDependenciesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthProjectDisclosuresDefaultParams = TypedDict('ModrinthProjectDisclosuresDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthProjectDisclosuresTextResponseParams = TypedDict('ModrinthProjectDisclosuresTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthProjectDisclosuresStreamParams = TypedDict('ModrinthProjectDisclosuresStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthProjectVersionsDefaultParams = TypedDict('ModrinthProjectVersionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'loaders': NotRequired[str],
    'game_versions': NotRequired[str],
    'featured': NotRequired[bool],
    'include_changelog': NotRequired[bool],
}, total=False)

ModrinthProjectVersionsTextResponseParams = TypedDict('ModrinthProjectVersionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'loaders': NotRequired[str],
    'game_versions': NotRequired[str],
    'featured': NotRequired[bool],
    'include_changelog': NotRequired[bool],
}, total=False)

ModrinthProjectVersionsStreamParams = TypedDict('ModrinthProjectVersionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'loaders': NotRequired[str],
    'game_versions': NotRequired[str],
    'featured': NotRequired[bool],
    'include_changelog': NotRequired[bool],
}, total=False)

ModrinthProjectVersionDefaultParams = TypedDict('ModrinthProjectVersionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'number': Required[str],
}, total=False)

ModrinthProjectVersionTextResponseParams = TypedDict('ModrinthProjectVersionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'number': Required[str],
}, total=False)

ModrinthProjectVersionStreamParams = TypedDict('ModrinthProjectVersionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'number': Required[str],
}, total=False)

ModrinthProjectsDefaultParams = TypedDict('ModrinthProjectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

ModrinthProjectsTextResponseParams = TypedDict('ModrinthProjectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

ModrinthProjectsStreamParams = TypedDict('ModrinthProjectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

ModrinthRandomProjectsDefaultParams = TypedDict('ModrinthRandomProjectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': Required[int],
}, total=False)

ModrinthRandomProjectsTextResponseParams = TypedDict('ModrinthRandomProjectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': Required[int],
}, total=False)

ModrinthRandomProjectsStreamParams = TypedDict('ModrinthRandomProjectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': Required[int],
}, total=False)

ModrinthSearchDefaultParams = TypedDict('ModrinthSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'facets': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ModrinthSearchTextResponseParams = TypedDict('ModrinthSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'facets': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ModrinthSearchStreamParams = TypedDict('ModrinthSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'facets': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ModrinthStatisticsDefaultParams = TypedDict('ModrinthStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ModrinthStatisticsTextResponseParams = TypedDict('ModrinthStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ModrinthStatisticsStreamParams = TypedDict('ModrinthStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ModrinthLicenseDefaultParams = TypedDict('ModrinthLicenseDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthLicenseTextResponseParams = TypedDict('ModrinthLicenseTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthLicenseStreamParams = TypedDict('ModrinthLicenseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthTagsDefaultParams = TypedDict('ModrinthTagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'type': Required[Literal['category', 'loader', 'game_version', 'license', 'donation_platform', 'report_type', 'project_type', 'side_type']],
}, total=False)

ModrinthTagsTextResponseParams = TypedDict('ModrinthTagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'type': Required[Literal['category', 'loader', 'game_version', 'license', 'donation_platform', 'report_type', 'project_type', 'side_type']],
}, total=False)

ModrinthTagsStreamParams = TypedDict('ModrinthTagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'type': Required[Literal['category', 'loader', 'game_version', 'license', 'donation_platform', 'report_type', 'project_type', 'side_type']],
}, total=False)

ModrinthForgeUpdatesDefaultParams = TypedDict('ModrinthForgeUpdatesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'neoforge': NotRequired[Literal['include', 'only']],
}, total=False)

ModrinthForgeUpdatesTextResponseParams = TypedDict('ModrinthForgeUpdatesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'neoforge': NotRequired[Literal['include', 'only']],
}, total=False)

ModrinthForgeUpdatesStreamParams = TypedDict('ModrinthForgeUpdatesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'neoforge': NotRequired[Literal['include', 'only']],
}, total=False)

ModrinthSearchV3DefaultParams = TypedDict('ModrinthSearchV3DefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated', 'date_created', 'date_modified', 'minecraft_java_server.verified_plays_2w', 'minecraft_java_server.ping.data.players_online']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'new_filters': NotRequired[str],
    'facets': NotRequired[str],
    'filters': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModrinthSearchV3TextResponseParams = TypedDict('ModrinthSearchV3TextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated', 'date_created', 'date_modified', 'minecraft_java_server.verified_plays_2w', 'minecraft_java_server.ping.data.players_online']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'new_filters': NotRequired[str],
    'facets': NotRequired[str],
    'filters': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModrinthSearchV3StreamParams = TypedDict('ModrinthSearchV3StreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'index': NotRequired[Literal['relevance', 'downloads', 'follows', 'newest', 'updated', 'date_created', 'date_modified', 'minecraft_java_server.verified_plays_2w', 'minecraft_java_server.ping.data.players_online']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'new_filters': NotRequired[str],
    'facets': NotRequired[str],
    'filters': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModrinthSearchV3BodyDefaultParams = TypedDict('ModrinthSearchV3BodyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthSearchV3BodyBody],
}, total=False)

ModrinthSearchV3BodyTextResponseParams = TypedDict('ModrinthSearchV3BodyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthSearchV3BodyBody],
}, total=False)

ModrinthSearchV3BodyStreamParams = TypedDict('ModrinthSearchV3BodyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthSearchV3BodyBody],
}, total=False)

ModrinthSearchV3OptionsDefaultParams = TypedDict('ModrinthSearchV3OptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ModrinthSearchV3OptionsTextResponseParams = TypedDict('ModrinthSearchV3OptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ModrinthSearchV3OptionsStreamParams = TypedDict('ModrinthSearchV3OptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ModrinthVersionDefaultParams = TypedDict('ModrinthVersionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ModrinthVersionTextResponseParams = TypedDict('ModrinthVersionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ModrinthVersionStreamParams = TypedDict('ModrinthVersionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ModrinthFileProjectsDefaultParams = TypedDict('ModrinthFileProjectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthFileProjectsBody],
}, total=False)

ModrinthFileProjectsTextResponseParams = TypedDict('ModrinthFileProjectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthFileProjectsBody],
}, total=False)

ModrinthFileProjectsStreamParams = TypedDict('ModrinthFileProjectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthFileProjectsBody],
}, total=False)

ModrinthFileVersionDefaultParams = TypedDict('ModrinthFileVersionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
}, total=False)

ModrinthFileVersionTextResponseParams = TypedDict('ModrinthFileVersionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
}, total=False)

ModrinthFileVersionStreamParams = TypedDict('ModrinthFileVersionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
}, total=False)

ModrinthFileUpdateDefaultParams = TypedDict('ModrinthFileUpdateDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'body': Required[ModrinthFileUpdateBody],
}, total=False)

ModrinthFileUpdateTextResponseParams = TypedDict('ModrinthFileUpdateTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'body': Required[ModrinthFileUpdateBody],
}, total=False)

ModrinthFileUpdateStreamParams = TypedDict('ModrinthFileUpdateStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hash': Required[str],
    'algorithm': NotRequired[Literal['sha1', 'sha512']],
    'body': Required[ModrinthFileUpdateBody],
}, total=False)

ModrinthFileVersionsDefaultParams = TypedDict('ModrinthFileVersionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthFileVersionsBody],
}, total=False)

ModrinthFileVersionsTextResponseParams = TypedDict('ModrinthFileVersionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthFileVersionsBody],
}, total=False)

ModrinthFileVersionsStreamParams = TypedDict('ModrinthFileVersionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthFileVersionsBody],
}, total=False)

ModrinthFilesUpdateDefaultParams = TypedDict('ModrinthFilesUpdateDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthFilesUpdateBody],
}, total=False)

ModrinthFilesUpdateTextResponseParams = TypedDict('ModrinthFilesUpdateTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthFilesUpdateBody],
}, total=False)

ModrinthFilesUpdateStreamParams = TypedDict('ModrinthFilesUpdateStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthFilesUpdateBody],
}, total=False)

ModrinthFilesUpdateIndividualDefaultParams = TypedDict('ModrinthFilesUpdateIndividualDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthFilesUpdateIndividualBody],
}, total=False)

ModrinthFilesUpdateIndividualTextResponseParams = TypedDict('ModrinthFilesUpdateIndividualTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthFilesUpdateIndividualBody],
}, total=False)

ModrinthFilesUpdateIndividualStreamParams = TypedDict('ModrinthFilesUpdateIndividualStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthFilesUpdateIndividualBody],
}, total=False)

ModrinthFilesUpdateManyDefaultParams = TypedDict('ModrinthFilesUpdateManyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'body': Required[ModrinthFilesUpdateManyBody],
}, total=False)

ModrinthFilesUpdateManyTextResponseParams = TypedDict('ModrinthFilesUpdateManyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'body': Required[ModrinthFilesUpdateManyBody],
}, total=False)

ModrinthFilesUpdateManyStreamParams = TypedDict('ModrinthFilesUpdateManyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'body': Required[ModrinthFilesUpdateManyBody],
}, total=False)

ModrinthVersionsDefaultParams = TypedDict('ModrinthVersionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

ModrinthVersionsTextResponseParams = TypedDict('ModrinthVersionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

ModrinthVersionsStreamParams = TypedDict('ModrinthVersionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)
