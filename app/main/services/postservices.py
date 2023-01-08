from app.main.models.post import Post
from datetime import datetime
from app.main.db import session

class post_service():
    
    def create_post(self, title: str, content: str, username: str, image: str):
        
        if image=='':
            post = Post(title=title, content=content, username=username)
        
        else:
            post = Post(title=title, content=content, username=username, image=image)

        session.add(post)
        session.commit()

    def update_post(self, post_title: str, post_content: str, post_id: int, image: str):
        post_to_update = session.query(Post).get(post_id)

        if image != '':
            post_to_update.image = image

        post_to_update.title = post_title
        post_to_update.content = post_content
        post_to_update.date_updated = datetime.utcnow()
       
        session.commit()
       
        
    def delete_post(self, post_id: int):
        post_to_delete = session.query(Post).get(post_id)

        session.delete(post_to_delete)
        session.commit()

        
# def count(post_id):
#     post = session.query(Post).get(post_id)

#     post.no_of_views = post.no_of_views + 1

#     session.commit()