from mongoengine import *


# class Meta(Document):
#     protein_factor = FloatField()
#     fat_factor = FloatField()
#
#
# class Name(Document):
#     long = StringField()
#     common = ListField(StringField())
#     sci = StringField()


class Portion(Document):
    unit = StringField()
    g = FloatField()
    amt = FloatField()


class Nutrient(Document):
    code = StringField()

    class Meta(Document):
        is_add = StringField()
        mod_month = StringField()
        upper_error = StringField()
        mod_year = StringField()
        source_type = StringField()
        std_error = FloatField()
        conf = StringField()
        imputed = StringField()
        lower_error = StringField()
        data_points = IntField()
        stat_comments = StringField()
        minval = StringField()
        maxval = StringField()
        studies = StringField()
        rounded = StringField()
        sources = ListField(StringField())
        degrees_of_freedom = StringField()

    name = StringField()
    units = StringField()
    abbr = StringField()
    value = FileField()


class Food(Document):
    id = ObjectIdField()
    manufacturer = StringField()
    group = StringField()
    # meta = Meta()
    # name = Name()
    portion = ListField(ReferenceField(Portion))
    nutrients = ListField(ReferenceField(Nutrient))
