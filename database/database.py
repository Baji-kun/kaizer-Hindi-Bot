# (©)CodeXBotz
# Recoded by @Its_Oreki_Hotarou

import pymongo
import asyncio
from config import DB_URI, DB_NAME, FORCE_CHANNEL, FORCE_CHANNEL2

# Connect to MongoDB and select database
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

# Define collections
user_data = database['users']
admin_data = database['admins']
channel_data = database['channels']
channel_data2 = database['channels2']

# Utility function to run MongoDB operations asynchronously
async def run_async(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, func, *args, **kwargs)


# ---- USER MANAGEMENT ---- #

async def present_user(user_id: int):
    return await run_async(user_data.find_one, {'_id': user_id}) is not None


async def add_user(user_id: int):
    if not await present_user(user_id):
        await run_async(user_data.insert_one, {'_id': user_id})


async def full_userbase():
    user_docs = await run_async(user_data.find)
    return [doc['_id'] for doc in user_docs]


async def del_user(user_id: int):
    await run_async(user_data.delete_one, {'_id': user_id})


# ---- ADMIN MANAGEMENT ---- #

async def present_admin(admin_id: int):
    return await run_async(admin_data.find_one, {'_id': admin_id}) is not None


async def add_admin(admin_id: int):
    if not await present_admin(admin_id):
        await run_async(admin_data.insert_one, {'_id': admin_id})


async def full_adminbase():
    admin_docs = await run_async(admin_data.find)
    return [doc['_id'] for doc in admin_docs]


async def del_admin(admin_id: int):
    await run_async(admin_data.delete_one, {'_id': admin_id})


# ---- FORCE SUBSCRIPTION CHANNEL MANAGEMENT ---- #

async def get_force_channel_1():
    try:
        config = await run_async(channel_data.find_one, {})
        return config.get('force_sub_channel_1', FORCE_CHANNEL) if config else FORCE_CHANNEL
    except Exception as e:
        print(f"Error getting Force Subscribe Channel 1: {e}")
        return FORCE_CHANNEL


async def add_channel_1(channel_id: int):
    try:
        await run_async(channel_data.update_one, {}, {'$set': {'force_sub_channel_1': channel_id}}, upsert=True)
        print(f"Force Subscribe Channel 1 updated to: {channel_id}")
    except Exception as e:
        print(f"Error setting Force Subscribe Channel 1: {e}")


async def get_force_channel_2():
    try:
        config = await run_async(channel_data2.find_one, {})
        return config.get('force_sub_channel_2', FORCE_CHANNEL2) if config else FORCE_CHANNEL2
    except Exception as e:
        print(f"Error getting Force Subscribe Channel 2: {e}")
        return FORCE_CHANNEL2


async def add_channel_2(channel_id: int):
    try:
        await run_async(channel_data2.update_one, {}, {'$set': {'force_sub_channel_2': channel_id}}, upsert=True)
        print(f"Force Subscribe Channel 2 updated to: {channel_id}")
    except Exception as e:
        print(f"Error setting Force Subscribe Channel 2: {e}")


async def get_forcesub_channels():
    try:
        # Fetch channel IDs for Force Subscribe 1 and 2
        channel_1 = await get_force_channel_1()
        channel_2 = await get_force_channel_2()

        # Combine and deduplicate channel lists
        return list({channel_1, channel_2})
    except Exception as e:
        print(f"Error fetching Force Subscribe Channels: {e}")
        return []


# ---- TEST CONNECTION (OPTIONAL) ---- #

def test_db_connection():
    try:
        dbclient.server_info()  # Trigger an exception if connection fails
        print("✅ Connected to MongoDB successfully!")
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(f"❌ Failed to connect to MongoDB: {err}")
        
