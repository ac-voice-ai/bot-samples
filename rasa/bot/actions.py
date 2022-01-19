# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is tal's rasa bot"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ConversationPaused, ConversationResumed, ReminderScheduled, ReminderCancelled, SlotSet
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


state = {
    "responses": {
        "basicTalk_stream1": "and hello to you too",
        "basicTalk_stream2": "Many people want to work with clouds but everybody works with windows",
    }
}


class ActionConnector(Action):
    def resume_listening(self):
        print("resume listening.....")
        state["is_bot_available"] = True

    def name(self) -> Text:
        return "action_connector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        print("----------------------------------")
        print("intent: " + str(intent))
        print("----------------------------------")

        response = state["responses"].get(intent, None)
        if response:
            dispatcher.utter_message(text=response)
            return []
        elif intent == "disconnect":
            dispatcher.utter_message(text="action: disconnect")
            dispatcher.utter_message(json_message={
                "type": "event",
                "name": "hangup",
                "activityParams": {
                    "hangupReason": "conversationCompleted"
                }
            })
            return []
        elif intent == "transfer":
            dispatcher.utter_message(json_message={
                "type": "event",
                "name": "transfer"
            })
            return []

        else:
            dispatcher.utter_message(text="dont know what to do with your request")
            return []
