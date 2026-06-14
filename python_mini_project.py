print("nishazareentaj")

state_leaders = {
    "andhra pradesh": {
        "parties": ["YSRCP", "TDP", "JANASENA", "BJP", "CONGRESS", "NOTA"],
        "leaders": ["Jagan Mohan Reddy", "Chandrababu Naidu", "Pawan Kalyan"]
    },
    "tamil nadu": {
        "parties": ["DMK", "AIADMK", "TVK", "BJP", "CONGRESS", "NOTA"],
        "leaders": ["M K Stalin", "Edappadi K Palaniswami", "Vijay", "Jayalalithaa"]
    },
    "karnataka": {
        "parties": ["CONGRESS", "BJP", "JDS", "AAP", "NOTA"],
        "leaders": ["Siddaramaiah", "B S Yediyurappa", "H D Kumaraswamy"]
    },
    "telangana": {
        "parties": ["BRS", "CONGRESS", "BJP", "AIMIM", "NOTA"],
        "leaders": ["KCR", "Revanth Reddy", "Bandi Sanjay"]
    }
}

national_election = {
    "parties": ["BJP", "CONGRESS", "AAP", "NOTA", "Other"],
    "leaders": ["Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Mamata Banerjee"]
}

all_voters = []

for i in range(5):
    age = int(input("Enter your age: "))
    name = input("Enter your name: ")
    aadhar = input("Enter your Aadhar number: ")
    location = input("Enter your location: ")
    state = input("Enter your state: ").lower().strip()

    state_info = state_leaders.get(state)
    if state_info:
        print(f"\nShowing parties for {state.title()}: {', '.join(state_info['parties'])}")
        default_leaders = state_info["leaders"]
    else:
        print(f"\nState '{state}' not found. Using default party and leader lists.")
        default_leaders = ["Unknown Leader 1", "Unknown Leader 2"]

    if age >= 18:
        print(f"{name} is eligible to vote")
        if state_info:
            parties = state_info["parties"] + ["Other"]
            print(f"\nSelect your favourite party from {state.title()} options:")
        else:
            parties = [
                "YSR CONGRESS PARTY",
                "INDIAN NATIONAL CONGRESS PARTY",
                "TELUGHUDHESHAM PARTY",
                "JANASENA PARTY",
                "BJP",
                "Other",
                "NOTA"
            ]
            print("\nSelect your favourite party:")

        for idx, party in enumerate(parties, 1):
            print(f"{idx}. {party}")

        choice_text = input("Enter choice number: ")
        try:
            choice = int(choice_text)
        except ValueError:
            choice = None

        if choice is not None and 1 <= choice <= len(parties):
            selected_party = parties[choice - 1]
        else:
            print("Invalid choice, defaulting to 'Other'.")
            selected_party = "Other"

        print(f"\nState election - choose your favourite cheif minister  candidate in {state.title()}: ")
        for idx, leader in enumerate(default_leaders, 1):
            print(f"{idx}. {leader}")
        state_leader_choice = input("Type your favourite leaderfrom above or other: ")

        print("\nNational election - choose your favourite Prime Minister candidate:")
        for idx, leader in enumerate(national_election["leaders"], 1):
            print(f"{idx}. {leader}")
        national_leader_choice = input("Type your favourite leader from national elections: ")

        print("\nSelect your favourite national party:")
        for idx, party in enumerate(national_election["parties"], 1):
            print(f"{idx}. {party}")
        national_choice_text = input("Enter choice number: ")
        try:
            national_choice = int(national_choice_text)
        except ValueError:
            national_choice = None

        if national_choice is not None and 1 <= national_choice <= len(national_election["parties"]):
            selected_national_party = national_election["parties"][national_choice - 1]
        else:
            print("Invalid choice, defaulting to 'Other'.")
            selected_national_party = "Other"

        cm_qualities = input("Enter qualities you want in your Chief Minister candidate, using commas: ")
        cm_qualities_list = [q.strip() for q in cm_qualities.split(",") if q.strip()]

        pm_qualities = input("Enter qualities you want in your Prime Minister candidate, using commas: ")
        pm_qualities_list = [q.strip() for q in pm_qualities.split(",") if q.strip()]

        print("\nOpinion Section:")
        state_evm_opinion = input("Do you think EVM manipulation happened in the state election? (yes/no): ").strip().lower()
        national_evm_opinion = input("Do you think EVM manipulation happened in the national election? (yes/no): ").strip().lower()
        if state_evm_opinion == "yes" or national_evm_opinion == "yes":
            resign_opinion = input("Do you think the present Chandrababu Naidu and Narendra Modi should resign? (yes/no): ").strip().lower()
            if resign_opinion == "yes":
                print("\nPeople are the government and the government is the people. Fight for your valid vote.\n")
            else:
                benefit = input("So, you like the present government qualities. Enter your government benefits: ")
                print(f"You shared: {benefit}")
        else:
            print("\nSo, you trust the election process and the current government.\n")
            print(list(input("please share your current state government benefits: ").split(",")))
            print(list(input("please share your current national government benefits: ").split(",")))

        user_data = {
            "age": age,
            "name": name,
            "aadhar": aadhar,
            "location": location,
            "state": state.title(),
            "state_party": selected_party,
            "state_chief_minister": state_leader_choice,
            "state_cm_qualities": cm_qualities_list,
            "national_party": selected_national_party,
            "national_prime_minister": national_leader_choice,
            "national_pm_qualities": pm_qualities_list,
            "state_evm_opinion": state_evm_opinion,
            "national_evm_opinion": national_evm_opinion
        }
        all_voters.append(user_data)
        print(f"\nStored details: {user_data}\n")
    else:
        print(f"{name} is not eligible to vote\n")

print("Survey complete. Total voters processed:", len(all_voters))
       