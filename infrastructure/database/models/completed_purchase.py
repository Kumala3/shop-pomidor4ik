from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

from infrastructure.database.models.base import Base, TableNameMixin, TimestampMixin


class CompletedPurchase(Base, TableNameMixin, TimestampMixin):
    """
    Represents a purchase made by a user.

    Attributes:
        completed_purchase_id (int): The unique identifier for the purchase.
        user_id (int): The user ID associated with the purchase.
        product_id (int): The product ID associated with the purchase.
        purchase_status (str): The status of the purchase.
    """

    purchase_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )
    username: Mapped[Optional[str]] = mapped_column(String)
    software: Mapped[str] = mapped_column(String)
    payment_method: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, server_default="Paid")