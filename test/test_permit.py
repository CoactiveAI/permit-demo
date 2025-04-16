import uuid

import pytest

from permit import Permit, RoleAssignmentCreate, UserCreate, UserUpdate
from src.config import Settings


@pytest.mark.asyncio
async def test_create_client() -> None:
    settings = Settings()
    org_id = settings.PERMIT_ORG_ID
    user_id = str(uuid.uuid4())
    permit = Permit(
        pdp=settings.PERMIT_PDP_URL,
        token=settings.PERMIT_SDK_KEY,
        proxy_facts_via_pdp=True,
        facts_sync_timeout=60,
        facts_sync_timeout_policy="fail",
    )
    await permit.api.users.sync(
        user=UserCreate(
            key=user_id,
            first_name="hi",
            last_name="",
            attributes={"oauth_client": True, "full_access": True},
        )
    )
    # Manually update it after the sync to ensure this is not a viable workaround
    await permit.api.users.update(
        user_key=user_id,
        user_data=UserUpdate(attributes={"oauth_client": True, "full_access": True}),
    )
    await permit.api.users.assign_role(
        assignment=RoleAssignmentCreate(
            role="member",
            tenant=org_id,
            user=user_id,
        )
    )
    roles = await permit.api.users.get_assigned_roles(user=user_id, tenant=org_id)
    permissions = await permit.get_user_permissions(user={"key": user_id}, tenants=[org_id])
    print(permissions)

    assert len(roles) > 0

    assert len(permissions.get(f"__tenant:{settings.PERMIT_ORG_ID}").get("permissions")) > 0
