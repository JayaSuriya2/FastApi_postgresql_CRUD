from db.databasse import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from views import db_user
from schema.user_schema import User_schema

router = APIRouter(
   prefix='/api/v1/User',
  tags=['User']
)

@router.get('/')
async def get_alluser(db: Session = Depends(get_db)):
  return await db_user.get_alluser(db)


@router.get('/{id}')
async def get_userbyid(id:int,db:Session=Depends(get_db)):
  return await db_user.get_userbyid(id,db)


@router.post('/')
async def create_user(request:User_schema,db:Session=Depends(get_db)):
  return await db_user.create_user(request,db)

@router.put('/update/{id}')
async def update_user(id:int,request:User_schema,db:Session=Depends(get_db)):
  return await db_user.update_user(id,request,db)

@router.delete('/delete/{id}')
async def delete_user(id:int,db:Session=Depends(get_db)):
  return await db_user.delete_user(id,db)