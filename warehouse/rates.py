"""Shipping rate calculations."""

SERVICES = {"standard", "express"}
_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone, one of ``local`` or ``regional``.
        service: ``standard`` (default) or ``express``. Express adds $7.

    Returns:
        Quoted price in dollars, rounded to two decimal places.

    Raises:
        ValueError: If weight is not positive, zone is unknown, or service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    if service == "express":
        base += _EXPRESS_SURCHARGE
    return round(base + 1.5 * weight_kg, 2)
