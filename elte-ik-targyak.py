from pyvis.network import Network

if __name__ == "__main__":
    net = Network()
    course_list_1 = ['Matematikai-alapok-GY', 'Programozas-EA-GY', 'Imperativ-programozas-EA-GY', 'Szamitogepes-rendszerek-EA-GY']
    course_list_2 = ['Web-fejlesztes-Ea-Gy', 'Algoritmusok-es-adatszerkezetek-I-Ea', 'Objektumelvu-programozas-Ea-Gy',
                     'Algoritmusok-es-adatszerkezetek-I-Gy', 'Diszkret-matematika-I-Ea', 'Diszkret-matematika-I-Gy', 'Analizis-I-Gy', 'Analizis-I-Ea']
    course_list_3 = ['Programozasi-nyelvek-Ea-Gy', 'Algoritmusok-es-adatszerkezetek-II-Gy', 'Algoritmusok-es-adatszerkezetek-II-Ea',
                     'Programozasi-nyelvek-I-Ea-Gy-C++', 'Kozgazdasagi-es-jogi-ismeretek-Ea', 'Funkcionalis-programozas-Ea-Gy',
                     'Programozasi-nyelvek-II-Ea-Gy-Java', 'Analizis-II-Ea', 'Analizis-II-Gy']
    course_list_4 = ['Konkurrens-programozas-Ea-Gy', 'Operacios-rendszerek-Ea-Gy', 'Webprogramozas-Ea-Gy', 'A-szamitaselmelet-alapjai-I-Ea',
                     'A-szamitaselmelet-alapjai-I-Ea', 'Programozasi-technologia-Ea-Gy', 'Numerikus-modszerek-Ea', 'Numerikus-modszerek-Gy']
    course_list_5 = ['Mesterseges-intelligencia-Ea', 'Adatbazisok-I-Ea', 'Adatbazisok-I-Gy',
                     'A-szamitaselmelet-alapjai-II-Gy', 'A-szamitaselmelet-alapjai-II-Ea',
                     'Diszkret-modellek-alkalmazasai-Gy', 'Valoszinusegszamitas-es-statisztika-Gy']
    course_list_6 = ['Adatbazisok-II-Ea', 'Telekommunikacios-halozatok-Ea', 'Telekommunikacios-halozatok-Gy']
    net.add_nodes(course_list_1, x = range(len(course_list_1)), y = [0] * len(course_list_1), color = ['#00ff1e'] * len(course_list_1))
    net.add_nodes(course_list_2) #, x = range(len(course_list_1)), y = [0] * len(course_list_1))
    #net.add_nodes(course_list_3)
    #net.add_nodes(course_list_4)
    #net.add_nodes(course_list_5)
    #net.add_nodes(course_list_6)
    """
    net.add_node(1, label="Node 1")
    net.add_node(2)
    nodes = ["a", "b", "c", "d"]
    net.add_nodes(nodes)
    net.add_nodes("hello")
    g = Network()
    g.add_nodes([1,2,3], value=[10, 100, 400],
    title=["I am node 1", "node 2 here", "and im node 3"],
    x=[21.4, 54.2, 11.2],
    y=[100.2, 23.54, 32.1],
    label=["NODE 1", "NODE 2", "NODE 3"],
    color=["#00ff1e", "#162347", "#dd4b39"])
    net.add_node(0, label="a")
    net.add_node(1, label="b")
    net.add_edge(0, 1)
    net.add_edge(0, 1, weight=.87)
    net.show_buttons(filter_=['physics'])
    """
    net.show("mygraph.html")