import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    
    if person is not None:
        person.sort_values(by="id", inplace=True)

        person = person.drop_duplicates(subset=["email"],inplace=True, keep="first")
