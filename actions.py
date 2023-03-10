# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionCheckSong(Action):

    def name(self) -> Text:

        return "action_check_song"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("reached check song method")
        user_choice = tracker.get_slot('song_name')
        dispatcher.utter_message(text = f"You chose the song {user_choice}")

        return []

class ActionCheckLocation(Action):

    def name(self) -> Text:

        return "action_check_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("reached check location method")
        user_choice = tracker.get_slot('location_name')
        dispatcher.utter_message(text = f"You chose the location {user_choice}")

        return []

class ActionCheckContact(Action):

    def name(self) -> Text:

        return "action_check_contact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("reached check contact method")
        user_choice = tracker.get_slot('contact_name')
        dispatcher.utter_message(text = f"You chose the person {user_choice}")

        return []

class ConfirmSong(Action):

    def name(self) -> Text:

        return "action_confirm_song"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_conf = tracker.get_slot('input_confirmation')
        print(tracker.latest_message['intent'].get('name'))
        print(user_conf)
        print(type(user_conf))
        # if tracker.latest_message['intent'].get('name') == 'confirm_input':
        #     print("reached")
        #     return [FollowupAction("action_set_api_slot_music")]
        resp_list = ['yes', 'YES', 'yess', 'yessir']
        print(type(resp_list[0]))

        if user_conf in resp_list :
            print("reached")
            return [FollowupAction("action_call_spotify_api")]

class ConfirmLocation(Action):

    def name(self) -> Text:

        return "action_confirm_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_conf = tracker.get_slot('input_confirmation')
        print(tracker.latest_message['intent'].get('name'))
        print(user_conf)
        print(type(user_conf))
        # if tracker.latest_message['intent'].get('name') == 'confirm_input':
        #     print("reached")
        #     return [FollowupAction("action_set_api_slot_music")]
        resp_list = ['yes', 'YES', 'yess', 'yessir']
        print(type(resp_list[0]))

        if user_conf in resp_list :
            print("reached")
            return [FollowupAction("action_call_maps_api")]

class ConfirmContact(Action):

    def name(self) -> Text:

        return "action_confirm_contact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_conf = tracker.get_slot('input_confirmation')
        print(tracker.latest_message['intent'].get('name'))
        print(user_conf)
        print(type(user_conf))
        # if tracker.latest_message['intent'].get('name') == 'confirm_input':
        #     print("reached")
        #     return [FollowupAction("action_set_api_slot_music")]
        resp_list = ['yes', 'YES', 'yess', 'yessir']
        print(type(resp_list[0]))

        if user_conf in resp_list :
            print("reached")
            return [FollowupAction("action_call_contacts_api")]


class ActionCallSpotifyAPI(Action):

    def name(self) -> Text:

        return "action_call_spotify_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_choice = tracker.get_slot("song_name")
        print(f"Now calling the Spotify API to play the song {user_choice}")
        dispatcher.utter_message(f"I will now call the Spotify API to play the song {user_choice}")

        return []


class ActionCallMapsAPI(Action):

    def name(self) -> Text:

        return "action_call_maps_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_choice = tracker.get_slot("location_name")
        print(f"Now calling the Maps API to play the song {user_choice}")
        dispatcher.utter_message(f"Now calling the Maps API to find the location {user_choice}")

        return []


class ActionCallContactsAPI(Action):

    def name(self) -> Text:

        return "action_call_contacts_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_choice = tracker.get_slot("contact_name")

        # if user_choice in contact_list:
        #     print(f"Now calling the Contacts API to call the person {user_choice}")
        #     dispatcher.utter_message(f"Now calling the Contacts API to call the person {user_choice}")
        # else:
        #     dispatcher.utter_message("The person you are trying to search is not in your contacts")

        print(f"Now calling the Contacts API to call the person {user_choice}")
        dispatcher.utter_message(f"Now calling the Contacts API to call the person {user_choice}")

        return []