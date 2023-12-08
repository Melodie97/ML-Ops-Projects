from dagster import (
    AssetSelection,
    Definitions,
    define_asset_job,
    load_assets_from_modules,
    ScheduleDefinition,
    FilesystemIOManager,
)

from . import assets

all_assets = load_assets_from_modules([assets])

# Addition: define a job that will materialize the assets
hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(base_dir="data")

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={"io_manager": io_manager},
)
