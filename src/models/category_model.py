from typing import Optional

from pydantic import BaseModel, Field


# represents how the category data will be stored in your MongoDB database.
class CategorySchema(BaseModel):
    category_id: int = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "_id": "ObjectId",
                "category_id": 10,
                "name": "Moda Feminina",
                "image": "http://imagem.com.br",
                "meta_data": {
                    "description": "",
                    "meta_title": "",
                    "meta_description": "",
                    "meta_keyword": "",
                    "second_description": ""
                },
                "module_id": 1,
                "status": 1,
                "disabled": 0,
                "parent_id": 10,
                "path": [
                    {
                        "path_id": 119,
                        "_id": "ObjectId",
                        "level": 0
                    },
                    {
                        "path_id": 126,
                        "_id": "ObjectId",
                        "level": 1
                    }
                ],
                "layout": {
                    "carousel_id": 1,
                    "top": 1,
                    "bottom": 1,
                    "lateral": 1,
                    "column": 1,
                    "description_position": 0,
                    "category_title_h1": None,
                    "show_breadcrumbs": 1,
                    "show_top_order": 0,
                    "show_name_category": 1,
                    "image_icon": None,
                    "drop_image": None,
                    "drop_link": None,
                    "show_image_subcategory": None,
                    "customer_exibition": None
                },
                "marketing" : {
                    "promotional": 0,
                    "outfit" : [
                        {
                            "outfit_id": 1,
                            "_id": "ObjectId",
                        },
                        {
                            "outfit_id": 2,
                            "_id": "ObjectId",
                        }
                    ],
                    "coupon" : [
                        {
                            "coupon_id": 1,
                            "_id": "ObjectId",
                        },
                        {
                            "coupon_id": 2,
                            "_id": "ObjectId",
                        }
                    ],
                    "filters": [
                        {
                            "filter_id": 1,
                            "_id": "ObjectId",

                        },
                        {
                            "filter_id": 2,
                            "_id": "ObjectId",

                        }
                    ]
                },
                "sort": {
                    "sort_order": 1,
                    "option_sort_order_status": 1,
                    "option_sort_order_category": "pd.name",
                    "option_type_sort_order": "ASC"
                },
                "information": None,
                "index": 1,
                "nolink": None,
                "products": [
                    {
                        "product_id": 1,
                        "_id": "ObjectId"

                    },
                    {
                        "product_id": 2,
                        "_id": "ObjectId"

                    },
                    {
                        "product_id": 3,
                        "_id": "ObjectId"

                    }
                ]
            }
        }


class UpdateCategoryModel(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = CategorySchema.Config.schema_extra

