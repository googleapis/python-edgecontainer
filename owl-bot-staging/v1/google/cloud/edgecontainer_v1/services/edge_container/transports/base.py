# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.edgecontainer_v1.types import resources
from google.cloud.edgecontainer_v1.types import service
from google.longrunning import operations_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-edgecontainer',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class EdgeContainerTransport(abc.ABC):
    """Abstract transport class for EdgeContainer."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'edgecontainer.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_clusters: gapic_v1.method.wrap_method(
                self.list_clusters,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cluster: gapic_v1.method.wrap_method(
                self.get_cluster,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_cluster: gapic_v1.method.wrap_method(
                self.create_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_cluster: gapic_v1.method.wrap_method(
                self.update_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_cluster: gapic_v1.method.wrap_method(
                self.delete_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_access_token: gapic_v1.method.wrap_method(
                self.generate_access_token,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_node_pools: gapic_v1.method.wrap_method(
                self.list_node_pools,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_node_pool: gapic_v1.method.wrap_method(
                self.get_node_pool,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_node_pool: gapic_v1.method.wrap_method(
                self.create_node_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_node_pool: gapic_v1.method.wrap_method(
                self.update_node_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_node_pool: gapic_v1.method.wrap_method(
                self.delete_node_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_machines: gapic_v1.method.wrap_method(
                self.list_machines,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_machine: gapic_v1.method.wrap_method(
                self.get_machine,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_vpn_connections: gapic_v1.method.wrap_method(
                self.list_vpn_connections,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vpn_connection: gapic_v1.method.wrap_method(
                self.get_vpn_connection,
                default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_vpn_connection: gapic_v1.method.wrap_method(
                self.create_vpn_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_vpn_connection: gapic_v1.method.wrap_method(
                self.delete_vpn_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_clusters(self) -> Callable[
            [service.ListClustersRequest],
            Union[
                service.ListClustersResponse,
                Awaitable[service.ListClustersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_cluster(self) -> Callable[
            [service.GetClusterRequest],
            Union[
                resources.Cluster,
                Awaitable[resources.Cluster]
            ]]:
        raise NotImplementedError()

    @property
    def create_cluster(self) -> Callable[
            [service.CreateClusterRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_cluster(self) -> Callable[
            [service.UpdateClusterRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_cluster(self) -> Callable[
            [service.DeleteClusterRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def generate_access_token(self) -> Callable[
            [service.GenerateAccessTokenRequest],
            Union[
                service.GenerateAccessTokenResponse,
                Awaitable[service.GenerateAccessTokenResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_node_pools(self) -> Callable[
            [service.ListNodePoolsRequest],
            Union[
                service.ListNodePoolsResponse,
                Awaitable[service.ListNodePoolsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_node_pool(self) -> Callable[
            [service.GetNodePoolRequest],
            Union[
                resources.NodePool,
                Awaitable[resources.NodePool]
            ]]:
        raise NotImplementedError()

    @property
    def create_node_pool(self) -> Callable[
            [service.CreateNodePoolRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_node_pool(self) -> Callable[
            [service.UpdateNodePoolRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_node_pool(self) -> Callable[
            [service.DeleteNodePoolRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_machines(self) -> Callable[
            [service.ListMachinesRequest],
            Union[
                service.ListMachinesResponse,
                Awaitable[service.ListMachinesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_machine(self) -> Callable[
            [service.GetMachineRequest],
            Union[
                resources.Machine,
                Awaitable[resources.Machine]
            ]]:
        raise NotImplementedError()

    @property
    def list_vpn_connections(self) -> Callable[
            [service.ListVpnConnectionsRequest],
            Union[
                service.ListVpnConnectionsResponse,
                Awaitable[service.ListVpnConnectionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_vpn_connection(self) -> Callable[
            [service.GetVpnConnectionRequest],
            Union[
                resources.VpnConnection,
                Awaitable[resources.VpnConnection]
            ]]:
        raise NotImplementedError()

    @property
    def create_vpn_connection(self) -> Callable[
            [service.CreateVpnConnectionRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_vpn_connection(self) -> Callable[
            [service.DeleteVpnConnectionRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'EdgeContainerTransport',
)
