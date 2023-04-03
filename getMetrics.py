def getMetrics(instanceId):
    return {
        "@context": {
            "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
            "query": "https://schema.hbp.eu/myQuery/",
            "propertyName": {"@id": "propertyName", "@type": "@id"},
            "path": {"@id": "path", "@type": "@id"},
        },
        "meta": {
            "type": "https://core.kg.ebrains.eu/metrics/search/Metric",
            "responseVocab": "https://schema.hbp.eu/myQuery/",
        },
        "structure": [
            {
                "propertyName": "query:allTimeViews",
                "path": "https://core.kg.ebrains.eu/vocab/allTimeViews",
            },
            {
                "propertyName": "query:metricOf",
                "path": "https://core.kg.ebrains.eu/vocab/metricOf",
                "required": True,
                "structure": {
                    "propertyName": f"query:{instanceId}",
                    "path": "@id",
                    "filter": {
                        "op": "EQUALS",
                        "value": f"{instanceId}",
                    },
                },
            },
            {
                "propertyName": "query:allTimeDownloads",
                "path": "https://core.kg.ebrains.eu/vocab/allTimeDownloads",
            },
            {
                "propertyName": "query:last30daysViews",
                "path": "https://core.kg.ebrains.eu/vocab/last30daysViews",
            },
            {
                "propertyName": "query:last30daysDownloads",
                "path": "https://core.kg.ebrains.eu/vocab/last30daysDownloads",
            },
            {
                "propertyName": "query:last5daysViews",
                "path": "https://core.kg.ebrains.eu/vocab/last5daysViews",
            },
            {
                "propertyName": "query:last5daysDownloads",
                "path": "https://core.kg.ebrains.eu/vocab/last5daysDownloads",
            },
            {
                "propertyName": "query:firstReleasedAt",
                "path": "https://core.kg.ebrains.eu/vocab/meta/firstReleasedAt",
            },
        ],
    }
