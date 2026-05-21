
import wikipedia

def get_wikipedia_summary(query):
    try:
        # Set language (optional)
        wikipedia.set_lang("en")

        # Get summary for the given query
        summary = wikipedia.summary(query)

        # Limit the summary to two lines
        summary_lines = summary.split('\n')
        truncated_summary = '\n'.join(summary_lines[:2])

        return truncated_summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation (multiple matching pages)
        return "i don't know"
    except wikipedia.exceptions.PageError:
        # Handle page not found error
        return "i don't know"
    except Exception as e:
        # Handle other errors
        return "i don't know"

