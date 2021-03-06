# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lists the UBA (User Behavioral Analysis) activities"


class Input:
    LIMIT = "limit"
    OFFSET = "offset"
    

class Output:
    ACTIVITIES = "activities"
    

class ListActivitiesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of paginated results to return. Max: 100",
      "default": 20,
      "order": 2
    },
    "offset": {
      "type": "number",
      "title": "Offset",
      "description": "Pagination offset",
      "default": 0,
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListActivitiesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activities": {
      "type": "array",
      "title": "Activities",
      "description": "Activities",
      "items": {
        "$ref": "#/definitions/activity"
      },
      "order": 1
    }
  },
  "definitions": {
    "activity": {
      "type": "object",
      "title": "activity",
      "properties": {
        "client_ip": {
          "type": "string",
          "title": "Client Ip",
          "description": "The clients IP address",
          "order": 2
        },
        "client_location": {
          "$ref": "#/definitions/client_location",
          "title": "Client Location",
          "description": "Client location information",
          "order": 6
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "When the activity took place",
          "format": "date-time",
          "order": 4
        },
        "event_category": {
          "type": "string",
          "title": "Event Category",
          "description": "The event category type",
          "order": 7
        },
        "event_id": {
          "type": "string",
          "title": "Event Id",
          "description": "This is CloudLock Internal Identifier for an activity",
          "order": 1
        },
        "event_type": {
          "type": "string",
          "title": "Event Type",
          "description": "The type of the event",
          "order": 3
        },
        "extra": {
          "type": "object",
          "title": "Extra",
          "description": "Additional information related to the activity",
          "order": 12
        },
        "extra.auth": {
          "type": "object",
          "title": "Extra Auth",
          "description": "Authentication information related to the activity",
          "order": 13
        },
        "extra.auth.auth_type": {
          "type": "string",
          "title": "Extra Auth Auth Type",
          "description": "Type of authentication",
          "order": 14
        },
        "extra.auth.is_suspicious": {
          "type": "boolean",
          "title": "Extra Auth Is Suspicious",
          "description": "Indication regarding whether the activity is flagged as being suspicious",
          "order": 15
        },
        "operation_successful": {
          "type": "boolean",
          "title": "Operation Successful",
          "description": "Did the activity succeed",
          "order": 5
        },
        "origin_id": {
          "type": "string",
          "title": "Origin Id",
          "description": "The origin id",
          "order": 8
        },
        "raw": {
          "type": "object",
          "title": "Raw",
          "description": "Raw information for the activity",
          "order": 16
        },
        "user": {
          "$ref": "#/definitions/user",
          "title": "User",
          "description": "User information",
          "order": 9
        },
        "user_agent": {
          "type": "string",
          "title": "User Agent",
          "order": 10
        },
        "vendor": {
          "$ref": "#/definitions/vendor",
          "title": "Vendor",
          "description": "Platform information. ",
          "order": 11
        }
      },
      "definitions": {
        "client_location": {
          "type": "object",
          "title": "client_location",
          "properties": {
            "city": {
              "type": "string",
              "title": "City",
              "order": 5
            },
            "country": {
              "$ref": "#/definitions/country",
              "title": "Country",
              "order": 3
            },
            "lat": {
              "type": "number",
              "title": "Lat",
              "order": 1
            },
            "lng": {
              "type": "number",
              "title": "Lng",
              "order": 2
            },
            "region": {
              "$ref": "#/definitions/region",
              "title": "Region",
              "order": 4
            }
          },
          "definitions": {
            "country": {
              "type": "object",
              "title": "country",
              "properties": {
                "code": {
                  "type": "string",
                  "title": "Code",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                }
              }
            },
            "region": {
              "type": "object",
              "title": "region",
              "properties": {
                "code": {
                  "type": "string",
                  "title": "Code",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                }
              }
            }
          }
        },
        "country": {
          "type": "object",
          "title": "country",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            }
          }
        },
        "region": {
          "type": "object",
          "title": "region",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "User email address",
              "order": 4
            },
            "exposure_counts": {
              "type": "number",
              "title": "Exposure Counts",
              "description": "Number of objects the user has, broken down by their exposure",
              "order": 10
            },
            "id": {
              "type": "string",
              "title": "Id",
              "description": "Unique internal identifier for the user",
              "order": 1
            },
            "incident_status_counts": {
              "type": "number",
              "title": "Incident Status Counts",
              "description": "Number of incidents the user has, broken down by status",
              "order": 11
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User name",
              "order": 3
            },
            "ou": {
              "type": "string",
              "title": "Ou",
              "description": "The OU the user belongs to",
              "order": 6
            },
            "suspended": {
              "type": "boolean",
              "title": "Suspended",
              "description": "Is the user suspended or not",
              "order": 5
            },
            "total_active_incidents": {
              "type": "number",
              "title": "Total Active Incidents",
              "description": "Total number of incidents that are in play (new or in progress)",
              "order": 7
            },
            "total_entities": {
              "type": "number",
              "title": "Total Entities",
              "description": "Total number of objects the user has",
              "order": 8
            },
            "total_incidents": {
              "type": "number",
              "title": "Total Incidents",
              "description": "Total number of incidents the user has",
              "order": 9
            },
            "vendor": {
              "$ref": "#/definitions/vendor",
              "title": "Vendor",
              "description": "Vendor name",
              "order": 2
            }
          },
          "definitions": {
            "vendor": {
              "type": "object",
              "title": "vendor",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of the vendor. For example, google",
                  "order": 1
                }
              }
            }
          }
        },
        "vendor": {
          "type": "object",
          "title": "vendor",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the vendor. For example, google",
              "order": 1
            }
          }
        }
      }
    },
    "client_location": {
      "type": "object",
      "title": "client_location",
      "properties": {
        "city": {
          "type": "string",
          "title": "City",
          "order": 5
        },
        "country": {
          "$ref": "#/definitions/country",
          "title": "Country",
          "order": 3
        },
        "lat": {
          "type": "number",
          "title": "Lat",
          "order": 1
        },
        "lng": {
          "type": "number",
          "title": "Lng",
          "order": 2
        },
        "region": {
          "$ref": "#/definitions/region",
          "title": "Region",
          "order": 4
        }
      },
      "definitions": {
        "country": {
          "type": "object",
          "title": "country",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            }
          }
        },
        "region": {
          "type": "object",
          "title": "region",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            }
          }
        }
      }
    },
    "country": {
      "type": "object",
      "title": "country",
      "properties": {
        "code": {
          "type": "string",
          "title": "Code",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        }
      }
    },
    "region": {
      "type": "object",
      "title": "region",
      "properties": {
        "code": {
          "type": "string",
          "title": "Code",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "User email address",
          "order": 4
        },
        "exposure_counts": {
          "type": "number",
          "title": "Exposure Counts",
          "description": "Number of objects the user has, broken down by their exposure",
          "order": 10
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Unique internal identifier for the user",
          "order": 1
        },
        "incident_status_counts": {
          "type": "number",
          "title": "Incident Status Counts",
          "description": "Number of incidents the user has, broken down by status",
          "order": 11
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User name",
          "order": 3
        },
        "ou": {
          "type": "string",
          "title": "Ou",
          "description": "The OU the user belongs to",
          "order": 6
        },
        "suspended": {
          "type": "boolean",
          "title": "Suspended",
          "description": "Is the user suspended or not",
          "order": 5
        },
        "total_active_incidents": {
          "type": "number",
          "title": "Total Active Incidents",
          "description": "Total number of incidents that are in play (new or in progress)",
          "order": 7
        },
        "total_entities": {
          "type": "number",
          "title": "Total Entities",
          "description": "Total number of objects the user has",
          "order": 8
        },
        "total_incidents": {
          "type": "number",
          "title": "Total Incidents",
          "description": "Total number of incidents the user has",
          "order": 9
        },
        "vendor": {
          "$ref": "#/definitions/vendor",
          "title": "Vendor",
          "description": "Vendor name",
          "order": 2
        }
      },
      "definitions": {
        "vendor": {
          "type": "object",
          "title": "vendor",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the vendor. For example, google",
              "order": 1
            }
          }
        }
      }
    },
    "vendor": {
      "type": "object",
      "title": "vendor",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the vendor. For example, google",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
