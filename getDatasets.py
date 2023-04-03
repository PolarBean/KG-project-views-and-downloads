def getDatasets(projectName):
    return {
        "@context": {
            "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
            "query": "https://schema.hbp.eu/myQuery/",
            "propertyName": {"@id": "propertyName", "@type": "@id"},
            "path": {"@id": "path", "@type": "@id"},
        },
        "meta": {
            "type": "https://openminds.ebrains.eu/core/Project",
            "responseVocab": "https://schema.hbp.eu/myQuery/",
        },
        "structure": [
            {
                "propertyName": f"query:{projectName}",
                "path": "https://openminds.ebrains.eu/vocab/fullName",
                "filter": {
                    "op": "EQUALS",
                    "value": f"{projectName}",
                },
            },
            {
                "propertyName": "query:hasPart",
                "path": "https://openminds.ebrains.eu/vocab/hasPart",
            },
        ],
    }
