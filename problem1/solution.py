
class SocialNetwork:
    def _init_(self):
        self.graph = defaultdict(set)

    def add_friendship(self, person1, person2):
        self.graph[person1].add(person2)
        self.graph[person2].add(person1)

    def find_friends(self, person):
        return self.graph[person]

    def find_common_friends(self, person1, person2):
        return self.graph[person1].intersection(self.graph[person2])

    def find_nth_connection(self, person1, person2):
        visited = {person1}
        queue = deque([(person1, 0)])  # (current_person, degree)

        while queue:
            current, degree = queue.popleft()
            if current == person2:
                return degree

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, degree + 1))

        return -1  # No connection found

# Example usage:
network = SocialNetwork()
network.add_friendship("Alice", "Bob")
network.add_friendship("Bob", "Janice")
network.add_friendship("Alice", "Carol")

print("Friends of Alice:", network.find_friends("Alice"))
print("Friends of Bob:", network.find_friends("Bob"))
print("Common friends of Alice and Bob:", network.find_common_friends("Alice", "Bob"))
print("Connection between Alice and Janice:", network.find_nth_connection("Alice", "Janice"))
