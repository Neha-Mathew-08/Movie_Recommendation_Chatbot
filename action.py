from rasa_sdk import Action, Tracker   #Action class
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, Text, Dict, List
import random

class ActionRecommendMovie(Action):  #Action class has two methods

    def name(self) -> str:   #name method to return the name of the action
        return "action_recommend_movie"

    def run(self, dispatcher: CollectingDispatcher,     #run method, where all logics are defined
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        genre = tracker.get_slot('genre')

        # Predefined dictionary of movies by genre
        movies_dict = {
            "action": ["Die Hard", "The Dark Knight", "Inception"],
            "comedy": ["Superbad", "The Hangover", "Bridesmaids"],
            "crime": ["Zodiac", "Seven", "The Snowman"],
            "romance": ["La la land", "The Notebook","Notting Hill"],
        }

        # Checking if the genre is in the movies_dict keys
        if genre in movies_dict:
            movies = movies_dict[genre]

            # Selects a random movie from the list
            recommended_movie = random.choice(movies)
        
            dispatcher.utter_message(text=f"I recommend you watch {recommended_movie}.")
        else:
            dispatcher.utter_message(text=f"I'm sorry, I couldn't find any movies in the {genre} genre.")

        return []
    
