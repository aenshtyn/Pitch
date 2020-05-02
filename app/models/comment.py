class Comment:

    all_comments = []

    def __init__(self,pitch_id,title,comment):
        self.picth_id = pitch_id
        self.title = title
        self.comment = comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()


    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.pitch_id == id:
                response.append(comment)

        return response    
