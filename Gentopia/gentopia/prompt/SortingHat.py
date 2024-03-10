from gentopia.prompt import PromptTemplate

SortingHatPrompt = PromptTemplate(
    input_variables=["user_traits"],
    template=
    """Welcome to Hogwarts ! Delighted to have you here. Foe the curious minds, NO! you won't be learning how to turn your homework into a niffler.
    Firstly, Discover your Hogwarts house based on your traits! Rate yourself on the following traits from 1 to 10, where 1 is low and 10 is high.
    
    Trait: Curiosity
    Rating: {user_traits['Curiosity']}
    
    Trait: Friendship
    Rating: {user_traits['Friendship']}
    
    #Thought: Analyzing your traits to determine your Hogwarts house.
    Action: analyze_traits_and_sort_house
    
    Action Input: {user_traits}
    
    Observation: Sorting in progress...
    
    #Thought: I now have a suggestion for your Hogwarts house!
    Final Answer: You might belong to {house_suggestion}
    """
)
