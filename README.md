# Project on AP Politics

This repository contains a small Python script `python_mini_project.py` created as a mini project about AP politics.

## Files

- `python_mini_project.py` — main script

## Usage

Run the script with Python 3.x:

```
python python_mini_project.py
```

## Notes

- Pushed to https://github.com/kolkarnisha/project_on_AP_politics.git

- print("nishazareentaj")
for i in range(5):
    age = int(input("enter your age: "))
    name = str(input("enter your name: "))
    if age >= 18:
        print(f"{name} eligible to vote")
        parties = ["YSR CONGRESS PARTY", "INDIAN NATIONAL CONGRESS PARTY", "TELUGHUDHESHAM PARTY", "JANASENA PARTY", "BJP", "Other", "NOTA"]
        print("\nSelect your favourite party:")
        for idx, party in enumerate(parties, 1):
            print(f"{idx}. {party}")
        
        choice = int(input("Enter choice number: "))
        if 1 <= choice <= len(parties):
            selected_party = parties[choice - 1]
            print(f"{name} selected: {selected_party}")
        else:
            print("Invalid choice, no party selected")
        print()  # Empty line for spacing
            
    else:
        print(f"{name} not eligible to vote\n")
