def create_youtube_video (title,description):
    youtubevideo = {"title":title , "description":description,"likes":100, "dislike":0,"comments":{}}

def like (youtubevideo):  
	if "likes" in youtubevideo: 
		youtubevideo ["likes"] += 1 
		return youtubevideo

def dislike (youtubevideo):
	if "dislike" in youtubevideo:
		youtubevideo ["dislike"] += 1

def add_comment(youtubevideo ,username , comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

	print(create_youtube_video) 
	