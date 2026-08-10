def process_video_views(titles, view_counts):
    return [(title, round(views, -3)) for title, views in zip(titles, view_counts)]

video_titles = ["Python Basics Tutorial", "Vehicle Assembly POV", "Perfume Review"]
views = [12450, 89800, 3100]

output = process_video_views(video_titles, views)
print(output)