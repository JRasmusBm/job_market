from sites.relocate import jobs as relocate_jobs
from mongoengine import connect
import schedule
import time
import asyncio


async def gather_items(getters):
    lists = await asyncio.gather(*getters)
    return [item for sublist in lists for item in sublist]


async def write_jobs(jobs):
    for job in jobs:
        print(job)
        connect()
        job.save()
    return jobs


async def main():
    jobs = await gather_items([relocate_jobs()])
    await write_jobs(jobs)


def cron():
    asyncio.run(main())


try:
    schedule.every().day.at("00:00").do(cron)
    while 1:
        schedule.run_pending()
        time.sleep(1)
except Exception as e:
    print(e)
