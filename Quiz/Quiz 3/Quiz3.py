"""
Consider the following Twitter post, and define a class to represent the elements given in the following post. 

Hint: Identify properties and methods. Then create an implementation of the class. Create three posts and display them. (You can skip image part). Submit the code and screenshots of the program execution.

The post is as follows: Some west end toronto residents say raw sewage and subway noise have increased on their street now that the city has finally removed a boring machine that was stuck underground for 19 months
"""

import random

class TwitterPost:
    def __init__(self, username, post, date, retweets=0, likes=0,comments=0,reach = 0):
        self.username = username
        self.post = post
        self.date = date
        self.retweets = retweets
        self.likes = likes
        self.comments = comments
        self.reach = reach
    
    #Getter methods
    def getUsername(self):
        return self.username
    
    def getPost(self):
        return self.post
    
    def getDate(self):
        return self.date
    
    def getRetweets(self):
        return self.retweets
    
    def getLikes(self):
        return self.likes
    
    def getComments(self):
        return self.comments
    
    def getReach(self):
        return self.reach
    
    #setter methods
    def setUsername(self, username):
        self.username = username
        
    def setPost(self, post):
        self.post = post
        
    def setDate(self, date):
        self.date = date
        
    def setRetweets(self, retweets):
        self.retweets = retweets
    
    def setLikes(self, likes):
        self.likes = likes
    
    def setComments(self, comments):
        self.comments = comments
    
    def setReach(self, reach):
        self.reach = reach
        
        # function for displaying the post
    def displayPost(self):
        print("-" * 48)
        print(f"Username: {self.username}")
        print(f"Post: {self.post}, Date: {self.date}")
        print(f"Retweets: {self.retweets}, Likes: {self.likes}, Comments: {self.comments}, Reach: {self.reach}")
        print("-" * 48)  
    
    #function for updating the posts stats, with a random int from 0 to 10
    def updatePost(self):
        self.likes += random.randint(0,10)
        self.retweets += random.randint(0,10)
        self.comments += random.randint(0,10)
        self.reach += random.randint(0,10)
    
    
        
post1 = TwitterPost(input("Enter username for post 1: "), input("Enter post 1: "), "November 17, 2023")
post2 = TwitterPost(input("Enter username for post 2: "), input("Enter post 2: "), "November 17, 2023")
post3 = TwitterPost(input("Enter username for post 3: "), input("Enter post 3: "), "November 17, 2023")

for post in [post1, post2, post3]:
    post.updatePost()
    post.displayPost()