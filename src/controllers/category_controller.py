from database.db import category_collection
from bson.objectid import ObjectId


# helper
# isso é a forma com que os dados sao retornados
def category_helper(category) -> dict:
    return {
        "_id": str(category["_id"]),
        "fullname": category["fullname"],
        "email": category["email"],
        "course_of_study": category["course_of_study"],
        "year": category["year"],
        "GPA": category["gpa"],
    }


## CRUD
# Retrieve all categories present in the database
async def get_all_categories(query = None) -> dict:
    categories = []
    async for category in category_collection.find(query):
        categories.append(category_helper(category))
    return categories


# Add a new student into to the database
async def add_category(category_data: dict) -> dict:
    category = await category_collection.insert_one(category_data)
    new_category = await category_collection.find_one({"_id": category.inserted_id})
    return category_helper(new_category)


# Add categories in bulk
async def add_category_bulk(category_data: dict) -> dict:
    category = await category_collection.insert_many(category_data)
    return category_helper(category)


# Retrieve a category with a matching ID
async def get_category_by_id(id: str) -> dict:
    category = await category_collection.find_one({"_id": ObjectId(id)})
    if category:
        return category_helper(category)
    return False


# Update a category with a matching ID
async def update_category(id: str, category_data: dict):
    if category_data:
        category = await category_collection.find_one({"_id": ObjectId(id)})
        if category:
            updated_category = await category_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": category_data}
            )
            if updated_category:
                return True
            return False
    return False



# Delete a category from the database
async def delete_category(id: str):
    category = await category_collection.find_one({"_id": ObjectId(id)})
    if category:
        await category_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
