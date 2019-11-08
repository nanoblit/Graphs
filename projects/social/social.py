import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for userId in range(numUsers):
            self.addUser("Sam")
        # Create friendships
        random_friendships = []
        for user in range(1, numUsers + 1):
            for user2 in range(1, numUsers + 1):
                if user != user2:
                    random_friendships.append((user, user2))
        random.shuffle(random_friendships)
        numFriendships = avgFriendships * numUsers
        for _ in range(numFriendships):
            friendship = random_friendships.pop()
            if (friendship[0] < friendship[1]):
                self.addFriendship(friendship[0], friendship[1])
            else:
                numFriendships += 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = set()
        # Make a queue
        q = Queue()
        # Make paths dictionary
        paths = {}
        # enqueue userID
        q.enqueue(userID)
        # add userID to visited
        visited.add(userID)
        # make path with userID key and [userID] value
        paths[userID] = [userID]
        # while queue not empty
        while q.size() > 0:
            # user = dequeued user
            user = q.dequeue()
            # for friend in user's frinds
            for friend in self.friendships[user]:
                # if visited
                if friend in visited:
                    # continue
                    continue
                # add friend to visited
                visited.add(friend)
                # enqueue friend
                q.enqueue(friend)
                # add friend to new path based on user's path and save it with friend key
                newPath = paths[user][:]
                newPath.append(friend)
                paths[friend] = newPath
        # return paths
        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
