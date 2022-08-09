"""Client to get asset from another organization server.

This module provides various helpers to access assets stored in remote Organizations.
It verifies as well the integrity of downloaded asset when possible.
"""
import os
import typing

import requests
import structlog
from django.conf import settings
from requests.auth import HTTPBasicAuth

from substrapp.exceptions import IntegrityError
from substrapp.exceptions import OrganizationError
from substrapp.utils import compute_hash
from substrapp.utils import get_hash

logger = structlog.get_logger(__name__)

CHUNK_SIZE = 1024 * 1024


def _fetch_secret(organization_id: str) -> str:
    """Find credentials to authenticate with remote organization."""
    from organization.models import OutgoingOrganization

    try:
        outgoing = OutgoingOrganization.objects.get(organization_id=organization_id)
    except OutgoingOrganization.DoesNotExist:
        logger.error("Missing outgoing credentials", organization_id=organization_id)
        raise
    return outgoing.secret


def http_get(
    channel: str,
    organization_id: str,
    url: str,
    stream: typing.Optional[bool] = False,
    headers: typing.Optional[dict[str, str]] = None,
) -> requests.Response:
    """Low level helper to get asset and return successful HTTP response."""
    secret = _fetch_secret(organization_id)

    headers = headers or {}
    headers.update(
        {
            "Accept": "application/json;version=0.0",
            "Substra-Channel-Name": channel,
        }
    )

    try:
        response = requests.get(
            url,
            headers=headers,
            stream=stream,
            auth=HTTPBasicAuth(settings.LEDGER_MSP_ID, secret),
            verify=not settings.DEBUG,
            timeout=settings.HTTP_CLIENT_TIMEOUT_SECONDS,
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        logger.exception("Get asset failure", url=url, e=e)
        raise OrganizationError(f"Failed to fetch {url}") from e

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        logger.error("Get asset failure", url=url, status=response.status_code, text=response.text)
        raise OrganizationError(f"Url: {url} returned status code: {response.status_code}")
    return response


def http_post(
    channel: str,
    organization_id: str,
    url: str,
    data: dict,
    headers: typing.Optional[dict[str, str]] = None,
) -> requests.Response:
    """Low level helper to get asset and return successful HTTP response."""
    secret = _fetch_secret(organization_id)

    headers = headers or {}
    headers.update(
        {
            "Accept": "application/json;version=0.0",
            "Substra-Channel-Name": channel,
        }
    )

    try:
        response = requests.post(
            url,
            data=data,
            headers=headers,
            auth=HTTPBasicAuth(settings.LEDGER_MSP_ID, secret),
            verify=not settings.DEBUG,
            timeout=settings.HTTP_CLIENT_TIMEOUT_SECONDS,
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        logger.exception("Post asset failure", url=url, e=e)
        raise OrganizationError(f"Failed to post to {url}") from e

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        logger.error("Post asset failure", url=url, status=response.status_code, text=response.text)
        raise OrganizationError(f"Url: {url} returned status code: {response.status_code}")
    return response


def download(
    channel: str,
    organization_id: str,
    url: str,
    destination: str,
    checksum: str,
    salt: typing.Optional[str] = None,
) -> None:
    """Download an asset data to a file (not atomic)."""
    response = http_get(channel, organization_id, url, stream=True)
    try:
        with open(destination, "wb") as fp:
            for chunk in response.iter_content(CHUNK_SIZE):
                fp.write(chunk)
    finally:
        response.close()

    new_checksum = get_hash(destination, key=salt)
    if new_checksum != checksum:
        os.remove(destination)
        raise IntegrityError(f"url {url}: checksum doesn't match expected={checksum} vs actual={new_checksum}")


def get(
    channel: str,
    organization_id: str,
    url: str,
    checksum: str,
    salt: typing.Optional[str] = None,
) -> bytes:
    """Get asset data."""
    response = http_get(channel, organization_id, url)
    content = response.content
    new_checksum = compute_hash(content, key=salt)
    if new_checksum != checksum:
        raise IntegrityError(f"url {url}: checksum doesn't match {checksum} vs {new_checksum}")
    return content


def post(
    channel: str,
    organization_id: str,
    url: str,
    data: dict,
) -> bytes:
    """Post asset data."""
    response = http_post(channel, organization_id, url, data)
    content = response.content
    return content
