#!/home/cicada/.gemini/extensions/youtube/venv/bin/python
import argparse
import json
import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def search_youtube(query):
    """
    Performs a search on YouTube and returns a list of video results.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    # URL encode the query
    query = requests.utils.quote(query)
    url = f"https://www.youtube.com/results?search_query={query}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    # This is a bit fragile as YouTube's structure can change.
    # We look for script tags containing video data.
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.string and 'var ytInitialData' in script.string:
            # Extract the JSON data
            json_text = script.string.split(' = ')[1]
            # The JSON might end with a semicolon
            if json_text.endswith(';'):
                json_text = json_text[:-1]
            
            try:
                data = json.loads(json_text)
                contents = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
                
                for item in contents:
                    if 'videoRenderer' in item:
                        video_data = item['videoRenderer']
                        video_id = video_data.get('videoId')
                        title = video_data.get('title', {}).get('runs', [{}])[0].get('text')
                        description_snippet = video_data.get('descriptionSnippet', {}).get('runs', [{}])[0].get('text')
                        
                        if video_id and title:
                            results.append({
                                "title": title,
                                "url": f"https://www.youtube.com/watch?v={video_id}",
                                "description": description_snippet
                            })
                # We found the data, no need to check other script tags
                break
            except (KeyError, IndexError, json.JSONDecodeError) as e:
                # This can happen if the structure of the page is not as expected.
                # Continue to the next script tag.
                continue

    print(json.dumps(results, indent=2))


def get_transcript(video_url):
    """
    Fetches and prints the transcript for a given YouTube video URL.
    """
    video_id_match = re.search(r"v=([^&]+)", video_url)
    if not video_id_match:
        print("Error: Could not extract video ID from URL.")
        return

    video_id = video_id_match.group(1)

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        full_transcript = " ".join([snippet.text for snippet in transcript.snippets])
        print(full_transcript)
    except Exception as e:
        print(f"Error fetching transcript: {e}")

def main():
    parser = argparse.ArgumentParser(description="A YouTube search and transcript tool.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search command
    search_parser = subparsers.add_parser("search", help="Search YouTube for videos.")
    search_parser.add_argument("query", type=str, help="The search query.")

    # Transcript command
    transcript_parser = subparsers.add_parser("transcript", help="Get the transcript for a YouTube video.")
    transcript_parser.add_argument("url", type=str, help="The URL of the YouTube video.")

    args = parser.parse_args()

    if args.command == "search":
        search_youtube(args.query)
    elif args.command == "transcript":
        get_transcript(args.url)

if __name__ == "__main__":
    main()
