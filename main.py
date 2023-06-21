import instaloader

def download_instagram_video(url):
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        video_url = post.url
        loader.download_video(video_url, target=f"{post.owner_username}_{post.shortcode}")
        print("Video downloaded successfully!")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {str(e)}")

# Example usage
instagram_url = input("Enter video link: ")

download_instagram_video(instagram_url)
