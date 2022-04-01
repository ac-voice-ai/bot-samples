# This file contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these actions:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ActionConnector(Action):
    def name(self) -> Text:
        return "action_connector"

    @staticmethod
    def get_metadata(tracker: Tracker):
        message = tracker.latest_message
        if 'metadata' in message:
            obj = message
        else:
            obj = next(ev for ev in tracker.events if ev['event'] == 'session_started')
        try:
            return obj['metadata']
        except Exception as e:
            logger.error(f"Failed:", exc_info=e)
            logger.info(vars(tracker))
            return None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message
        intent = message['intent'].get('name')
        logger.info(f"Intent: {intent}")

        if intent == "vaig_event_start":
            metadata = self.get_metadata(tracker)
            name = metadata['callerDisplayName'] if metadata else ''
            dispatcher.utter_message(text=f'Hi {name}, this is AudioCodes Rasa bot')
            return [SlotSet("name", name)]

        elif intent == "disconnect":
            dispatcher.utter_message(text="action: disconnect")
            dispatcher.utter_custom_json({
                "type": "event",
                "name": "hangup",
                "activityParams": {
                    "hangupReason": "conversationCompleted"
                }
            })
            return []

        elif intent == "transfer":
            dispatcher.utter_message(text="transferring call")
            dispatcher.utter_custom_json({
                "type": "event",
                "name": "transfer",
                "activityParams": {
                    "transferTarget": "tel:+15551212"
                }
            })
            return []

        elif intent == "play":
            dispatcher.utter_custom_json({
                "type": "event",
                "name": "playUrl",
                "activityParams": {
                    "playUrlUrl": "http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/Samples/Goldwave/addf8-mulaw-GW.wav",
                    "playUrlMediaFormat": "wav/mulaw"
                }
            })
            return []

        else:
            dispatcher.utter_message(text="dont know what to do with your request")
            return []
