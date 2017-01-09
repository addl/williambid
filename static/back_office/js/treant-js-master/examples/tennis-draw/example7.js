// source: 
// http://www.atpworldtour.com/Share/Event-Draws.aspx?EventId=410&Year=2013

var tree_structure = {
    chart: {
        container: "#OrganiseChart6",
        levelSeparation: 20,
        siblingSeparation: 15,
        subTeeSeparation: 15,
        rootOrientation: "NORTH",

        node: {
            HTMLclass: "tennis-draw",
            drawLineThrough: true
        },
        connectors: {
            type: "straight",
            style: {
                "stroke-width": 2,
                "stroke": "#ccc"
            }
        }
    },

    nodeStructure: {
        text: {
            name: {
                val: "Your Network",
                href: ""
            }
        },
        HTMLclass: "williambid_node",
        children: [
            {
                text: {
                    name: "Djokovic, Novak",
                    desc: "4-6, 6-2, 6-2"
                },
            },
            {
                text: {
                    name: "Nieminen, Jarkko",
                    desc: "6-3, 1-6, 7-6(3)"
                },

            }
        ]
    }
};
