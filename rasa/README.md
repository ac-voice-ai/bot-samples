Rasa bot example
================

This is an example bot for use with AudioCodes channel.

Configuration
-------------

credentials.yml:
```yaml
rasa_audiocodes.AudiocodesInput:
  token: "example_token"
  websocket_is_on: False
```

The `token` must match the token you set on the VAIC when configuring the
provider for the rasa bot.

If `websocket_is_on == True`, bot replies are sent over websocket instead of HTTP replies.

Example: This would be the matching configuration on the VAIC config file

```json
{
  "name": "rasa_provider",
  "type": "ac-api",
  "botURL": "http://<YOUR IP>:5006/webhooks/audiocodes/webhook",
  "credentials": {
    "token": "example_token"
  }
}
```

Running
-------
docker-compose up -d
