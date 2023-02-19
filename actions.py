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

# class ActionPlaySong(Action):

#     def name(self) -> Text:

#         return "action_play_song"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text = "I will now send GET request and call the spotify API")

#         return []

class ActionSetAPISlot_Music(Action):

    def name(self) -> Text:
        
        return "action_set_api_slot_music"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("reached set api slot func")
        return[SlotSet("API_num", "one")]

class ActionSetAPISlot_Location(Action):

    def name(self) -> Text:
        
        return "action_set_api_slot_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("reached set api location slot func")
        return[SlotSet("API_num", "two")]

class ActionSetAPISlot_Contacts(Action):

    def name(self) -> Text:
        
        return "action_set_api_slot_contact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("reached set api contact slot func")
        return[SlotSet("API_num", "three")]

class ActionCheckSong(Action):

    def name(self) -> Text:

        return "action_check_song"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot('song_name')
        dispatcher.utter_message(text = f"You chose the song {user_choice}")

        return []

class ActionCheckLocation(Action):

    def name(self) -> Text:

        return "action_check_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot('location_name')
        dispatcher.utter_message(text = f"You chose the location {user_choice}")

        return []

class ActionCheckContact(Action):

    def name(self) -> Text:

        return "action_check_contact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot('contact_name')
        dispatcher.utter_message(text = f"You chose the song {user_choice}")

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
            return [FollowupAction("action_set_api_slot_music")]

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
            return [FollowupAction("action_set_api_slot_location")]

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
            return [FollowupAction("action_set_api_slot_contact")]

class ActionCallAPI(Action):

    def name(self) -> Text:

        return "action_call_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("reached in api call func")
        if(tracker.get_slot('API_num') == 'one'):
            dispatcher.utter_message(text = "I will now send GET request and call the SpotifyAPI")
        elif(tracker.get_slot('API_num') == 'two'):
            dispatcher.utter_message(text = "I will now send GET request and call the GoogleMaps API")
        elif(tracker.get_slot('API_num') == 'three'):
            dispatcher.utter_message(text = "I will now send GET request and call the Contacts API")
        else:
            dispatcher.utter_message(text = "No value was set in the API num slot")

        return []
        

# class ActionOpenMaps(Action):

#     def name(self) -> Text:

#         return "action_open_maps"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text = "I will now send GET request and call the GoogleMaps API")

#         return []

# class ActionSetAPISlot_Maps(Action):

#     def name(self) -> Text:
        
#         return "action_set_api_slot_maps"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         return [SlotSet("API_num", "two")]


# class ActionCheckLocation(Action):

#     def name(self) -> Text:

#         return "action_check_location"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_choice = tracker.get_slot('location_name')
#         dispatcher.utter_message(text = f"You chose the location {user_choice}")
#         dispatcher.utter_message(text = "Was this the location you wanted?")


#         return [FollowupAction("action_set_api_slot_maps")]

# class ActionSetAPISlot_Contacts(Action):

#     def name(self) -> Text:
        
#         return "action_set_api_slot_contacts"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         return [SlotSet("API_num", "three")]

# class ActionCheckContacts(Action):

#     def name(self) -> Text:

#         return "action_check_contacts"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_choice = tracker.get_slot('contact_name')
#         dispatcher.utter_message(text = f"You chose the location {user_choice}")
#         dispatcher.utter_message(text = "Was this the person you wanted?")


#         return [FollowupAction("action_set_api_slot_contact")]



# class ValidateSimpleMusicForm(FormValidationAction):
    
#     def name(self) -> Text:
#         return "validate_simple_music_form"

#     def validate_song_name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         user_choice = tracker.get_slot('song_name')

#         if user_choice in range(1000, 10000):
#             dispatcher.utter_message(text = "You have entered a phone number, please request a song")
        
#         dispatcher.utter_message(text = f"You have chosen the song {user_choice}")

#         user_conf = tracker.get_slot('song_confirmation')
#         if user_conf == 'yes':
#             return [FollowupAction('action_play_song')]

#         return []
        
        # user_conf = tracker.get_slot('song_confirmation')

        # if user_conf == 'yes' | 'Yes' | 'YES':

        # return [FollowupAction("action_play_song")]
        
        # if user_conf == 'no':
            
        #     dispatcher.utter_message(text = f"Oops! Seems like I heard you wrong! Please repeat the song name!")

        #     return [FollowupAction("validate_simple_music_form")]

