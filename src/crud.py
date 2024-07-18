import httpx
from fastapi import HTTPException


async def get_obj(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()


async def create_obj(url: str, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()


async def update_obj(url: str, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(url=url, json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()


async def delete_obj(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(url=url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()


