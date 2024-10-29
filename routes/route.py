from fastapi import APIRouter
from config.database import users_collection
from schema.schemas import list_serial
from models.users import User

router = APIRouter()

# Get Request Method for all Users
@router.get("/users")
async def get_users():
    users = list_serial(users_collection.find(), User)
    return users

# Post Request Method for a new User
@router.post("/users")
async def post_user(user: User):
    users_collection.insert_one(dict(user))
