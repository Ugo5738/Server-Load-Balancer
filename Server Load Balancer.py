import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        if connection_load > 10:
            connection_load -= 1
        # Adding the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Removing the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Adding up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


server = Server()
server.add_connection("192.168.1.1")
print(server.load())


server.close_connection("192.168.1.1")
print(server.load())


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Adding the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Adding the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Finding out the right server
        for server in self.servers:
            if connection_id in server.connections:
                # Closing the connection on the server
                server.close_connection(connection_id)
                # Removing the connection from the load balancer
                del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Summing the load of each server and divide by the amount of servers
        total_load = 0
        for server in self.servers:
            total_load += server.load()
            average_load = total_load / len(self.servers)
        return average_load

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            new_server = Server()
            self.servers.append(new_server)
            new_server.add_connection(connection)

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())


l.servers.append(Server())
print(l.avg_load())


l.close_connection("fdca:83d2::f20d")
print(l.avg_load())


for connection in range(100):
    l.add_connection(connection)
print(l)


print(l.avg_load())