# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get statistics organized by country"


class Input:
    pass

class Output:
    COUNTRIES = "countries"
    

class GetCountryStatisticsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCountryStatisticsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "countries": {
      "type": "array",
      "title": "Countries",
      "description": "All countries and basic stats",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "countries"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
