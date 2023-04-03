from kg_core.kg import kg
# from query import query
from dopamap import dopamap
from getDatasets import getDatasets
from getMetrics import getMetrics
from getVersions import getVersions
kg_client = kg().build()

project = "Map of dopamine receptor positive cell types in the developing and adult mouse brain (DOPAMAP)"

#Get all the datasets related to the project
projectQuery = getDatasets(project)
results = kg_client.queries.test_query(projectQuery)
datasets = [result["hasPart"] for result in results.items()]
# unpack list of lists
datasets = [item["@id"] for sublist in datasets for item in sublist]

#Get all the versions of each dataset
datasetVersions = {}
for dataset in datasets:
    versionQuery = getVersions(dataset)
    results = kg_client.queries.test_query(versionQuery)
    print(list(results.items()))
    result_versions = [i["hasVersion"] for i in results.items()]
    if len(result_versions) == 0:
        continue
    datasetName = [i["fullName"] for i in results.items()][0]

    result_versions = result_versions[0]
    if isinstance(result_versions, list):
        datasetVersions[datasetName] = [item["@id"] for item in result_versions]
    else:
        datasetVersions[datasetName] = [result_versions["@id"]]
    print(datasetVersions)
  
#Get all the metrics of each version

keys = ["last5daysViews", "allTimeViews", "last30daysViews", "last5daysDownloads", "firstReleasedAt", "allTimeDownloads", "last30daysDownloads"]
result_metrics_all = []
for key, value in datasetVersions.items():
    for version in value:
        metricsQuery = getMetrics(version)
        results = kg_client.queries.test_query(metricsQuery)
        result_metrics = list(results.items())[0]
        result_metrics = {key:result_metrics[key] for key in keys}
        result_metrics["versionID"] = version
        result_metrics["project"] = project
        result_metrics["dataset"] = key
        result_metrics_all.append(result_metrics)

# write to csv
import pandas as pd
df = pd.DataFrame(result_metrics_all)
newIndex = ['dataset','last5daysViews', 'last30daysViews','allTimeViews', 
       'last5daysDownloads','last30daysDownloads', 'allTimeDownloads', 'firstReleasedAt', 
       'versionID', 'project']
df = df.reindex(columns=newIndex)
# calculate total views and downloads for all datasets and append as a new row
df.loc['Total'] = df.sum(numeric_only=True, axis=0)

df.to_csv(f"{project}_views_and_downloads.csv", index=False)
