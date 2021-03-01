# build order:
# You are given a list of projects and a list of dependencies (list of pairs of projects, where second project depends on first).
# All of a project's dependencies must be built before the project can be built.
# Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.
from typing import List

def build_order(projects: List, dependencies: List[tuple]) -> List:
    """
        ALGORITHM:
            - overall we want to topologically sort and check for cycles
            - topo sort requires that we
                * create directed graph from dependencies using a dict
                * do a DFS of the graph while keeping track of visitation by coloring
                    (white = unvisited, gray = visited 1x, black = finished)
                * reverse the order of "finishing time" i.e. order in which the nodes become black
            - we will ensure that no cycle exists by using a set: when node goes black, remove from set
            - refresh set each call to `dfs_visit`

        Example:
        Input:
            projects: [a, b, c, d, e, f]
            dependencies: [(a, d), (f, b), (b, d), (f, a), (d, c)]
        Return: [f, e, a, b, d, c]
    """
    def _create_graph(projects, dependencies) -> dict:
        """
            The direction of the edges in the directed graph is projectA -> projectB
            where projectB depends on projectA => projectA needs to be built before projectB

            We will use a dictionary to store the current color of each node (project) in the graph,
            which allows us to keep track of whether or not we have visited that node.
        """
        graph = {}
        for project in projects:
            graph[project] = []
            graph_coloring[project] = 'white'

        for dependency_tuple in dependencies:
            key, val = dependency_tuple
            graph[key].append(val)
        return graph

    def dfs(graph: dict, graph_coloring: dict):
        project_order = []
        for project in graph:
            set_of_seen_projects = set()
            if graph_coloring[project] == "white":
                dfs_visit(graph, graph_coloring, project, set_of_seen_projects, project_order)
        # reverse "finish time" in topo sort algorithm
        return project_order[::-1]

    def dfs_visit(graph: dict, graph_coloring: dict, project: str, set_of_seen_projects: set, project_order: List[str]):
        # color project that we are currently visiting gray
        graph_coloring[project] = "gray"
        set_of_seen_projects.add(project)
        # loop through dependencies and call dfs_visit if unvisited
        for dependent_project in graph[project]:
            if graph_coloring[dependent_project] == "white":
                dfs_visit(graph, graph_coloring, dependent_project, set_of_seen_projects, project_order)
            elif dependent_project in set_of_seen_projects:
                raise Exception('Cycle detected - no valid build order.')
        # project gets colored black once we've explored all of its avenues
        graph_coloring[project] = "black"
        set_of_seen_projects.remove(project)
        project_order.append(project)


    graph_coloring = {}
    graph = _create_graph(projects, dependencies)
    return dfs(graph, graph_coloring)


# Space and time comp both O(P + D)

if __name__ == "__main__":
    # projects = ['a', 'b', 'c', 'd', 'e', 'f']
    # dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    # print(build_order(projects, dependencies))

    # example with cycle
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('d', 'f')]
    print(build_order(projects, dependencies))

    # # example with fake cycle
    # projects = ['a', 'b', 'c', 'd', 'e', 'f']
    # dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('a', 'c')]
    # print(build_order(projects, dependencies))