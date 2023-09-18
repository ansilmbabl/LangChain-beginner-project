# Fetching YouTube Video Recommendations with the `youtube` Method (5/5)

In this guide, we'll explore the `youtube` method within the `Health` class. This method is responsible for fetching YouTube video recommendations based on user input parameters, such as age, gender, and language. Let's break down the code step by step:

```python
def youtube(self):
    videos = self.youtube_vid.run(f"health tips for {self.sex} with age {self.age} in {self.language},3")
    urls = re.findall('watch\?v=[\w\-]+', videos)
    youtube_url = ["https://www.youtube.com/" + link for link in urls]
    return youtube_url
```

## Understanding the `youtube` Method

### Fetching YouTube Videos

- The `youtube` method begins by utilizing the `YouTubeSearchTool`, an instance of which was created during the `Health` class initialization. [[1]](https://python.langchain.com/docs/integrations/tools/youtube)
- It constructs a search query using user input parameters such as `sex`, `age`, and `language`. The query is formatted to search for "health tips" relevant to the user's input, limiting the results to the top 3 videos.

### Extracting Video URLs

- The method then uses `re.findall` to extract video URLs from the search results. The regular expression `'watch\?v=[\w\-]+'` is used to match YouTube video URLs. [[2]](https://docs.python.org/3/library/re.html)
- These URLs are stored in the `urls` variable, which contains a list of video links.

### Constructing YouTube URLs

- The `youtube_url` list comprehension takes each URL found and constructs a complete YouTube video URL by appending it to `"https://www.youtube.com/"`.
- This step ensures that you have direct links to the YouTube videos.
- Finally, the method returns the `youtube_url` list, which contains direct links to the YouTube videos that match the user's input criteria.

## Conclusion

The `youtube` method in the `Health` class is a crucial component responsible for fetching YouTube video recommendations tailored to the user's age, gender, and language preferences. By understanding how this method works, you'll see how the project provides users with relevant video content to complement the health tips.

In this guide, we've covered how the `youtube` method operates, but if you have any further questions or need to explore other aspects of the project, please feel free to ask.