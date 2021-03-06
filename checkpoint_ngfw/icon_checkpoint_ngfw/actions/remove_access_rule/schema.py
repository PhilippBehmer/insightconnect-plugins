# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove an access rule"


class Input:
    ACCESS_RULE_NAME = "access_rule_name"
    LAYER = "layer"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    

class RemoveAccessRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_rule_name": {
      "type": "string",
      "title": "Access Rule Name",
      "description": "Access rule name",
      "order": 1
    },
    "layer": {
      "type": "string",
      "title": "Layer",
      "description": "Layer",
      "default": "Network",
      "order": 2
    }
  },
  "required": [
    "access_rule_name",
    "layer"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAccessRuleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Remove operation status",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    }
  },
  "required": [
    "message",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
