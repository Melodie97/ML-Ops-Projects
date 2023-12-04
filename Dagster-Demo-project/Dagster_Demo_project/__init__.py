from dagster import (
    load_assets_from_modules,
    Definitions,
    define_asset_job,
    ScheduleDefinition
)
from Dagster_Demo_project import assets
import os
from github import Github

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    schedules=[
        ScheduleDefinition(
            job=define_asset_job(name="daily_refresh", selection="*"),
            cron_schedule="@daily",
        )
    ],
    resources={"github_api": Github(os.environ["GITHUB_ACCESS_TOKEN"])}
)
