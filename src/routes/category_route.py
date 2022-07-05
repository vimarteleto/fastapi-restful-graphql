from typing import List, Optional
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controllers.category_controller import (
    add_category,
    add_category_bulk,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category,
)
from models.category_model import (
    CategorySchema,
    UpdateCategoryModel,
)
from models.response import (
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()


@router.post("/", response_description="Category data added into the database")
async def add_category_data(category: CategorySchema = Body(...)):
    category = jsonable_encoder(category)
    new_category = await add_category(category)
    return ResponseModel(new_category, "Category added successfully.")


@router.post("/bulk", response_description="Category data added into the database")
async def add_category_bulk_data(category: List[CategorySchema] = Body(...)):
    category = jsonable_encoder(category)
    bulk_categories = await add_category_bulk(category)
    return ResponseModel(bulk_categories, "Category added successfully.")


@router.get("/", response_description="Categories retrieved")
async def get_all_categories_data(query: Optional[dict] = None):
    categories = await get_all_categories(query)
    if categories:
        return ResponseModel(categories, "Categories data retrieved successfully")
    return ResponseModel(categories, "Empty list returned")


@router.get("/{id}", response_description="Category data retrieved")
async def get_category_by_id_data(id):
    category = await get_category_by_id(id)
    if category:
        return ResponseModel(category, "Category data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Category doesn't exist.")


@router.put("/{id}")
async def update_category_data(id: str, req: UpdateCategoryModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_category(id, req)
    if updated_student:
        return ResponseModel(
            "Category with ID: {} name update is successful".format(id),
            "Category name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the category data.",
    )


@router.delete("/{id}", response_description="Category data deleted from the database")
async def delete_category_data(id: str):
    deleted_student = await delete_category(id)
    if deleted_student:
        return ResponseModel(
            "Category with ID: {} removed".format(id), "Category deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Category with id {0} doesn't exist".format(id)
    )


