class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        if photos_count % 4 == 0:
            return cls(int(photos_count / 4))
        return cls(int(photos_count / 4 + 1))

    def add_photo(self, label):
        for index, row in enumerate(self.photos):
            if len(row) < 4:
                row.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(row)}"
        return "No more free slots"

    def display(self):
        new_line = '\n'
        separator = "-----------"
        pages_frames = [["[]" for _ in row] for row in self.photos]
        pages_frames_view = [" ".join(row) for row in pages_frames]
        display = [f"{separator}{new_line}{page}" for page in pages_frames_view]
        return f"{new_line.join(display)}{new_line}{separator}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
