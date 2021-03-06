# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieves logs from InsightOps service"


class Input:
    pass

class Output:
    LOGS = "logs"
    

class QueryLogsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryLogsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "logs": {
      "type": "array",
      "title": "Logs Data",
      "description": "Logs",
      "items": {
        "$ref": "#/definitions/logs"
      },
      "order": 1
    }
  },
  "required": [
    "logs"
  ],
  "definitions": {
    "links": {
      "type": "object",
      "title": "links",
      "properties": {
        "href": {
          "type": "string",
          "title": "href",
          "description": "Hypertext Reference",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "rel",
          "description": "The relationship between the current document and the linked document",
          "order": 2
        }
      }
    },
    "logs": {
      "type": "object",
      "title": "logs",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Logsets ID",
          "order": 1
        },
        "logsets_info": {
          "type": "array",
          "title": "Logsets Information",
          "description": "Information about logsets",
          "items": {
            "$ref": "#/definitions/logsets_info"
          },
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of logsets",
          "order": 3
        },
        "source_type": {
          "type": "string",
          "title": "Source Type",
          "description": "Source type",
          "order": 4
        },
        "structures": {
          "type": "array",
          "title": "Structures",
          "description": "An array of log structures",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "token_seed": {
          "type": "string",
          "title": "Token Seed",
          "description": "Seed of token",
          "order": 6
        },
        "tokens": {
          "type": "array",
          "title": "Tokens",
          "description": "An array of Tokens",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "user_data": {
          "$ref": "#/definitions/user_data",
          "title": "User Data",
          "description": "Logentry Data",
          "order": 8
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "href": {
              "type": "string",
              "title": "href",
              "description": "Hypertext Reference",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "rel",
              "description": "The relationship between the current document and the linked document",
              "order": 2
            }
          }
        },
        "logsets_info": {
          "type": "object",
          "title": "logsets_info",
          "properties": {
            "id": {
              "type": "string",
              "title": "Logsets ID",
              "description": "ID associated with the Logsets",
              "order": 1
            },
            "links": {
              "type": "array",
              "title": "Link",
              "description": "Link to the logs logsets ID within InsightOps",
              "items": {
                "$ref": "#/definitions/links"
              },
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the log",
              "order": 3
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "href",
                  "description": "Hypertext Reference",
                  "order": 1
                },
                "rel": {
                  "type": "string",
                  "title": "rel",
                  "description": "The relationship between the current document and the linked document",
                  "order": 2
                }
              }
            }
          }
        },
        "user_data": {
          "type": "object",
          "title": "user_data",
          "properties": {
            "le_agent_filename": {
              "type": "string",
              "title": "LE Agent Filename",
              "description": "Logentry Agent Filename",
              "order": 1
            },
            "le_agent_follow": {
              "type": "string",
              "title": "LE Agent Follow",
              "description": "Logentry Agent Follow",
              "order": 2
            }
          }
        }
      }
    },
    "logsets_info": {
      "type": "object",
      "title": "logsets_info",
      "properties": {
        "id": {
          "type": "string",
          "title": "Logsets ID",
          "description": "ID associated with the Logsets",
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Link",
          "description": "Link to the logs logsets ID within InsightOps",
          "items": {
            "$ref": "#/definitions/links"
          },
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the log",
          "order": 3
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "href": {
              "type": "string",
              "title": "href",
              "description": "Hypertext Reference",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "rel",
              "description": "The relationship between the current document and the linked document",
              "order": 2
            }
          }
        }
      }
    },
    "user_data": {
      "type": "object",
      "title": "user_data",
      "properties": {
        "le_agent_filename": {
          "type": "string",
          "title": "LE Agent Filename",
          "description": "Logentry Agent Filename",
          "order": 1
        },
        "le_agent_follow": {
          "type": "string",
          "title": "LE Agent Follow",
          "description": "Logentry Agent Follow",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
