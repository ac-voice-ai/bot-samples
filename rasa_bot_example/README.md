# RASA bot AUDC example code
This folder holds an example of implemanting the AUDC RASA bot.\
This bot supports a few fuctionalitys to get you started with developing your down bot integrated with the VAIC.\
This bot supports the following functionality examples:
1. transfer call
2. Disconnect call
3. respond to the words "short reply"

# Working with or without websocket:
## Summary
Generally when the websocket_is_on == True in the credentials file weather
like in the below example we send all of the bot messages over websocket instead of http.\
The below example shows you how to configure this feature.
credentials.yml file example below:
```yaml
rasa_audiocodes.AudiocodesInput:
  token: "example_token"
  websocket_is_on: True
```
# Credentials
## credentials.yml file example below

```yaml
rasa_audiocodes.AudiocodesInput:
  token: "example_token"
  websocket_is_on: False
```
This token must match the token you set on the VAIC when configuring the provider for the rasa bot
## Example: This would be the matching configuration on the VAIC config file
```json
    {
      "name": "rasa_provider",
      "type": "ac-api",
      "botURL": "http://<YOUR IP>:5006/webhooks/audiocodes/webhook",
      "credentials": {
        "token": "example_credentials"
      },
    }
```
# How to run
```bash
docker-compose -f docker-compose.you -d 
```