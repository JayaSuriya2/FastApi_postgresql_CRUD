from schema.user_schema import User_schema
from sqlalchemy.orm import Session
from db.model import user_details
from sqlalchemy import select
from fastapi import HTTPException


async def get_alluser(db:Session):
    result = await db.execute(select(user_details))  
    user= result.scalars().all()
    # user=db.query(user_details).all()
    response={
        "status":200,
        "message":"user details get sucessfully",
        "responces":user
    }
    return response


async def get_userbyid(id:int,db:Session):
    result = await db.execute(select(user_details).where(user_details.id==id))
    user= result.scalar_one_or_none()
    response={
        "status":200,
        "message":"user details get sucessfully",
        "responces":user
    }
    return response

async def create_user(request:User_schema,db:Session):
    new_user= user_details(
        name = request.name,
        mail = request.mail,
        age= request.age,
        create_by= request.create_by,
        create_date= request.create_date
    )
    print(new_user)
    db.add(new_user)             
    await db.commit()            
    await db.refresh(new_user)   

    return {
        "status": 201,
        "message": "User created successfully",
        "response": new_user
    }


async def update_user(id:int,request:User_schema,db:Session):
    result = await db.execute(select(user_details).where(user_details.id == id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)

    return {
        "status": 200,
        "message": "User updated successfully",
        "response": user
    }

async def delete_user(id:int,db:Session):
    result = await db.execute(select(user_details).where(user_details.id == id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()

    return {"status": 200, "message": "User deleted successfully"}