from prefect import flow
from prefect.artifacts import create_markdown_artifact, create_table_artifact
import urllib.parse as urllp
import pandas as pd
from prefect.runtime import flow_run

@flow(log_prints=True)
def create_artefact_with_link(name: str = "world", done: str = 'Finish'):
    print(f"Create artefact in Prefect ! 🤗")
    df = None
    test = {
        "input": {
            "customer": "Cornelio", "country": "FR", "days": 1, "k": 100
        }, 
        "conditions": [
            {"condition": "value_1:\"76000\" AND value_2:\"124.080727\" and value_3:\"ip_qualification\"", "ratio": 0.3665810036464664}, 
            {"condition": "value_1:\"768000\" AND value_2:\"125033\"", "ratio": 0.35879517795108934},
        ]
    }
    
    input_pattern_value = ""
    for pattern in test["conditions"]:
        pattern["url"] = f"[Link](https://www.google.com/)"
    df = pd.DataFrame(test["conditions"])
    df = df.sort_values(by="ratio", ascending=False)
    for index, row in df.iterrows():
        input_pattern_value += f"| {row['ratio']} | {row['url']} | {row['condition']} |\n"

    input_key_value = ""
    for key, value in test["input"].items():
        input_key_value += f"| {key} | {value} |\n"

    markdown_report = f"""# Report

## Input

| Key        | Value |
|:--------------| :-- |
{input_key_value}

## Conditions

| Ratio        | URL | Condition |
|:--------------| :-- | :-- |
{input_pattern_value}
"""
    create_markdown_artifact(
        key="table-with-link",
        markdown=markdown_report,
        description="Condition report",
    )
    
    # Print flow parameter
    flow_name = flow_run.id
    print(flow_name)

    parameters = flow_run.parameters
    print(parameters)

    # Argument given in function
    print(done)


if __name__ == "__main__":

    create_artefact_with_link.serve(name="artefact-table-with-link",
        tags=["onboarding"],
        parameters={"done": "Execution is finished"},
        interval=60
    )