

# class db_meals:

# async def add_meal(self, user: User):
#     try:
#         request = await db["users"].insert_one(
#             {'username': user.username, 'email': user.email, 'password': str(user.password)})
#         return request
#     except:
#         raise HTTPException(
#             status_code=403, detail=Custom_Error_Message.ADD_USER.value)

# async def get_user_with_email(self, user: User):
#     try:
#         request = await db["users"].find_one(
#             {'email': user.email})
#         return request
#     except Exception as e:
#         print(e)
#         raise HTTPException(
#             status_code=403, detail=Custom_Error_Message.NO_AUTHORIZATION.value)
