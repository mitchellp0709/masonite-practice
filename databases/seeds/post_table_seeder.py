"""PostTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Post import Post

class PostTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Post.create({"title":"abcd","body":"fuhqiquhwef"})
        Post.create({"title":"efgh","body":"ijkl"})
        Post.create({"title":"mnop","body":"qrst"})
