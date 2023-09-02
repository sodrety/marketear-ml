import openai
import json
import os
openai.api_key = os.environ.get("GPT_KEY")



def sentiment(prompt):
    augmented_prompt = f"""Analyze and extract the sentiment and emotion of the given text below. The sentiment can be positive, negative, neutral. The emotion can be angry, happy, sad, scared, tender, undefined. Desired format is array : Sentiment: Emotion: 

Text: {prompt}"""
    summary = openai.Completion.create(
            model="davinci:ft-personal-2023-07-16-09-53-16", 
            prompt=augmented_prompt,
            # temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    
    # return summary
    stripped = summary.strip()
    final = stripped.split()
    sentiments = final[final.index("Sentiment:") + 1]
    emotion = final[final.index("Emotion:") + 1]

    return sentiments, emotion
    


def main():
    print('Query: ')
    print("------------------------")
    new_question = input()
    result = sentiment(new_question)
    print("------------------------")
    print("Result: ")
    
    text = json.dumps(result)

    list_of_words = text.split()
    sentiments = list_of_words[list_of_words.index("Sentiment:") + 1]
    emotion = list_of_words[list_of_words.index("Emotion:") + 1]

    return [sentiments, emotion]


if __name__ == "__main__":
    main()
