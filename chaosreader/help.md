# Description

[Chaosreader](http://chaosreader.sourceforge.net/) is a tool to trace sessions and fetch application data from snoop or tcpdump logs.The plugin is used to trace sessions and fetch application data from snoop or tcpdump logs.

# Key Features

* Analyze captured network traffic

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Run

This action is used to run Chaosreader on a given capture (PCAP or Snoop) file.
Session details are provided in the output, as well as the extracted files in a `bytes array`.
Specific file traffic/file types can be excluded.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dump|bytes|None|True|Base64 encoded PCAP or snoop file|None|
|exclude|string|None|False|Exclude traffic/files|['None', 'Info', 'Raw', 'TCP', 'UDP', 'ICMP']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ethernet_count|[]count|False|List of ethernet types and their count|
|file_count|integer|False|Number of files extracted|
|files|[]bytes|False|Extracted files|
|ip_count|[]count|False|List of IPs and their count|
|proto_count|[]count|False|List of IP protocols and their count|
|sessions|[]string|False|List of sessions found in traffic|
|tcp_count|[]count|False|List of TCP ports and their count|
|udp_count|[]count|False|List of UDP ports and their count|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.4 - Fix set options to exclude | Upgrade code to new version of chaos reader
* 1.0.3 - Changed 2 spaces to 4 spaces | Changed bare strings in params.get and output to static fields from schema | Removed unnecessarily comments and variables | Changed `Exception` to `PluginException` | Changed deprecated `decodestring` to `decodebytes`
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Chaosreader](http://chaosreader.sourceforge.net/)

