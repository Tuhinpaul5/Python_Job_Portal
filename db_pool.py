import asyncpg
import json

with open('config.json') as config_file:
    config = json.load(config_file)

pool = None

async def init_pool():
    global pool 
    pool = await asyncpg.create_pool(
                user=config['db_user'], 
                password=config['db_password'], 
                database=config['db_name'], 
                host=config['db_host']
            )
    
    return pool
    