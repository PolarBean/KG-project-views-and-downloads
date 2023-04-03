def getVersions(datasetID):
    return {
  "@context": {
    "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
    "query": "https://schema.hbp.eu/myQuery/",
    "propertyName": {
      "@id": "propertyName",
      "@type": "@id"
    },
    "path": {
      "@id": "path",
      "@type": "@id"
    }
  },
  "meta": {
    "type": "https://openminds.ebrains.eu/core/Dataset",
    "responseVocab": "https://schema.hbp.eu/myQuery/"
  },
  "structure": [
    {
                "propertyName": f"{datasetID}",
      "path": "@id",
      "filter": {
        "op": "EQUALS",
                    "value": f"{datasetID}",
      }
    },
    {
      "propertyName": "query:hasVersion",
      "path": "https://openminds.ebrains.eu/vocab/hasVersion"
    },
    {
      "propertyName": "query:fullName",
      "path": "https://openminds.ebrains.eu/vocab/fullName"
    }
  ]
}