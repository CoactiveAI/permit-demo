from permit import Permit
from src.config import Settings

_permit: Permit | None = None

settings = Settings()

def get_permit() -> Permit:
    global _permit
    if _permit is None:
        _permit = Permit(
            pdp=settings.PERMIT_PDP_URL,
            token=settings.PERMIT_SDK_KEY,
            proxy_facts_via_pdp=True,
            facts_sync_timeout=15,
            facts_sync_timeout_policy="fail",
        )
    return _permit
