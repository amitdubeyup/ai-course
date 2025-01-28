import instaloader

# Function to download public images from an Instagram profile
def download_instagram_images(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download all posts (including images)
        for post in profile.get_posts():
            if not post.is_video:  # Skip videos, only download images
                loader.download_post(post, target=f"{username}_images")
                print(f"Downloaded: {post.url}")

        print(f"All images from @{username} have been downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'grapeot' with the target Instagram username
username = "grapeot"
download_instagram_images(username)