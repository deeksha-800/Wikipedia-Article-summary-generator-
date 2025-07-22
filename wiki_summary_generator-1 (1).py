import wikipedia
import pyttsx3

def generate_summary(topic, num_sentences=5):
    try:
        wikipedia.set_lang("en")
        search_results = wikipedia.search(topic)
        if not search_results:
            return None, "No results found for your query."

        page_title = search_results[0]
        summary = wikipedia.summary(page_title, sentences=num_sentences)
        return page_title, summary

    except wikipedia.exceptions.DisambiguationError as e:
        options = ', '.join(e.options[:5])
        return None, f"Disambiguation Error: Your query is ambiguous. Did you mean one of these?\n{options}..."

    except wikipedia.exceptions.PageError:
        return None, "Page not found. Try a different topic."

    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("🔍 Wikipedia Article Summary Generator with Voice")
    topic = input("Enter a topic to search: ")
    num_sent = input("How many sentences should the summary have? (default 5): ")
    if not num_sent.isdigit():
        num_sent = 5
    else:
        num_sent = int(num_sent)

    title, summary = generate_summary(topic, num_sent)
    if title:
        print(f"\n📘 Topic: {title}\n\n{summary}\n")
        print("🔊 Reading the summary aloud...")
        speak_text(summary)
    else:
        print(summary)
        speak_text(summary)
