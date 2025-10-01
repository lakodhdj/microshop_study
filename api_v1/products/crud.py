"""
Create
Read
Update
Delete
"""

from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import ProductCreate, ProductOut, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    stat = select(Product).order_by(Product.id)
    result: Result = await session.execute(stat)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)

    await session.commit()
    return product


async def update_product(
    session: AsyncSession,
    product: ProductOut,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for k, v in product_update.model_dump().items():
        setattr(product, k, v)

    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: ProductOut,
) -> None:
    await session.delete(product)
    await session.commit()
