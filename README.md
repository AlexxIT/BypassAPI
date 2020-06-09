# BypassAPI for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Disable authentication for Home Assistant [REST API](https://developers.home-assistant.io/docs/api/rest/). Useful when headless installation is used (disabled [frontend](https://www.home-assistant.io/integrations/frontend/) and [default_config](https://www.home-assistant.io/integrations/default_config/)).

## Config

**Only REST API**

```yaml
#default_config: 

bypass_api:

sonoff:
  username: mymail@gmail.com
  password: mypassword

yandex_station:
  username: mymail@yandex.ru
  password: mypassword
```

**REST API and WebSockets**

e.g. for Node-RED - use any token (not empty)!

```yaml
auth:
bypass_api:
websocket_api:
```

## Usage

```shell script
curl --request POST \
  --url http://192.168.1.123:8123/api/services/homeassistant/turn_on \
  --header 'content-type: application/json' \
  --data '{"entity_id": "switch.sonoff_mini"}'
```

```shell script
curl --request POST \
  --url http://192.168.1.123:8123/api/services/media_player/play_media \
  --header 'content-type: application/json' \
  --data '{
	"entity_id": "media_player.yandex_station_mini",
	"media_content_id": "How are you?",
	"media_content_type": "text"
}'
```