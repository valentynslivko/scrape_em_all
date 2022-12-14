import datetime

import mongoengine

from scrape_em_all.config import tz

datetime_with_tz = datetime.datetime.now(tz=tz)


class User(mongoengine.Document):
    username = mongoengine.StringField(required=True)
    telegram_id = mongoengine.StringField(required=True)
    has_parsed_djinni = mongoengine.BooleanField(default=False)
    has_parsed_dou = mongoengine.BooleanField(default=False)
    has_parsed_robota = mongoengine.BooleanField(default=False)
    has_parsed_workua = mongoengine.BooleanField(default=False)
    first_interaction_with_bot = mongoengine.DateTimeField(
        default=datetime_with_tz,
    )

    meta = {
        "db_alias": "core",
        "collection": "user",
    }


class BaseVacancy(mongoengine.Document):
    parsed_by = mongoengine.ReferenceField(User)
    title = mongoengine.StringField()
    link = mongoengine.StringField()
    short_description = mongoengine.StringField()
    ad_posted_at = mongoengine.DateField()

    meta = {
        "db_alias": "core",
        "ordering": ["-ad_posted_at"],
        "allow_inheritance": True,
        "abstract": True,
    }


class DjinniVacancies(BaseVacancy):
    meta = {
        "db_alias": "core",
        "collection": "djinni",
        "ordering": ["-ad_posted_at"],
    }


class DouVacancies(BaseVacancy):
    meta = {
        "db_alias": "core",
        "collection": "dou",
        "ordering": ["-ad_posted_at"],
    }


# class RobotaVacancies(DjinniVacancies):
#     meta = {
#         "db_alias": "core",
#         "collection": "robota",
#     }


class WorkVacancies(BaseVacancy):
    meta = {
        "db_alias": "core",
        "collection": "workua",
    }
